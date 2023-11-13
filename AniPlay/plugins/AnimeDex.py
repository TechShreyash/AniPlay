import requests
import urllib.parse
from AniPlay.plugins.other import emoji


class AnimeDex:
    def __init__(self) -> None:
        pass

    def search(query):
        url = 'https://api.anime-dex.workers.dev/search/' + \
            str(urllib.parse.quote(query))
        data =requests.get(url).json()['results']
        return data
        
    def anime(id):
        data =requests.get('https://api.anime-dex.workers.dev/anime/'+id).json()['results']

        title = data['name']
        text = f'{emoji()} **{title}**\n'
        img = data['image']

        item = []
        
        for i,j in item:
            text += '\n' + i.title().strip() +' : '+ j.strip().replace('\n', ' ')

        text += f"\nGenres: {data['genre']}"
        ep = int(data['episodes'])
        eplist =[]
        for i in range(1,ep+1):
            eplist.append((i,f'{id}-episode-{i}'))
            

        return img, text, eplist

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
