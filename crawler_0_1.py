import requests
from bs4 import BeautifulSoup

url_array = []
urls_new = set()
with open("url's.txt", 'r') as url_s:
    for url in url_s:
        url_array += [url.strip()]

library = []
with open('library.txt', 'r', encoding='utf8') as file:
    for line in file:
        library += [line.strip()]


for i in range(len(url_array)):

    request = requests.get(url_array[i])

    soup = BeautifulSoup((request.text), "lxml")

    main_information = soup.find('div', {'id' : 'bodyContent'})

    if i == len(library):
        filename = str(i + 1) + '.txt'
        library += ['data/' + filename]
        with open('library.txt', 'a', encoding='utf8') as file:
            file.write('data/' + filename + '\n')

    with open(library[i], 'w', encoding='utf8') as file:
        file.write(main_information.text)

    for word in main_information.text.split():
        if 'www' in word:
            urls_new.update({word})

with open("url's_new.txt", 'a', encoding='utf8') as file:
    for word in urls_new:
        file.write(word + '\n')
