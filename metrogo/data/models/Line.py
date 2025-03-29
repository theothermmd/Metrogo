from typing import List
from metrogo.data.models.Station import Station


class Line:
	def __init__(self, name: str, stations: List[Station]):
		self.name = name
		self.stations = [i for i in stations if i.active]
		self.stations_names = [station.get_persian_name() for station in self.stations]
		self.terminals = [stations[0], stations[-1]]

	def get_stations(self) -> List[Station]:
		return self.stations

	def get_stations_by_name(self, name: str) -> Station:
		for i in self.stations:
			if i.name == name:
				return i
		return None

	def get_terminals(self) -> List[Station]:
		return self.terminals

	def add_station(self, station: Station):
		self.stations.append(station)

	def __str__(self):
		station_names = [station.get_persian_name() for station in self.stations]
		return f'خط: {self.name}, ایستگاه‌ها: {", ".join(station_names)}'
