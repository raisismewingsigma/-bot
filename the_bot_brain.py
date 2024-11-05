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
    await ctx.send('once upon ago,in the jungle of amazon,live a titan anacondas,and the monster,but,suddenly,after the final quake of mesozoikum,the titan anacondas turns into a ancondas,end')

@bot.command()
async def joke(ctx):
    await ctx.send("Do you know how big a squirrel's teeth are? They're so big that we can land a plane on their teeth")

@bot.command()
async def frick(ctx):
    await ctx.send('your face is like a gorilla')

@bot.command()
async def trashedu(ctx):
    await ctx.send(f'Trash is a material/item that is not used, most of the trash is dangerous for the environment such as anorganic and B3 trash, but there is also useful trash such as organic trash')

@bot.command()
async def trash2r(ctx):
    await ctx.send(f'Trash can be recycled and reused, reuse is using trash again but not changing the shape of the trash, such as glass cups that become flower vases, recycling is reusing trash by changing its shape, such as dirt can become biogas')


bot.run("")
