from pyrogram.types import Message, CallbackQuery


def CMDErrorHandler(func):
    async def new_func(_, message: Message):
        try:
            return await func(_, message)
        except Exception as e:
            print(e)
            try:
                await message.reply_message(
                    "Something went wrong.\n\nReport @TechZBots_Support"
                )
            except:
                pass
            return

    return new_func


def CBErrorHandler(func):
    async def new_func(_, query: CallbackQuery):
        try:
            return await func(_, query)
        except Exception as e:
            print(e)
            try:
                await query.message.edit(
                    "Something went wrong.\n\nReport @TechZBots_Support"
                )
            except:
                pass
            return

    return new_func
