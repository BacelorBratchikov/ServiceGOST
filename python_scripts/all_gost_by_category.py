import glob
import json
import os


EMPTY_CATEGORY_TEMPLATE = '# {}'

md_strings = dict(
	wind=dict(
		term=['Термины и определения', ''],
		requirements=['Технические требования', ''],
		measurement=['Измерения', ''],
		safety=['Безопасность', ''],
		control=['Контроль', ''],
		recommendations=['Рекомендации', ''],
		index=['Ветроэнергетика', ''],
	),
	solar=dict(
		term=['Термины и определения', ''],
		requirements=['Технические требования', ''],
		measurement=['Измерения', ''],
		safety=['Безопасность', ''],
		control=['Контроль', ''],
		recommendations=['Рекомендации', ''],
		index=['Гелеоэнергетика', ''],
	),
)


def write_to_mds():
	for gost_type, categories_dict in md_strings.items():
		try:
			os.mkdir(gost_type)
		except FileExistsError:
			pass
		for category, category_list in categories_dict.items():
			with open(f'{gost_type}/{category}.md', 'w', encoding='utf-8') as f:
				template = EMPTY_CATEGORY_TEMPLATE.format(category_list[0])
				template += category_list[1]

				f.write(template)


def classify_gost_to_categories(gost):
	template_for_gost_link = '\n\n<b>[ГОСТ Р {short_name}](~/gost_mds/{short_name}.md)</b><br/>[{full_name}](~/gost_mds/{short_name}.md)<br/><a onclick="openFileCallback(\'{download_gost_url}\', \'{short_name}.pdf\');" href="#">[Читать в PDF]</a>'

	for category in gost['categories']:
		md_strings[gost['type']][category][1] += template_for_gost_link.format(
			short_name=gost['short_name'],
			full_name=gost['full_name'],
			download_gost_url=gost['download_gost_url']
		)
		md_strings[gost['type']]['index'][1] += template_for_gost_link.format(
			short_name=gost['short_name'],
			full_name=gost['full_name'],
			download_gost_url=gost['download_gost_url']
		)


if __name__ == '__main__':
	fnames = glob.glob('gosts/*.json')
	gosts_length = len(fnames)
	for index, fname in enumerate(fnames):
		with open(fname, 'r', encoding='utf-8') as f:
			gost_json = json.load(f)
		classify_gost_to_categories(gost_json)
		print('-' * 15, f'{index + 1}/{gosts_length}', '-' * 15)
	write_to_mds()
	print('BADABADABOOM')
