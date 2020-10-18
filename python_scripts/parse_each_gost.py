from bs4 import BeautifulSoup
import requests
import json


BASE_URL = 'https://standartgost.ru'
CATEGORIES_KWARGS = dict(
	term=['определения', 'термины', 'основные параметры', 'словарь'],
	requirements=['требования', 'технические условия', 'проверка работоспособности', 'эксплуатационные характеристики', 'техническим требованиям', 'рабочие характеристики'],
	measurement=['измерени', 'методы определения', 'испытани', 'определение'],
	safety=['безопасност', 'меры защиты'],
	control=['контрол', 'управлени'],
	recommendations=['рекомендации'],
)


def choose_categories(title):
	categories = list()
	for category_name, kw_list in CATEGORIES_KWARGS.items():
		for kw in kw_list:
			if kw.lower() in title.lower():
				categories.append(category_name)
				break

	return categories


def get_replaced_gost_url(url):
	soup = BeautifulSoup(requests.get(url).text, 'html5lib')
	try:
		replaced_uri = soup.find('div', class_='alert alert-warning').find('b').find('a').get('href')
	except AttributeError:
		return ''

	return BASE_URL + replaced_uri


def get_attributes_of_gost(url):
	attrs = dict()
	soup = BeautifulSoup(requests.get(url).text, 'html5lib')

	full_name_block = soup.find('small', attrs={'itemprop': 'description'})
	full_name = full_name_block.text.strip() if full_name_block is not None else ''
	attrs['full_name'] = full_name
	attrs['categories'] = choose_categories(full_name)

	description_block = soup.find('div', class_='gost_description')
	attrs['description'] = description_block.find('p').text.strip() if description_block is not None else ''

	table_block = soup.find('table', class_='table gost_info')
	trs = table_block.find('tbody').find_all('tr') if table_block is not None else list()
	attrs['attributes'] = dict()
	for tr in trs:
		attrs['attributes'][tr.find('th').text.strip()] = tr.find('td').text.strip()

	annotation_block = soup.find('div', class_='alert alert-default')
	attrs['annotation'] = annotation_block.find('p').text.strip() if annotation_block is not None else ''

	return attrs


def import_gosts_from_txt(fname, type_):
	str_gosts = None
	gosts = list()
	with open(fname, 'r', encoding='utf-8') as f:
		str_gosts = f.read()
		for str_gost in str_gosts.split('\n'):
			is_relevant = bool(int(str_gost.split(',')[1]))
			url = str_gost.split(',')[0]
			gosts.append((url, is_relevant, type_,))

	return gosts


def get_json_of(url, is_relevant, type_):
	dict_gost = dict(
		type=type_,
		short_name=url.split('/')[-1],
		gost_url=url,
		download_gost_url=f'{url}.pdf',
		is_relevant=is_relevant
	)
	replaced_gost_url = ''
	if not is_relevant:
		replaced_gost_url = get_replaced_gost_url(url)
	dict_gost['replaced_gost_url'] = replaced_gost_url
	for k, v in get_attributes_of_gost(url).items():
		dict_gost[k] = v

	return dict_gost


def save_json(json_gost):
	fname = json_gost['gost_url'].split('/')[-1] + '.json'
	with open('/'.join(('gosts', fname,)), 'w', encoding='utf-8') as f:
		f.write(json.dumps(json_gost))


if __name__ == '__main__':
	gosts = import_gosts_from_txt('gosts_solar.txt', 'solar') + import_gosts_from_txt('gosts_wind.txt', 'wind')
	gosts_length = len(gosts)
	for index, gost in enumerate(gosts):
		json_gost = get_json_of(*gost)
		print(json.dumps(json_gost, indent=4, ensure_ascii=False))
		print('-' * 15, f'{index + 1}/{gosts_length}', '-' * 15)
		save_json(json_gost)
	print('BOOM')
