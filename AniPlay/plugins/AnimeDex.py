import requests
import urllib.parse
from bs4 import BeautifulSoup as bs
from AniPlay.plugins.other import emoji


class AnimeDex:
    def __init__(self) -> None:
        pass

    def search(query):
        url = 'https://animedex.live/search?query=' + \
            str(urllib.parse.quote(query))
        soup = bs(requests.get(url).content, 'html.parser')
        animes = []

        for anime in soup.find('div', 'divox').find_all('a'):
            title = anime.find('h3').text
            url = 'https://animedex.live' + anime.get('href')
            animes.append((title, url))
        return animes

    def anime(url):
        soup = bs(requests.get(url).content, 'html.parser')

        title = soup.find('h1').text
        text = f'{emoji()} **{title}**\n'
        img = soup.find('div', 'poster').find('img').get('src')

        item = soup.find_all('div', 'info-items')[2:-1]
        for i in item:
            text += '\n' + i.text.strip().replace('\n', ' ')

        genres = soup.find('div', 'info-items genre').find_all('a')
        text += '\nGenres: '
        for i in genres:
            text += i.text + ', '
        text = text[:-2]

        ep = []
        eps = soup.find_all('a', 'ep-btn')
        for i in eps:
            ep.append((i.text, 'https://animedex.live' + i.get('href')))

        return img, text, ep

    def episode(url):
        soup = bs(requests.get(url).content, 'html.parser')
        text = soup.find('b').text

        sub = soup.find('div', 'server').find_all('div', 'sitem')
        surl = []
        for i in sub:
            url = 'https://animedex.live' + \
                i.find('a').get('data-value').split(' ')[0]
            surl.append((i.text.strip(), url))

        dub = soup.find('div', 'server sd')
        durl = []
        if dub:
            for i in dub.find_all('div', 'sitem'):
                url = 'https://animedex.live' + \
                    i.find('a').get('data-value').split(' ')[0]
                durl.append((i.text.strip(), url))

        return text, surl, durl
