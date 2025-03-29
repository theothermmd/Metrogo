from typing import List, Dict
from metrogo.utils.words.WordUtils import WordUtils


class Station:
	def __init__(
		self,
		name: str,
		translations: Dict[str, str],
		address: str,
		lines: List[str],
		location: Dict[str, float],
		colors: List[str],
		active: bool,
		wc: bool,
		coffee_shop: bool,
		grocery_store: bool,
		fastfood: bool,
		perfumeshop: bool,
		atm: bool,
		parking: bool,
		relations: List[str],
		train_arrival_times: List[str],
		Time_interval_to_the_previous_station: int,
		Time_interval_to_the_next_station: int,
	):
		self.name = name
		self.translations = translations
		self.address = address
		self.lines = lines
		self.location = location
		self.colors = colors
		self.active = active
		self.wc = wc
		self.coffee_shop = coffee_shop
		self.grocery_store = grocery_store
		self.fastfood = fastfood
		self.perfumeshop = perfumeshop
		self.atm = atm
		self.parking = parking
		self.relations = relations
		self.train_arrival_time = train_arrival_times
		self.Time_interval_to_the_previous_station = (
			Time_interval_to_the_previous_station
		)
		self.Time_interval_to_the_next_station = Time_interval_to_the_next_station

	def get_persian_name(self) -> str:
		return WordUtils.correct_persian_text(self.translations.get('fa', self.name))

	def get_english_name(self) -> str:
		return self.translations.get('en', self.name)

	def is_on_line(self, line: str) -> bool:
		return line in self.lines

	def has_facility(self, facility: str) -> bool:
		facilities = {
			'wc': self.wc,
			'coffee_shop': self.coffee_shop,
			'grocery_store': self.grocery_store,
			'fast_food': self.fast_food,
			'atm': self.atm,
		}
		return facilities.get(facility, False)

	def update_arrival_times(self, new_times: List[str]):
		self.train_arrival_times = new_times

	def __str__(self):
		return f'ایستگاه: {self.get_persian_name()}, خطوط: {self.lines}, موقعیت: {self.location}, زمان‌های رسیدن: {self.train_arrival_time}'
