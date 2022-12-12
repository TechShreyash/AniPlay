import requests as r
import matplotlib.pyplot as plt
import random
from string import hexdigits
cache = []


def hash():
    while True:
        hash = ''.join(random.choices(hexdigits, k=10))
        if hash not in cache:
            cache.append(hash)
            break
    return hash


def day():
    a = r.get('https://animedex-api.azurewebsites.net').json()['per day']

    total = []
    anime = []
    ep = []

    for i in a:
        b = i.find("'watch'")+9
        j = i[b:]
        b = j.find("'views'")-2
        s1 = int(j[:b])
        b = b + 11
        s2 = int(j[b:-1])

        total.append(s1+s2)
        anime.append(s2)
        ep.append(s1)

    plt.plot(total, label='Total')
    plt.plot(anime, label='Anime')
    plt.plot(ep, label='Episode')

    plt.title('AnimeDex Stats Graph | Per Day Views')
    plt.xlabel('Days')
    plt.ylabel('Views')
    plt.legend()
    n = hash()+'.jpg'
    plt.savefig(n)
    plt.close()
    return n


def over():
    a = r.get('https://animedex-api.azurewebsites.net').json()['per day']

    total = []
    anime = []
    ep = []

    x1, x2, x3 = 0, 0, 0

    for i in a:
        b = i.find("'watch'")+9
        j = i[b:]
        b = j.find("'views'")-2
        s1 = int(j[:b])
        b = b + 11
        s2 = int(j[b:-1])

        x1 += s1+s2
        x2 += s1
        x3 += s2
        total.append(x1)
        anime.append(x3)
        ep.append(x2)

    plt.plot(total, label='Total')
    plt.plot(anime, label='Anime')
    plt.plot(ep, label='Episode')

    plt.title('AnimeDex Stats Graph | Overall Views')
    plt.xlabel('Days')
    plt.ylabel('Views')
    plt.legend()
    n = hash()+'.jpg'
    plt.savefig(n)
    plt.close()
    return n
