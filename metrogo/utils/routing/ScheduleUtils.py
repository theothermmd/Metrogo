from datetime import datetime, timedelta
from typing import List, Optional, Union


class TimeServices:
	@staticmethod
	def parse_time(time_str: str) -> datetime:
		return datetime.strptime(time_str, '%H:%M')

	@staticmethod
	def format_duration(duration: timedelta) -> str:
		total_minutes = int(duration.total_seconds() // 60)
		hours, minutes = divmod(total_minutes, 60)
		return f'{hours:02}:{minutes:02}'

	@staticmethod
	def is_time_valid(time_str: Optional[str]) -> bool:
		return time_str not in [None, '', 'None', 'none']


class ScheduleManager:
	@staticmethod
	def get_next_time(
		station_times: List[str], current_time: Union[str, datetime]
	) -> Optional[str]:
		if isinstance(current_time, str):
			try:
				current_time = TimeServices.parse_time(current_time)
			except ValueError as e:
				raise ValueError(
					f'فرمت نامعتبر برای current_time: {current_time}'
				) from e

		for time_str in station_times:
			if not TimeServices.is_time_valid(time_str):
				continue
			try:
				next_time = TimeServices.parse_time(time_str)
			except ValueError as e:
				raise ValueError(f'فرمت نامعتبر برای time_str: {time_str}') from e

			if next_time > current_time:
				return next_time
		return None
