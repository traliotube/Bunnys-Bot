import discord
import random
import requests
from discord.ext import commands
from bs4 import BeautifulSoup

bot = commands.Bot(
    command_prefix="$",
    case_insensitive=True
)


bot.remove_command('help')


@bot.event
async def on_ready():
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID : {}'.format(bot.user.id))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"I am in {len(client.guilds)} servers!"))


@bot.command()
async def ping(ctx):
    await ctx.send(f'Hello! I am there and my latency is {round(bot.latency*1000)}ms ')


@bot.command(name='Bulk delete Messages', help='Bulk delete messages by specifying number of messages to delete')
async def clear(ctx, ammount=4):
    await ctx.channel.purge(limit=ammount)


@bot.command(name='Math Calcualtor', help='Use math n1 operation n2, for using the math calculator.', aliases=['math', 'calc'])
async def math(ctx, ni, oper, ns):
    if oper == '+':
        await ctx.send(int(ni)+int(ns))
    if oper == '-':
        await ctx.send(int(ni)-int(ns))
    if oper == '*':
        await ctx.send(int(ni)*int(ns))
    if oper == '/':
        await ctx.send(int(ni)/int(ns))


@bot.command(name='discord.py Help', aliases=['pyhelp', 'helppy', 'py'], help='All the help websites for python discord.py')
async def py(ctx):
    embed = discord.Embed(
        title="Useful Links", description="The useful links for bunny to use while coding", color=0x0b7fe5)
    embed.set_author(name=ctx.author.name,
                     url="https://dsc.gg/botstopia", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Discord embed generator",
                    value="https://cog-creators.github.io/discord-embed-sandbox/", inline=False)
    embed.add_field(name="Coding help",
                    value="https://discord.com/channels/654884606750752778/654884606750752781", inline=False)
    embed.add_field(name="Heroku hosting",
                    value="https://dashboard.heroku.com/apps/bunnysbot/", inline=False)
    embed.add_field(name="Heroku Logs",
                    value="https://dashboard.heroku.com/apps/bunnysbot/logs", inline=False)
    embed.set_footer(text="All the coding help Bunny needs")
    await ctx.send(embed=embed)


@bot.command(aliases=['len', 'length'], name='Length of word char', help='Use this command to get the length of char in a word')
async def _len(ctx, text='example'):
    await ctx.send(f'The length of {text} is {len(text)}')


@bot.command(name='Roll Dice', aliases=['diceroll', 'dice'], help='Roll your own dice and get the number you get on your dice')
async def dice(ctx):
    dice_no = random.randint(1, 6)
    await ctx.send(f'You have got {dice_no} in the dice!!!')


@bot.command(name='Random Numbers', aliases=['random', 'rand'], help='Use rand n1 n2 and number of random numbers')
async def rand(ctx, ni, ns):
    await ctx.send(f"The random number is {random.randint(ni, ns)}")


@bot.command()
async def price(ctx, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    output = soup.find(id="priceblock_ourprice").get_text()
    await ctx.send(output.strip())


@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def help(ctx):

    embed = discord.Embed(title="Bunny's Bot help", url="https://dsc.gg/bunnysbot",
                          description="The help page of Bunny's Bot", color=0x07a8ed)
    embed.set_author(name=ctx.author.name,
                     url="https://dsc.gg/botstopia", icon_url=ctx.author.avatar_url)
    embed.add_field(
        name="calc", value="Calculate the +,-,*,/ of 2 numbers _Ex. $calc 10 + 20_", inline=False)
    embed.add_field(
        name="ping", value="Check if the bot is alive _Ex. $ping_", inline=False)
    embed.add_field(
        name="clear", value="Bulk delete msgs by specifiying the number of msgs _Ex. $clear 6_", inline=False)
    embed.add_field(
        name="len", value="Use this command to get the length of char in a word *Ex. $len test*", inline=False)
    embed.add_field(
        name="rand", value="Use rand n1 n2 and number of random numbers *Ex. $rand 10 20*", inline=False)
    embed.add_field(
        name="price", value="Get the price of a amazon product _Ex. $price (amazon url)_", inline=False)
    embed.add_field(name="help", value="Shows this Message ", inline=False)
    embed.add_field(
        name="invite", value="Shows the invite link of this bot", inline=False)
    embed.add_field(
        name="py", value="Shows all the coding help links bunny needs", inline=False)
    embed.add_field(
        name="danktrade", value="Check the amount of kn an zz while trading", inline=False)
    embed.set_footer(text="A general purpose bot made by Bunny Pranav")
    await ctx.send(embed=embed)


@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Bunny's Bot Invite",
                          description="The invite link of this bot", color=0x057ae1)
    embed.set_author(name=ctx.author.name,
                     url="https://dsc.gg/botstopia", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Invite link",
                    value="https://dsc.gg/bunnysbot", inline=False)
    embed.add_field(name="Support Server",
                    value="https://dsc.gg/botstopia", inline=False)
    embed.set_footer(
        text="It will help me a lot if you could invite this bot to your server")
    await ctx.send(embed=embed)


@bot.command(alias=['dankmoni', 'dankt', 'dt', 'knzz'])
async def danktrade(ctx, zz: int, kn: int):
    kn_moni = kn*200000
    zz_moni = zz*100000
    total_moni = kn_moni+zz_moni
    embed = discord.Embed(title="Dank Memer KN and ZZ money Calculator",
                          description="a money calculator for Dank Memer KN and ZZ", color=0x05acff)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/emojis/780515353704398869.png")
    embed.set_author(name=ctx.author.name,
                     url="https://dsc.gg/botstopia", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Amount for KN", value=kn_moni, inline=False)
    embed.add_field(name="Amount for ZZ", value=zz_moni, inline=False)
    embed.add_field(name="Total Amount", value=total_moni, inline=False)
    embed.set_footer(text="The best moni calculator for dank memer kn and zz")
    await ctx.send(embed=embed)

bot.run('Nzk4MTk4MzYxMDY0NjAzNzEx.X_xiJw.VprDLErH56HFgtbSumFHWy1jHIs')
