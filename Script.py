class script(object):
    START_TXT = """Hᴇʟʟᴏ {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝐈 𝐜𝐚𝐧 𝐩𝐫𝐨𝐯𝐢𝐝𝐞 𝐀𝐥𝐥 𝐍𝐞𝐰 𝐌𝐨𝐯𝐢𝐞𝐬🤩, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT =  """➪ 𝑴𝒚 𝒏𝒂𝒎𝒆 : {} 
➪ 𝑪𝒓𝒆𝒂𝒕𝒐𝒓 : <a href="https://t.me/bots_supported">ʜᴇʀᴇ</a>
➪ 𝑫𝒆𝒗𝒐𝒍𝒐𝒑𝒆𝒓 : <a href="https://t.me/AFxSU">ɛӼ_ռöֆ</a>
➪ 𝑳𝒊𝒃𝒓𝒂𝒓𝒚 : <a href='https://docs.pyrogram.org/'>𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎</a>
➪ 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆 : <a href='https://docs.pyrogram.org/'>𝑷𝒚𝒕𝒉𝒐𝒏 3</a>
➪ 𝑫𝒂𝒕𝒂 𝒃𝒂𝒔𝒆 : <a href='https://www.mongodb.com/'>𝑴𝒐𝒏𝒈𝒐𝑫𝑩</a>
➪ 𝑩𝒐𝒕 𝒔𝒆𝒓𝒗𝒆𝒓 : <a href="https://t.me/quickfastt">𝑸𝒖𝒊𝒄𝒌𝑭𝒂𝒔𝒕</a>
➪ 𝑩𝒖𝒊𝒍𝒅 𝑺𝒕𝒂𝒕𝒖𝒔 : v2.0.3 [ 𝑺𝒕𝒂𝒃𝒍𝒆 ]</b>""" 
    ADMINS_TXT = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : 🍒ɛӼ_ռöֆ__⁷⁷⁷✘⁴✨
• ᴜꜱᴇʀɴᴀᴍᴇ : @AFxSU
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/AFxSU'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""
 
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and LUCIFER will respond whenever a keyword is found the message

<b>NOTE:</b>
1. LUCIFER should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- LUCIFER Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. LUCIFER supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/bots_supported)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /donate - <code>to donate any gifts for my owner</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    DONATE_TXT = """<Hey {}
[Here is the Donation Link](https://t.me/at3movies) ❤"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
