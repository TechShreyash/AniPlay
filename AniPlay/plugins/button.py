from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from string import hexdigits

cache = dict()


def get_hash(data, back):
    while True:
        hash = "".join(random.choices(hexdigits, k=10))
        if not cache.get(hash):
            cache[hash] = (data, back)
            break
    return hash


def get_hash_btn(data: None, hash: None):
    if hash:
        cache[hash] = data
        return hash

    if not data:
        while True:
            hash = "".join(random.choices(hexdigits, k=10))
            if not cache.get(hash):
                cache[hash] = ""
                break
    else:
        while True:
            hash = "".join(random.choices(hexdigits, k=10))
            if not cache.get(hash):
                cache[hash] = data
                break
    return hash


def get_hash_anime(data):
    while True:
        hash = "".join(random.choices(hexdigits, k=10))
        if not cache.get(hash):
            cache[hash] = data
            break
    return hash


class BTN:
    def searchCMD(id, data, back):
        temp = []
        pos = 1
        x = []

        for i in data:
            cb = f"AnimeS {id} " + get_hash(i["id"], back)
            temp.append([InlineKeyboardButton(text=i["title"], callback_data=cb)])
        pos = len(temp)
        hash = get_hash_btn(None, None)

        if len(temp) > 10:
            b_parts = []
            x = 0
            page = 0

            while pos > 10:
                t = temp[x : x + 10]

                if len(t) == 0:
                    break
                b_parts.append(t)
                x += 10
                pos -= 10

                if page == 0:
                    b_parts[page].append(
                        [
                            InlineKeyboardButton(
                                text="Next  ⫸",
                                callback_data=f"switch_anime {id} {hash} 1",
                            )
                        ]
                    )
                else:
                    b_parts[page].append(
                        [
                            InlineKeyboardButton(
                                text="⫷ Prev",
                                callback_data=f"switch_anime {id} {hash} {page-1}",
                            ),
                            InlineKeyboardButton(
                                text="Next ⫸",
                                callback_data=f"switch_anime {id} {hash} {page+1}",
                            ),
                        ]
                    )

                page += 1
            if pos > 0:
                b_parts.append(temp[x:])
                b_parts[page].append(
                    [
                        InlineKeyboardButton(
                            text="⫷ Prev",
                            callback_data=f"switch_anime {id} {hash} {page-1}",
                        )
                    ]
                )

            hash = get_hash_btn((b_parts, back), hash)
            BTN = b_parts[0]
            return InlineKeyboardMarkup(BTN)
        else:
            return InlineKeyboardMarkup(temp)

    def AnimeS(id, data, back):
        temp = []
        pos = 1
        x = []

        for i in data:
            cb = f"episode {id} " + get_hash(i[1], back)
            if pos % 4 == 0:
                x.append(InlineKeyboardButton(text=i[0], callback_data=cb))
                temp.append(x)
                x = []
            else:
                x.append(InlineKeyboardButton(text=i[0], callback_data=cb))
            pos += 1

        if len(x) != 0:
            temp.append(x)

        hash = get_hash_btn(None, None)

        if len(temp) > 23:
            b_parts = []
            x = 0
            page = 0

            while pos > 23:
                t = temp[x : x + 23]

                if len(t) == 0:
                    break
                b_parts.append(t)
                x += 23
                pos -= 23

                if page == 0:
                    b_parts[page].append(
                        [
                            InlineKeyboardButton(
                                text="Back", callback_data=f"searchBACK {id} {back}"
                            ),
                            InlineKeyboardButton(
                                text="Next  ⫸", callback_data=f"switch_ep {id} {hash} 1"
                            ),
                        ]
                    )
                else:
                    b_parts[page].append(
                        [
                            InlineKeyboardButton(
                                text="⫷ Prev",
                                callback_data=f"switch_ep {id} {hash} {page-1}",
                            ),
                            InlineKeyboardButton(
                                text="Next ⫸",
                                callback_data=f"switch_ep {id} {hash} {page+1}",
                            ),
                        ]
                    )
                b_parts[page].append(
                    [
                        InlineKeyboardButton(
                            text="Back", callback_data=f"searchBACK {id} {back}"
                        )
                    ]
                )
                page += 1
            if pos > 0:
                b_parts.append(temp[x:])
                b_parts[page].append(
                    [
                        InlineKeyboardButton(
                            text="⫷ Prev",
                            callback_data=f"switch_ep {id} {hash} {page-1}",
                        ),
                        InlineKeyboardButton(
                            text="Back", callback_data=f"searchBACK {id} {back}"
                        ),
                    ]
                )

            hash = get_hash_btn((b_parts, back), hash)
            BTN = b_parts[0]
            return InlineKeyboardMarkup(BTN)
        else:
            temp.append(
                [
                    InlineKeyboardButton(
                        text="Back", callback_data=f"searchBACK {id} {back}"
                    )
                ]
            )
            return InlineKeyboardMarkup(temp)

    def episode(id, surl, murl, back, dl_open_cb):
        temp = []
        pos = 1
        x = []
        temp.append(
            [InlineKeyboardButton(text="⬇️ Direct Url ⬇️", callback_data="engSUB")]
        )

        for i in surl:
            if pos % 3 == 0:
                x.append(
                    InlineKeyboardButton(
                        text=i[0], url="https://animedex.pages.dev/embed?url=" + i[1]
                    )
                )
                temp.append(x)
                x = []
            else:
                x.append(
                    InlineKeyboardButton(
                        text=i[0], url="https://animedex.pages.dev/embed?url=" + i[1]
                    )
                )
            pos += 1

        if len(x) != 0:
            temp.append(x)

        x = []
        pos = 1

        if len(murl) != 0:
            temp.append([InlineKeyboardButton(text="➖➖➖➖➖➖➖➖➖➖", callback_data="line")])

            temp.append(
                [InlineKeyboardButton(text="⬇️ Mirror Url ⬇️", callback_data="engDUB")]
            )

            for i in murl:
                if pos % 3 == 0:
                    x.append(InlineKeyboardButton(text=i[0].title(), url=i[1]))
                    temp.append(x)
                    x = []
                else:
                    x.append(InlineKeyboardButton(text=i[0].title(), url=i[1]))
                pos += 1

            if len(x) != 0:
                temp.append(x)
        temp.append(
            [InlineKeyboardButton(text="📥 Download 📥", callback_data=dl_open_cb)]
        )
        temp.append(
            [InlineKeyboardButton(text="Back", callback_data=f"AnimeS {id} {back}")]
        )
        return InlineKeyboardMarkup(temp)

    def download(id, links, back):
        temp = []

        for q, l in links.items():
            q = q.split("x")[1] + "p"
            temp.append([InlineKeyboardButton(text=q, url=l)])

        temp.append([InlineKeyboardButton(text="Back", callback_data=back)])
        return InlineKeyboardMarkup(temp)
