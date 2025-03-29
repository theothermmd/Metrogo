from metrogo.data.models.Station import Station
from metrogo.data.models.Line import Line
from collections import defaultdict

from metrogo.data.db.db import db


class DataLoader:
	def __init__(self) -> None:
		self.db = db
		self.lines = {}
		self.line_lookup = {}
		for line_name in self.db:
			stations_list = []
			for station in self.db[line_name]:
				stations_list.append(
					Station(
						station,
						self.db[line_name][station]['translations'],
						self.db[line_name][station]['address'],
						self.db[line_name][station]['lines'],
						self.db[line_name][station]['location'],
						self.db[line_name][station]['colors'],
						self.db[line_name][station]['active'],
						self.db[line_name][station]['wc'],
						self.db[line_name][station]['coffeeShop'],
						self.db[line_name][station]['groceryStore'],
						self.db[line_name][station]['fastFood'],
						self.db[line_name][station]['perfumeshop'],
						self.db[line_name][station]['atm'],
						self.db[line_name][station]['parking'],
						self.db[line_name][station]['relations'],
						self.db[line_name][station]['Train_arrival_time'],
						self.db[line_name][station][
							'Time_interval_to_the_previous_station'
						],
						self.db[line_name][station][
							'Time_interval_to_the_next_station'
						],
					)
				)
			self.lines[line_name] = Line(name=line_name, stations=stations_list)

		for line, stations in self.lines.items():
			for station_a, station_b in zip(stations.stations, stations.stations[1:]):
				self.line_lookup[
					(station_a.get_persian_name(), station_b.get_persian_name())
				] = line
				self.line_lookup[
					(station_b.get_persian_name(), station_a.get_persian_name())
				] = line

		stations_line = defaultdict(list)
		for line, stations in self.lines.items():
			for station in stations.stations:
				if line not in stations_line[station.get_persian_name()]:
					stations_line[station.get_persian_name()].append(line)
		self.stations_line = dict(stations_line)

		self.stations_names = []
		for _, stationx in self.lines.items():
			for station in stationx.stations:
				self.stations_names.append(station.get_persian_name())
