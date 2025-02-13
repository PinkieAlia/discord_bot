# bot.py

import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


# 當機器人完成啟動時
@bot.event
async def on_ready():
    await bot.tree.sync()  # 確保指令同步
    print(f"目前登入身份 --> {bot.user}")
    dc_status = discord.Status.online
    dc_activity = discord.Activity(type=discord.ActivityType.playing,
                                   name="具反斗城")
    await bot.change_presence(status=dc_status, activity=dc_activity)


# 載入所有擴充套件（包括 slash.py）
async def load_extensions():
    for filename in os.listdir(os.path.join(os.path.dirname(__file__),
                                            "cogs")):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


# 設定啟動鉤子
async def setup_hook():
    await load_extensions()


bot.setup_hook = setup_hook

# 啟動機器人
if __name__ == "__main__":
    bot.run(TOKEN)  # 使用環境變數中的 TOKEN
