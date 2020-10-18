import glob
import json


def template_for_one(gost):
	template_for_one = '''# {short_name}

#### {full_name}{description}{annotation}{attributes}

<a onclick="openFileCallback(\'{download_gost_url}\', \'{short_name}.pdf\');" href="#">[Читать в PDF]</a>'''
	
	string_attributes = '\n'.join([f'- {attr_key}: {attr_value}' for attr_key, attr_value in gost['attributes'].items()])
	return template_for_one.format(
		short_name=gost['short_name'],
		full_name=gost['full_name'],
		description=f'\n\n{gost["description"]}' if gost['description'] else '',
		annotation=f'\n\n{gost["annotation"]}' if gost['annotation'] else '',
		attributes=f'\n\n{string_attributes}' if string_attributes else '',
		download_gost_url=gost['download_gost_url']
	)


def parse_mds_from_jsons():
	fnames = glob.glob('gosts/*.json')
	gosts_length = len(fnames)
	for index, fname in enumerate(fnames):
		with open(fname, 'r', encoding='utf-8') as f:
			gost_json = json.load(f)
		md_string = template_for_one(gost_json)
		with open(f'gost_mds/{gost_json["short_name"]}.md', 'w', encoding='utf-8') as f:
			f.write(md_string)
		print('-' * 15, f'{index + 1}/{gosts_length}', '-' * 15)
	print('BADABOOM')


if __name__ == '__main__':
	parse_mds_from_jsons()
