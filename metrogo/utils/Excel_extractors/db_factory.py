from pathlib import Path
import json


def run():
	import metrogo.utils.Excel_extractors.extractors.line_1 as line_1
	import metrogo.utils.Excel_extractors.extractors.line_2 as line_2
	import metrogo.utils.Excel_extractors.extractors.line_3 as line_3
	import metrogo.utils.Excel_extractors.extractors.line_4 as line_4
	import metrogo.utils.Excel_extractors.extractors.line_5 as line_5
	import metrogo.utils.Excel_extractors.extractors.line_6 as line_6
	import metrogo.utils.Excel_extractors.extractors.line_7 as line_7
	import metrogo.utils.Excel_extractors.extractors.parand as parand
	import metrogo.utils.Excel_extractors.extractors.mehrabad as mehrabad
	import metrogo.utils.Excel_extractors.extractors.hashtgerd as hashtgerd
	from metrogo.data.db.stations_template import stations_template

	x = {
		'line_1': line_1.line_1(),
		'line_2': line_2.line_2(),
		'line_3': line_3.line_3(),
		'line_4': line_4.line_4(),
		'line_5': line_5.line_5(),
		'line_6': line_6.line_6(),
		'line_7': line_7.line_7(),
		'line_parand': parand.parand(),
		'line_mehrabad': mehrabad.mehrabad(),
		'line_hashtgerd': hashtgerd.hashtgerd(),
	}

	for i in [
		'line_1',
		'line_parand',
		'line_2',
		'line_3',
		'line_4',
		'line_mehrabad',
		'line_5',
		'line_6',
		'line_7',
		'line_hashtgerd',
	]:
		times = x[i][i]
		flg = True
		for key, items in times.items():
			for key_2, items_2 in items.items():
				items_2_iter = iter(items_2.items())
				current_item = next(items_2_iter, None)

				for final_item in stations_template[i.replace('line_', '')].items():
					[key_3, items_3] = current_item

					if final_item[1]['active']:
						if flg:
							stations_template[i.replace('line_', '')][final_item[0]][
								'Train_arrival_time'
							] = {}
							flg = False

						if final_item[1]['Train_arrival_time'].get(key) == None:
							stations_template[i.replace('line_', '')][final_item[0]][
								'Train_arrival_time'
							][key] = {}

						if final_item[1]['Train_arrival_time'][key].get(key_2) == None:
							stations_template[i.replace('line_', '')][final_item[0]][
								'Train_arrival_time'
							][key][key_2] = {}

						current_item = next(items_2_iter, current_item)

						stations_template[i.replace('line_', '')][final_item[0]][
							'Train_arrival_time'
						][key][key_2] = items_3
					else:
						continue

	with open(
		Path.cwd() / 'metrogo' / 'data' / 'db' / 'db.py', 'w', encoding='UTF-8'
	) as file:
		file.write(
			f'db = {json.dumps(stations_template, ensure_ascii=False)}'.replace(
				'true', 'True'
			).replace('false', 'False')
		)


run()
