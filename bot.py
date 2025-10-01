import discord
from discord.ext import commands
from discord import PartialEmoji
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler


TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# ----- Intents -----
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ----- Dummy HTTP Server for Render -----
PORT = int(os.getenv("PORT", 8080))  # Render provides this environment variable


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")


def run_server():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()


threading.Thread(target=run_server, daemon=True).start()


# ----- Welcome Buttons -----
class WelcomeButtons(discord.ui.View):
    def __init__(self):
        super().__init__()
        youtube_emoji = PartialEmoji(name="youtube", id=1326491073811578890)
        self.add_item(
            discord.ui.Button(
                label="Telegram Channel",
                emoji=youtube_emoji,
                style=discord.ButtonStyle.link,
                url="https://t.me/+FELusRYsQLcyOGJl",
            )
        )

        tiktok_emoji = PartialEmoji(name="tiktok", id=1162772344973049876)
        self.add_item(
            discord.ui.Button(
                label="Follow on TikTok",
                emoji=tiktok_emoji,
                style=discord.ButtonStyle.link,
                url="https://www.tiktok.com/@twa_akash_06",
            )
        )


# ----- Bot Events -----
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_member_join(member):
    guild = member.guild
    member_count = guild.member_count

    embed = discord.Embed(
        title="Trading With AKASH",
        description=(
            f"WELCOME {member.mention}.\n\n"
            f"WELCOME TO OUR Trading With AKASH\n\n"
            f"THANK'S FOR JOINING WITH US"
        ),
        color=discord.Color.red(),
    )
    embed.set_author(
        name="𝐈'𝐌 𝐀𝐊𝐀𝐒𝐇 !!",
        icon_url="https://cdn.discordapp.com/avatars/286927341211615232/ce8b04fee60a308c44550d730df6e654.webp?size=128",
        url="https://t.me/+FELusRYsQLcyOGJl",
    )
    embed.set_thumbnail(url=member.display_avatar.url)

    # Channel mentions using actual IDs
    embed.add_field(
        name="CHECK OUR ANNOUNCEMENT",
        value=f"Check (⁠📣│<#{1405954193797419162}>)",
        inline=False,
    )
    embed.add_field(
        name="CHECK OUR RULES",
        value=f"Check (⁠📜│<#{1406360993616887999}>)",
        inline=False,
    )
    embed.add_field(
        name="GO TO MAIN CHAT",
        value=f"Check (⁠💬│<#{1405954202957512775}>)",
        inline=False,
    )

    embed.add_field(name="Members", value=f"{member_count} - CLOSERGB.", inline=False)

    # GIF
    embed.set_image(
        url="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2toMmJ6ampmbTFkcGl6aWdvam1pdGQ2cDlkbWdleWgwbWtsdjdsdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZCt9ZFqzGvNadpKNyE/giphy.gif"
    )
    embed.set_footer(
        icon_url="https://i.ibb.co.com/BK7Q0f5B/unnamed.jpg",
        text="Made With Love BY - Mac GunJon",
    )

    # Send embed + buttons
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(embed=embed, view=WelcomeButtons())


# ----- Run Bot -----
bot.run(TOKEN)
