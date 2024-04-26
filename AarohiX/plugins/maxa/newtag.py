from pyrogram import Client, filters
import random
from config import API_ID, API_HASH
# Your session file path
session_file_path = 'BQG_NJ0AJTqTf8Md8F9U-y5GLXnGfa8N1QEks4FBIQvJA5GR3UqCevNKvbHKRiXhGkwsnsqsS5YlMgTfPkTEEULHKC_9phxxX16I8OqYIwWLDbKgyLWr35d9BbFaG6zBK95WLq976ukmaxHmFVPr-WcU7lr1t69VJkE5AWVHZ7QnpPivCiNCPKlgx2Zd2dGcKpPKvoU2LjybZArTjUxoyI6axjgbNRdQ95LSx8aHWJpVZFNqPMB2PpI_MgaAkxh9o0nMojBu2LpyPfrn78i-MLz3E54MWCfngn_VHrdtUTPPhroDmaUI_hqjENXJJdG_kuG4KQ0FMZ5TuQifUAwWAODCYbeatQAAAAGF6z4UAA'

# List of random messages
messages = [
    "Good morning @{}! Have a great day ahead.",
    "Hey @{}, rise and shine! It's morning time.",
    "Good day @{}! Hope you have a wonderful morning."
]

# Initialize Pyrogram client
app = Client("my_session", api_id=API_ID, api_hash=API_HASH, session_string=session_file_path)

# Command to trigger the sending of random morning messages
@app.on_message(filters.command("morning", prefixes="/"))
def send_morning_messages(client, message):
    chat = cclient.get_chat('target_group_username')
    participants = client.get_chat_members(chat.chat_id)

    for member in participants:
        if member.user.username:
            random_message = random.choice(messages).format(member.user.username)
            client.send_message(chat.id, random_message)
