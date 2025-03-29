from typing import Optional
from metrogo.data.dataloader import DataLoader


class LineManager:
	def __init__(self, db: DataLoader) -> None:
		self.line_lookup = db.line_lookup
		self.db = db

	def get_line_for_station(self, station1: str, station2: str) -> Optional[str]:
		return self.line_lookup.get((station1, station2))

	def find_terminal_direction(
		self, line: str, current_station: str, next_station: str
	) -> str:
		line_stations = self.db.lines.get(line)
		if line_stations is None:
			raise ValueError(f"Line '{line}' does not exist in stations data.")
		line_stations = self.db.lines[line].stations_names
		try:
			current_index = line_stations.index(current_station)
			next_index = line_stations.index(next_station)
		except ValueError as e:
			raise ValueError(
				'Current station or next station not found in the list of stations.'
			) from e
		if current_index < next_index:
			return self.db.lines[line].stations_names[-1]
		else:
			return self.db.lines[line].stations_names[0]

	@staticmethod
	def get_line_color(line_name: str) -> Optional[str]:
		line_colors = {
			'line_1': 'قرمز',
			'line_parand': 'قرمز',
			'line_2': 'آبی',
			'line_3': 'آبی آسمانی',
			'line_4': 'زرد',
			'line_mehrabad': 'زرد',
			'line_5': 'سبز',
			'line_hashtgerd': 'سبز',
			'line_6': 'صورتی',
			'line_7': 'بنفش',
		}
		return line_colors.get(line_name, None)
