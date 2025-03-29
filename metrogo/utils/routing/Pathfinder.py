from dijkstar import Graph, find_path
from typing import List, Optional
from metrogo.data.dataloader import DataLoader


class Routing:
	def __init__(self, db: DataLoader) -> None:
		self.lines = db.lines
		self.stations_line = db.stations_line

		self.graph = {'lines': {}, 'linetoline': {}, 'all': Graph()}

		for line, stations in self.lines.items():
			line_graph = Graph()
			for station_a, station_b in zip(stations.stations, stations.stations[1:]):
				line_graph.add_edge(
					station_a.get_persian_name(), station_b.get_persian_name(), 1
				)
				line_graph.add_edge(
					station_b.get_persian_name(), station_a.get_persian_name(), 1
				)
			self.graph['lines'][line] = line_graph

		for line, stations in self.lines.items():
			self.graph['linetoline'][line] = {}
			for other_line, other_stations in self.lines.items():
				if line == other_line:
					continue

				if set(
					[station.get_persian_name() for station in stations.stations]
				).intersection(
					[station.get_persian_name() for station in other_stations.stations]
				):
					linetoline_graph = Graph()

					for station_a, station_b in zip(
						stations.stations, stations.stations[1:]
					):
						linetoline_graph.add_edge(
							station_a.get_persian_name(),
							station_b.get_persian_name(),
							1,
						)
						linetoline_graph.add_edge(
							station_b.get_persian_name(),
							station_a.get_persian_name(),
							1,
						)

					for station_a, station_b in zip(
						other_stations.stations, other_stations.stations[1:]
					):
						linetoline_graph.add_edge(
							station_a.get_persian_name(),
							station_b.get_persian_name(),
							1,
						)
						linetoline_graph.add_edge(
							station_b.get_persian_name(),
							station_a.get_persian_name(),
							1,
						)
					self.graph['linetoline'][line][other_line] = linetoline_graph

		all_graph = Graph()
		for _, stations in self.lines.items():
			for station_a, station_b in zip(stations.stations, stations.stations[1:]):
				all_graph.add_edge(
					station_a.get_persian_name(), station_b.get_persian_name(), 1
				)
				all_graph.add_edge(
					station_b.get_persian_name(), station_a.get_persian_name(), 1
				)
		self.graph['all'] = all_graph

	@staticmethod
	def find_intersection(arr1: List[str], arr2: List[str]) -> Optional[List[str]]:
		intersection = list(set(arr1) & set(arr2))
		return intersection if intersection else None

	def find_fastest_route(self, source: str, destination: str) -> List[str]:
		common_lines = self.find_intersection(
			self.stations_line[source], self.stations_line[destination]
		)

		if common_lines is not None and len(common_lines) == 1:
			line = common_lines[0]
			return find_path(self.graph['lines'][line], source, destination)[0]

		else:
			src_lines = self.stations_line[source]
			dest_lines = self.stations_line[destination]

			if len(src_lines) == 1 and len(dest_lines) == 1:
				src_line = src_lines[0]
				dest_line = dest_lines[0]
				if (
					src_line in self.graph['linetoline']
					and dest_line in self.graph['linetoline'][src_line]
				):
					return find_path(
						self.graph['linetoline'][src_line][dest_line],
						source,
						destination,
					)[0]

			for src_line in src_lines:
				if src_line in self.graph['linetoline']:
					for dest_line in dest_lines:
						if dest_line in self.graph['linetoline'][src_line]:
							return find_path(
								self.graph['linetoline'][src_line][dest_line],
								source,
								destination,
							)[0]

			return find_path(self.graph['all'], source, destination)[0]
