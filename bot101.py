import discord
import json
import aiohttp
import asyncio
import os

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
user_token = os.getenv("DISCORD_USER_TOKEN")
channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Print the values (for debugging purposes)
print(f"User Token: {user_token}")
print(f"Channel ID: {channel_id}")
print(f"Telegram Bot Token: {telegram_bot_token}")
print(f"Telegram Chat ID: {telegram_chat_id}")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message: discord.Message):
        # Exclude messages that mention @here or @everyone or are from bots
        if (
            not message.author.bot
            and "@here" not in message.content
            and "@everyone" not in message.content
            and message.channel.id != 1272654641515069621
        ):

            # Check if message contains any of the keywords
            if any(keyword.lower() in message.content.lower() for keyword in keywords):
                await self.send_notif(message)

    async def send_notif(self, message: discord.Message):
        # Format the notification message to include message content, user display name, channel name, and server name
        notification = f"# 🦊{message.content}🦊\n> ```{message.author.display_name}\n> {message.channel.name}\n> {message.guild.name}``` "

        # Send notification to the specified Discord channel
        discord_channel = self.get_channel(channel_id)
        if discord_channel:
            await discord_channel.send(notification)

        # Send notification to the specified Telegram chat
        await self.send_to_telegram(notification)

    async def send_to_telegram(self, message: str):
        telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
        payload = {
            "chat_id": telegram_chat_id,
            "text": message,
            "parse_mode": "Markdown",  # To support Markdown formatting
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(telegram_url, data=payload) as response:
                if response.status != 200:
                    print(
                        f"Failed to send message to Telegram. Status code: {response.status}, Response: {await response.text()}"
                    )


# # Load configuration from file
# with open("config.json") as f:
#     d = json.load(f)

# Define the list of keywords and phrases
keywords = [
    "phrase",
    "stak",
    "wallet",
    "cant",
    "can't",
    "eth",
    "unstake",
    "delegat",
    "undelegate",
    "error",
    "revert",
    "fail",
    "claim",
    "meta",
    "help me",
    "help",
    "where",
    "0x",
    "execution",
    "fix",
    "bug",
    "issue",
    "unable",
    "status",
    "load",
    "not",
    "migrat",
    "rpc",
    "can i",
    "can we",
    "kyc",
    "register",
    "days",
    "hours",
    "when",
    "why",
    "what",
    "who",
    "stop",
    "work",
    "broken",
    "lp",
    "reward",
    "point",
    "txn",
    "eligib",
    "network",
    "convert",
    "any",
    "key",
    "problem",
    "pool",
    "liquid",
    "add",
    "my",
    "new",
    "want",
    "how",
    "valid",
    "invalid",
    "node",
    "support",
    "withdraw",
    "token",
    "allocat",
    "quest",
    "farm",
    "unable",
    "ledger",
    "keplr",
    "stuck",
    "approv",
    "happen",
    "lock",
    "unlock",
    "exchange",
    "link",
    "mainnet",
    "testnet",
    "mine",
    "mismatch",
    "opcode",
    "reason",
    "limit",
    "broadcast",
    "rate",
    "pars",
    "timeout",
    "block",
    "exceed",
    "congest",
    "authoriz",
    "server",
    "internal",
    "unknown",
    "expire",
    "sync",
    "parameter",
    "resource",
    "fee",
    "estimat",
    "contract",
    "deploy",
    "execution",
    "decrypt",
    "access",
    "transact",
    "insufficient",
    "permission",
    "required",
    "initializ",
    "import",
    "export",
    "generat",
    "hardware ",
    "outdate",
    "storage",
    "corrupt",
    "unsupported",
    "version",
    "balance",
    "sale",
    "private",
    "whitelist",
    "allocat",
    "crowdsale",
    "subscription",
    "round",
    "invest",
    "offering",
    "period",
    "vest",
    "minimum",
    "maximum",
    "partiicpat",
    "contribut",
    "fund",
    "reserve",
    "fcfs",
    "join",
    "app",
    "submi",
    "deposit",
    "profit",
    "transfer",
    "distribut",
    "ROI",
    "yield",
    "swap",
    "validat",
    "APY",
    "earn",
    "bond",
    "harvest",
    "apr",
    "compound",
    "vault",
    "credit",
    "coin",
    "hash",
    "simulation" "?",
    # Add more keywords and phrases as needed
]

# Create the client and run the bot
client = MyClient()
client.run(user_token)
