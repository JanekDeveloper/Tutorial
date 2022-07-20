import discord

from discord.ext import commands, tasks

import asyncio

import aiohttp

import json

import random

intent = discord.Intents.all()

client = commands.Bot(command_prefix="ТВОЙ ПРЕФИКС", intents = intent)
client.remove_command('help')
token = ('ТВОЙ ТОКЕН')



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

client.run(token)
