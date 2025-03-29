from datetime import datetime, time
from typing import Dict, List, Optional, Any

from metrogo.data.dataloader import DataLoader
from metrogo.utils.routing.LineUtils import LineManager
from metrogo.utils.routing.Pathfinder import Routing
from metrogo.utils.routing.ScheduleUtils import ScheduleManager, TimeServices
from metrogo.utils.routing.TravelInfo import TravelInfo
from metrogo.utils.words.WordUtils import WordUtils

data_manager = DataLoader()
line_manager = LineManager(data_manager)
routing = Routing(data_manager)

METRO_START_TIME: datetime = datetime.strptime('05:00', '%H:%M')
METRO_END_TIME: datetime = datetime.strptime('23:00', '%H:%M')
DISTANCE_STEP: int = 2  # The distance between the two metro stations is usually 2 km


def find_best_route(
	source: str,
	destination: str,
	type_day: str = 'عادی',
	current_time_str: Optional[str] = None,
) -> Dict[str, Any]:
	if source == destination:
		return {
			'status': True,
			'isrouting': False,
			'message': 'The origin and destination stations cannot be the same.',
		}

	if type_day not in ['عادی', 'پنجشنبه', 'جمعه']:
		return {
			'status': True,
			'isrouting': False,
			'message': 'Days of the week are not valid.',
		}

	source_corrected: Optional[str] = WordUtils.find_closest_word(
		input_word=source, words_list=data_manager.stations_names
	)
	destination_corrected: Optional[str] = WordUtils.find_closest_word(
		input_word=destination, words_list=data_manager.stations_names
	)

	if source_corrected is None or destination_corrected is None:
		if source_corrected is None and destination_corrected is None:
			message: str = (
				'The names of the origin and destination stations are not valid.'
			)
		elif source_corrected is None:
			message: str = 'The origin station name is not valid.'
		else:
			message: str = 'The destination station name is not valid.'

		return {'status': True, 'isrouting': False, 'message': message}

	current_time: datetime = (
		TimeServices.parse_time(current_time_str)
		if current_time_str
		else datetime.now()
	)

	if not (METRO_START_TIME.time() < current_time.time() < METRO_END_TIME.time()):
		return {
			'status': True,
			'isrouting': False,
			'message': 'The metro is not operating.',
		}

	start_time: datetime = current_time

	route: List[str] = routing.find_fastest_route(
		source=source_corrected, destination=destination_corrected
	)

	if not route or len(route) < 2:
		return {'status': True, 'isrouting': False, 'message': 'No valid route found.'}

	current_line: str = line_manager.get_line_for_station(route[0], route[1])
	terminal_direction: str = line_manager.find_terminal_direction(
		current_line, route[0], route[1]
	)
	overview: List[Dict[str, str, str, bool, str]] = []
	travel_guide: List[str] = []
	travel_distance: int = 0
	next_train: Optional[str] = None

	for i in range(len(route)):
		if i < len(route) - 1:
			next_line: str = line_manager.get_line_for_station(route[i], route[i + 1])
			if next_line != current_line:
				time_list: List = (
					data_manager.lines[current_line]
					.get_stations_by_name(route[i])
					.train_arrival_time[type_day][terminal_direction]
				)

				updated_time: Optional[datetime] = ScheduleManager.get_next_time(
					time_list, current_time
				)
				if updated_time is None:
					return {
						'status': True,
						'isrouting': False,
						'message': 'You will not reach your destination station.',
					}
				current_time = updated_time

				TravelInfo.add_overview_entry(
					overview,
					route[i],
					current_time.strftime('%H:%M'),
					current_line,
					True,
					f'در ایستگاه {route[i]} از قطار پیاده شده و به سمت {terminal_direction} جهت تغییر خط به {next_line.replace("line_", "")} اقدام کنید.',
				)
				TravelInfo.add_travel_guide_entry(
					'change',
					travel_guide,
					route[i],
					next_line.replace('line_', ''),
					terminal_direction,
				)

				current_line = next_line
				terminal_direction = line_manager.find_terminal_direction(
					current_line, route[i], route[i + 1]
				)

				time_list: List = (
					data_manager.lines[current_line]
					.get_stations_by_name(route[i])
					.train_arrival_time[type_day][terminal_direction]
				)
				updated_time: Optional[datetime] = ScheduleManager.get_next_time(
					time_list, current_time
				)

				if updated_time is None:
					return {
						'status': True,
						'isrouting': False,
						'message': 'You will not reach your destination station.',
					}

				current_time = updated_time
				TravelInfo.add_overview_entry(
					overview,
					route[i],
					current_time.strftime('%H:%M'),
					current_line,
					False,
					'',
				)
				travel_distance += DISTANCE_STEP

			else:
				if i == 0:
					TravelInfo.add_travel_guide_entry(
						'source',
						travel_guide,
						route[i],
						next_line.replace('line_', ''),
						terminal_direction,
					)
					current_line: str = next_line
					time_list: List = (
						data_manager.lines[current_line]
						.get_stations_by_name(route[i])
						.train_arrival_time[type_day][terminal_direction]
					)

					updated_time: Optional[datetime] = ScheduleManager.get_next_time(
						time_list, current_time
					)

				if updated_time is None:
					return {
						'status': True,
						'isrouting': False,
						'message': 'You will not reach your destination station.',
					}

				current_time: Optional[datetime] = updated_time

				TravelInfo.add_overview_entry(
					overview,
					route[i],
					current_time.strftime('%H:%M'),
					current_line,
					False,
					'',
				)
				travel_distance += DISTANCE_STEP

				if i == 0:
					wait_duration = current_time - start_time
					next_train = str(wait_duration.seconds // 60)

		else:
			terminal_direction = line_manager.find_terminal_direction(
				current_line, route[i - 1], route[i]
			)

			dest_line = line_manager.get_line_for_station(route[i], route[i - 1])
			time_list: List = (
				data_manager.lines[current_line]
				.get_stations_by_name(route[i])
				.train_arrival_time[type_day][terminal_direction]
			)
			updated_time = ScheduleManager.get_next_time(time_list, current_time)
			if updated_time is None:
				return {
					'status': True,
					'isrouting': False,
					'message': 'You will not reach your destination station.',
				}
			current_time = (
				TimeServices.parse_time(updated_time)
				if isinstance(updated_time, str)
				else updated_time
			)
			TravelInfo.add_overview_entry(
				overview,
				route[i],
				current_time.strftime('%H:%M'),
				current_line,
				False,
				'',
			)
			TravelInfo.add_travel_guide_entry(
				'destination',
				travel_guide,
				route[i],
				dest_line.replace('line_', ''),
				terminal_direction,
			)
			travel_distance += DISTANCE_STEP

	travel_duration = TimeServices.format_duration(current_time - start_time)
	cost = TravelInfo.check_cost(travel_distance)

	return {
		'status': True,
		'isrouting': True,
		'route': overview,
		'travel_duration': travel_duration,
		'travel_distance': cost,
		'travel_guide': travel_guide,
		'next_train': next_train,
		'arrival_time': current_time.strftime('%H:%M'),
	}
