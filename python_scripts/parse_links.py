import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://standartgost.ru'
URL = 'https://standartgost.ru/0/559-gelioenergetika?page={page}'


def get_list_of_gosts(page):
	str_page = requests.get(URL.format(page=page)).text
	soup = BeautifulSoup(str_page, 'html5lib')
	gosts = list()
	for li in soup.find_all('li', class_='list-group-item'):
		is_relevant = 0 if 'gost_disabled' in str(li) else 1
		url = BASE_URL + li.find("span").find("a").get("href")
		gosts.append((url, is_relevant,))

	return gosts


def export_to_txt(gosts):
	with open('gosts1.txt', 'w', encoding='utf-8') as f:
		formatted = '\n'.join([','.join(map(str, gost)) for gost in gosts])
		f.write(formatted)


if __name__ == '__main__':
	gosts, page = list(), 1
	while True:
		new_gosts = get_list_of_gosts(page)
		page += 1
		if not new_gosts:
			break
		gosts += new_gosts
	export_to_txt(gosts)
