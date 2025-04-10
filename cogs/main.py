import discord
from discord.ext import commands
import requests 
import random

#串連GoogleAppsScript
#!吃什麼資料庫
eat_ar = requests.get("https://script.google.com/macros/s/AKfycbyvbzQXF7eHmX4mMfaEsgWgSiZvt8mR83sgP7v8aR3LLIKSErO1ZXVOd4wmM4G7RqM/exec")
#簡易指令資料庫
direct = requests.get("https://script.google.com/macros/s/AKfycbzMlHpRKcOb90YHoTZ-GNuNvh0ldP6TKgtN6SYmPfzHLH448_h2P6hkD86k7zsoRKC3/exec")

# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        if message.author == self.bot.user:
            return
            
        #抽卡 深海古語
        if message.content.startswith("!抽卡"):
            msg_card = ""
            card_all = [0]*10      
            atk = False
            haveR = False  #保底判斷      
            miss77 = False  #好想77
            haveMP = False  #判斷有無M、P      
            if message.content.find("好想77") != -1:
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
            await message.reply(msg_card)
    
        #通靈 外神秘法
        if message.content.startswith("!通靈"):
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
            if haveMP == True:
                card_all[9] += " <a:ki35:1104439965292703836>"        
            for i in range(0,10):
                msg_card += card_all[i] + " "      
            if atk == True:
                msg_card = "抽爽沒 <:ki41:1222381618954764358>"
            await message.reply(msg_card)

        #更新抽吃什麼、簡易指令的資料庫
        if message.content.startswith("!更新"):
            eat_ar = requests.get("https://script.google.com/macros/s/AKfycbyvbzQXF7eHmX4mMfaEsgWgSiZvt8mR83sgP7v8aR3LLIKSErO1ZXVOd4wmM4G7RqM/exec")
            direct = requests.get("https://script.google.com/macros/s/AKfycbzMlHpRKcOb90YHoTZ-GNuNvh0ldP6TKgtN6SYmPfzHLH448_h2P6hkD86k7zsoRKC3/exec")
            await message.channel.send("資料已更新")

        if message.content.startswith("!操"):
            await message.channel.send("<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>\n<:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>.")
            await message.channel.send("<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>.")
            await message.channel.send("<:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:ki41:1222381618954764358>.")
            await message.channel.send("<:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:ki41:1222381618954764358><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358>\n<:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358><:nothing:1225083828826148884><:nothing:1225083828826148884><:nothing:1225083828826148884><:ki41:1222381618954764358>.")

        #測試功能
        if message.content.startswith("!kiki"):
            msg = await message.channel.send("<:KI31:1075977250287144982><:KI32:1077862545437765706>")
            await asyncio.sleep(1)
            await msg.delete()
            msg = await message.channel.send("<:KI31:1075977250287144982><:KI33:1078228894433427506><:KI32:1077862545437765706>")
            await asyncio.sleep(1)
            await msg.delete()
            await message.channel.send("<:KI31:1075977250287144982><:KI32:1077862545437765706>")
        
        #指令表 之後想用更好的呈現方式
        if message.content == "!指令":
            dir_list = "操\n!抽卡\n!通靈\n!更新"
            await message.channel.send(dir_list)

        #回覆貼圖
        if message.content == "<:E_L_lookfromleft:844916158628233236>" and message.author.id != 963178073853947904:
            await message.channel.send("<:E_L_lookfromright:844916132649762837>")
        if message.content == "<:E_L_lookfromright:844916132649762837>" and message.author.id != 963178073853947904:
            await message.channel.send("<:E_L_lookfromleft:844916158628233236>")
        if message.content == "<:E_L_lul:823139120792469504>" and message.author.id != 963178073853947904:
            await message.channel.send("<:E_L_lul:823139120792469504>")
        if message.content == "<:NE_angryshark:1034081028974841957>" and message.author.id != 963178073853947904:
            await message.channel.send("<:NE_angryshark:1034081028974841957>")        
        if message.content == "<:shuiyang_YA:1130502957583040582>" and message.author.id != 963178073853947904:
            await message.channel.send("<:shuiyang_YA:1130502957583040582>")          

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))
