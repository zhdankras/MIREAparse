import requests
from bs4 import BeautifulSoup
import xlrd

HOST = 'https://www.mirea.ru/'
URL = 'https://www.mirea.ru/schedule/'
HEADERS = {
	'Accept': '*/*',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

def get_file(url):
	r = requests.get(url, headers=HEADERS)
	return r

def get_content():
	soup = BeautifulSoup(get_file(URL).content, 'html.parser')
	items = soup.find_all('div', class_='uk-width-1-2')
	urls = []
	for item in items:
		urls.append(item.find('a').get('href'))
	return urls
print((get_content()))

def get_name(url):
	name = url.split('/')[-1]
	return name

def save_image(name, file_object):
	with open(name, 'bw') as f:
		for chunk in file_object.iter_content(8192):
			f.write(chunk)

def main():
	for url in get_content():
		save_image(get_name(url), get_file(url))

if __name__ == '__main__':
	main()
	import parserasp