import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'hi!i am bot! {bot.user}!')

@bot.command()
async def repeat(ctx, times: int, content='repeat...'):
    """repeat."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def story(ctx):
    await ctx.send('in a universe,a human kill all underground monster,he reset for many times to kill and kill,but...the reset has begun a alternate timelines,and the human kill over and over,until the human bring together the judges of the 3 universes,the judges of 3 try to stop him,but they always failed,until they use tey recalled knowledge to fight,end')

@bot.command()
async def joke(ctx):
    await ctx.send("Do you know how big a squirrel's teeth are? They're so big that we can land a plane on their teeth")

@bot.command()
async def frick(ctx):
    await ctx.send('your face is like a gorilla')

bot.run("")
