import discord

from discord.ext import commands, tasks

import asyncio

import aiohttp

import json

import random

import DiscordUtils

import datetime

import time

intent = discord.Intents.all()
client = commands.Bot(command_prefix="t!", intents = intent)
client.remove_command('help')
token = ('ТВОЙ ТОКЕН')
invtrck = DiscordUtils.InviteTracker(client)


class LOGINFO :
	CHANNELID = 996746254866456599
	GUILDID = 996746254866456596



@client.event
async def on_member_join(member):

	inver = await invtrck.fetch_inviter(member)
	chann = client.get_channel(LOGINFO.CHANNELID)
	guild = client.get_guild(LOGINFO.GUILDID)
	total = 0

	for i in await guild.invites():
		if i.inviter == inver :
			total += i.uses

			embed = discord.Embed(
				title = 'Инвайт Логгер',
				description = f'{member.mention} зашёл на сервер!\n\n Пригласил его {inver.mention}\n Всего приглашений ``total``',
				colour = 0x00FF99
				)

			embed.timestamp = datetime.datetime.utcnow()
			embed.set_footer(text = 'Инвайт Логгер |', icon_url = f"{member.avatar_url}")
			embed.set_thumbnail(url = f'{inver.avatar_url}')

			await chann.send(embed=embed)



@client.command()
async def invites(ctx, member: discord.Member = None):
	if member == None:
		user = ctx.author
	else:
		user = member

	guild = ctx.guild
	total_invites = 0

	for i in await guild.invites():
		if i.inviter == user :
			total_invites += i.uses



	embed = discord.Embed(
		title = 'Инвайт Логгер',
		description = f"\nПользователь : {user.mention}\n\nОбщее количество приглашённых пользователей: ``{total_invites}``",
		colour = 0x00FF91
		)
	embed.add_field(name="Присоединился в:",value=user.joined_at,inline=False)
	embed.add_field(name="Присоединился в:",value=user.joined_at,inline=False)
	embed._timestamp = datetime.datetime.utcnow()

	async with ctx.typing():
		await asyncio.sleep(2)


	await ctx.send(embed=embed)


@client.event
async def on_ready():
	print("Бот запущен!")


@client.command()
async def привет(ctx):
	await ctx.reply(f"Привет, {ctx.author.mention}")


@client.command()
async def meme(ctx):
	embed = discord.Embed(title = "", description = "")

	async with aiohttp.ClientSession() as cs:
		async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r :
			res = await r.json()

			embed.set_image(url = res['data']['children'] [random.randint(0, 25)]['data']['url'])
			await ctx.reply(embed=embed)


@client.command()
async def cat(ctx):
	async with aiohttp.ClientSession() as ses:
		async with ses.get('https://some-random-api.ml/animal/cat') as r:
			if r.status in range(200, 299):
				data = await r.json()
				image = data["image"]
				await ctx.reply(image)
				ses.close()
			else:
				await ctx.send("Ошибка, попробуйте ещё раз.")
				ses.close()

@client.command()
async def ball(ctx, *, vopros):
	otvet1 = discord.Embed(title='', description="Да", color=discord.Color.blue())
	otvet2 = discord.Embed(title='', description="Нет", color=discord.Color.blue())
	otvet3 = discord.Embed(title='', description="Возможно", color=discord.Color.blue())
	otvet4 = discord.Embed(title='', description="Конечно что.... нет", color=discord.Color.blue())
	otvet5 = discord.Embed(title='', description="Даже не думай об этом!", color=discord.Color.blue())
	otvet6 = discord.Embed(title='', description="Спроси ещё раз", color=discord.Color.blue())
	otvet7 = discord.Embed(title='', description="Я не могу ответить на этот вопрос", color=discord.Color.blue())
	otvet8 = discord.Embed(title='', description="Не знаю", color=discord.Color.blue())
	embed=random.choice([otvet1, otvet2, otvet3, otvet4, otvet5, otvet6, otvet7, otvet8])
	await ctx.reply(embed=embed)







client.run(token)
