from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError


@register(outgoing=True, pattern=r"^\.sa(?: |$)(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```𝐌𝐨𝐡𝐨𝐧 𝐛𝐚𝐥𝐚𝐬 𝐩𝐞𝐬𝐚𝐧 𝐤𝐞 𝐚𝐧𝐚𝐤 𝐚𝐧𝐣𝐢𝐧𝐠!```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("```𝐁𝐚𝐥𝐚𝐬 𝐩𝐞𝐬𝐚𝐧 𝐤𝐞 𝐚𝐧𝐚𝐤 𝐚𝐧𝐣𝐢𝐧𝐠 𝐬𝐞𝐛𝐚𝐠𝐚𝐢 𝐭𝐚𝐫𝐠𝐞𝐭.```")
        return
    await steal.edit("```𝘈𝘨𝘪𝘭 𝘴𝘦𝘥𝘢𝘯𝘨 𝘮𝘦𝘯𝘨𝘢𝘮𝘣𝘪𝘭 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘴𝘪 𝘢𝘯𝘥𝘢 𝘴𝘶𝘳𝘶𝘩 𝘴𝘶𝘳𝘶𝘩 𝘴𝘪𝘢𝘱𝘢 𝘧𝘢𝘬𝘦 𝘢𝘤𝘤𝘰𝘶𝘯𝘵! 𝘭𝘪𝘩𝘢𝘵 𝘴𝘢𝘫𝘢 𝘥𝘢𝘯 𝘵𝘶𝘯𝘨𝘨𝘶...
```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Mohon Unblock @sangmatainfo_bot Dan Coba Lagi```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit("```𝐓𝐞𝐫𝐧𝐲𝐚𝐭𝐚 𝐚𝐧𝐚𝐤 𝐛𝐚𝐛𝐢 𝐢𝐧𝐢 𝐛𝐞𝐥𝐮𝐦 𝐠𝐚𝐧𝐭𝐢 𝐧𝐚𝐦𝐚 𝐝𝐚𝐫𝐢 𝐚𝐰𝐚𝐥 𝐦𝐚𝐢𝐧 𝐭𝐞𝐥𝐞(```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`𝘈𝘨𝘪𝘭 𝘴𝘦𝘥𝘢𝘯𝘨 𝘯𝘨𝘦𝘭𝘢𝘨, 𝘮𝘰𝘩𝘰𝘯 𝘮𝘢𝘢𝘧!!!`")


CMD_HELP.update({
    "sangmata":
        "`.sa`\
          \nUsage: Mendapatkan Riwayat Nama Pengguna."
})
