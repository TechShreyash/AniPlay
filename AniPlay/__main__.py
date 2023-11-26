import importlib
import asyncio
from AniPlay import app
from pyrogram import idle
from AniPlay.plugins import ALL_MODULES

loop = asyncio.get_event_loop()


async def init():
    for module in ALL_MODULES:
        importlib.import_module("AniPlay.plugins." + module)
    print("[INFO]: Imported Modules Successfully")

    await app.start()
    print("[INFO]: Bot Started")
    await idle()
    print("[INFO]: BOT STOPPED")
    await app.stop()
    for task in asyncio.all_tasks():
        task.cancel()


if __name__ == "__main__":
    loop.run_until_complete(init())
