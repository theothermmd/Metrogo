from typing import Optional
from rapidfuzz import process


class WordUtils:
	@staticmethod
	def correct_persian_text(text: str) -> str:
		translation_map = str.maketrans(
			{
				'ي': 'ی',
				'ك': 'ک',
				'ە': 'ه',
				'إ': 'ا',
				'ؤ': 'و',
				'ء': '',
				'ة': 'ه',
				'٫': '.',
				'٬': ',',
				'ّ': '',
				'\u200c': ' ',
			}
		)
		return text.translate(translation_map)

	@staticmethod
	def find_closest_word(
		input_word: str, words_list: list, score_threshold: int = 70
	) -> Optional[str]:
		result = process.extractOne(input_word, words_list)
		if result is None:
			return None
		closest_match, score, _ = result
		return closest_match if score > score_threshold else None
