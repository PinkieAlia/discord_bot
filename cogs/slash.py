import discord 
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
import requests
import random

#串連GoogleAppsScript
#!吃什麼資料庫
eat_ar = requests.get("https://script.google.com/macros/s/AKfycbyvbzQXF7eHmX4mMfaEsgWgSiZvt8mR83sgP7v8aR3LLIKSErO1ZXVOd4wmM4G7RqM/exec")
#簡易指令資料庫
direct = requests.get("https://script.google.com/macros/s/AKfycbzMlHpRKcOb90YHoTZ-GNuNvh0ldP6TKgtN6SYmPfzHLH448_h2P6hkD86k7zsoRKC3/exec")

class Slash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #機器人二選一
    # @app_commands.describe(參數名稱 = 參數敘述)
    # name指令名稱，description指令敘述
    # 參數: 資料型態，可以限制使用者輸入的內容
    @discord.app_commands.command(name = "二選一", description = "機器人幫你選")
    @discord.app_commands.describe(opt_1 = "請輸入選項A", opt_2 = "請輸入選項B")
    async def choose(self, interaction: discord.Interaction, opt_1: str, opt_2: str):
        rd = random.randint(1,10)
        out_opt = ""
        if rd > 5:
          out_opt = opt_1
        else:
          out_opt = opt_2
        embed=discord.Embed(
          title = f"機器人的選擇是... \"{out_opt}\" ！",
          description = f":arrow_right: \"{opt_1}\" v.s \"{opt_2}\"",
          color = 0xF096A9
        )
        await interaction.response.send_message(embed = embed)

    #吃什麼
    @discord.app_commands.command(name="吃什麼",description="機器人幫你選吃什麼")
    async def eatwhat(self, interaction: discord.Integration):
      eat_array = eat_ar.json()
      eat_rd = random.randint(0,len(eat_array)-1)
      embed=discord.Embed(
          description=f"機器人覺得...你可以吃... **{eat_array[eat_rd]}** ！",
          color = 0xF096A9
        )
      await interaction.response.send_message(embed = embed)

    #抽卡 深海古語
    @discord.app_commands.command(name="抽卡", description="CaCo377的十連抽卡")
    @discord.app_commands.describe(add="額外補充")
    async def caco377(self, interaction: discord.Interaction, add: str=""):
      msg_card = ""
      card_all = [0]*10      
      atk = False
      haveR = False  #保底判斷      
      miss77 = False  #好想77
      haveMP = False  #判斷有無M、P      
      if "好想77" in add:
        miss77 = True
      for i in range(10):
        dlc = random.randint(1,10000)  
        if dlc > 9950:
          card_all[i-1] = "<a:77_card_P:1115631665591615519>"
          haveR = True
          haveMP = True
        elif dlc > 9700:
          card_all[i-1] = "<a:77_card_M:1115626802312912948>"
          haveR = True
          haveMP = True
        elif dlc > 8700:
          card_all[i-1] = "<:77_card_R:1115543888187371530>"
          haveR= True
        elif dlc > 8695: #抽爽沒
          atk = True
          card_all[i-1] = ""
        elif dlc > 5000:
          card_all[i-1] = "<:77_card_U:1115626807241220158>"
        else:
          card_all[i-1] = "<:77_card_C:1115626797577539604>"
      if haveR == False:
        card_all[9] = "<:77_card_R:1115543888187371530> <:card_G:1115540749329641562>"
      if miss77==True and haveMP==False:
        card_all[9] = "<a:77_card_M:1115626802312912948> <a:__:1110916757037781033>"
      if miss77==False and haveMP==True:
        card_all[9] += " <a:__:1110916757037781033>"
      for i in range(0,10):
        msg_card += card_all[i] + " "
      if atk == True:
        msg_card = "抽爽沒 <:ki41:1222381618954764358>"
      if add=="":
        await interaction.response.send_message(msg_card)
      else:
        await interaction.response.send_message(add)
        await interaction.followup.send(msg_card)

    #通靈 外神秘法
    @discord.app_commands.command(name="通靈", description="外星ki的十連抽卡")
    @discord.app_commands.describe(add="額外補充")
    async def kiki(self, interaction: discord.Interaction, add: str=""):
      msg_card = ""
      card_all = [0]*10      
      atk = False
      haveR = False  #保底判斷
      haveMP = False #判斷有無M、P
      for i in range(10):
        dlc = random.randint(1,10000)  
        if dlc > 9950:
          card_all[i-1] = "<a:kiki_card_P:1115634385526472764>"
          haveR = True
          haveMP = True
        elif dlc > 9700:
          card_all[i-1] = "<:kiki_card_M:1115626880591208488>"
          haveR = True
          haveMP = True
        elif dlc > 8700:
          card_all[i-1] = "<:kiki_card_R:993174633777995886>"
          haveR= True
        elif dlc > 8695: #抽爽沒
          atk = True
          card_all[i-1] = ""
        elif dlc > 5000:
          card_all[i-1] = "<:kiki_U:1116423377251483721>"
        else:
          card_all[i-1] = "<:kiki_C:1116423374860722287>"
      if haveR == False:
        card_all[9] = "<:kiki_card_R:993174633777995886> <:card_D1:1034025672445792276>"
      if haveMP==True:
        card_all[9] += " <a:ki35:1104439965292703836>"        
      for i in range(0,10):
        msg_card += card_all[i] + " "      
      if atk == True:
        msg_card = "抽爽沒 <:ki41:1222381618954764358>"
      if add=="":
        await interaction.response.send_message(msg_card)
      else:
        await interaction.response.send_message(add)
        await interaction.followup.send(msg_card)
      
    #操 還沒開發好
    #@discord.app_commands.command(name="操",description="就是操")
    #async def hl(self, interaction: discord.Interaction):
    #  channel = self.bot.get_channel(channel_id)
    #  await interaction.response.send_message("<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>\n<:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>.")
    #  await channel.send("<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>.")
    #  await channel.send("<:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>.")
    #  await channel.send("<:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358>.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Slash(bot))

#即時查看 Embed 的版面配置
#https://cog-creators.github.io/discord-embed-sandbox/