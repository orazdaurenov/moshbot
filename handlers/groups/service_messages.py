from aiogram import types
from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(msg: types.Message):
    members = ", ".join([m.get_mention(as_html=True)
                        for m in msg.new_chat_members])
    await msg.reply(f"Benvenuto, {members}.")


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(msg: types.Message):
    if msg.left_chat_member.id == msg.from_user.id:
        await msg.answer(f"{msg.left_chat_member.get_mention(as_html=True)} ha lasciato il gruppo")
    elif msg.from_user.id == (await bot.me).id:
        return
    else:
        await msg.answer(f"{msg.left_chat_member.full_name} e stato buttato fuori \n"
                         f"Admin: {msg.from_user.get_mention(as_html=True)}.")
