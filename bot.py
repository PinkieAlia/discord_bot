import os
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

# 當機器人完成啟動時
@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    dc_status = discord.Status.online
    dc_activity = discord.Activity(type=discord.ActivityType.playing,name="具反斗城")
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）
    await bot.change_presence(status=dc_status , activity=dc_activity)

# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), "cogs")):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start('DISCORD_TOKEN')

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())

#https://discord.com/oauth2/authorize?client_id=963178073853947904&permissions=2147483647&scope=bot%20applications.commands
