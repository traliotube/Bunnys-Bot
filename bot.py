import discord
import random
import requests
import re
import os
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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"to your commands with prefix '$'"))


@bot.command()
async def ping(ctx):
    await ctx.send(f'Hello! I am there and my latency is {round(bot.latency*1000)}ms ')


@bot.command(name='Bulk delete Messages', help='Bulk delete messages by specifying number of messages to delete')
async def clear(ctx, ammount=4):
    am = ammount

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
    amount1 = amount+1
    await ctx.channel.purge(limit=amount1)


@bot.command()
async def help(ctx):

    author = ctx.message.author

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
        name="info", value="Shows the Information of this bot", inline=False)
    embed.add_field(
        name="py", value="Shows all the coding help links bunny needs", inline=False)
    embed.add_field(
        name="danktrade", value="Check the amount of kn an zz while trading", inline=False)
    embed.add_field(
        name="botify", value="Add the bot tag to your Message", inline=False)
    embed.add_field(
        name="emojify", value="Make you text into emoji", inline=False)
    embed.add_field(name="spoilify",
                    value="Make you text ||concealed||", inline=False)
    embed.add_field(
        name="members", value="Gives number of member count in a server", inline=False)
    embed.set_footer(text="A general purpose bot made by Bunny Pranav")
    await author.send(embed=embed)
    await ctx.send(" <:mail:812334350233632798> You Have got Mail!! <:mail:812334350233632798> ")
    await ctx.message.add_reaction('🇸')
    await ctx.message.add_reaction('🇪')
    await ctx.message.add_reaction('🇳')
    await ctx.message.add_reaction('🇹')
    await ctx.message.add_reaction('▫️')
    await ctx.message.add_reaction('🇩')
    await ctx.message.add_reaction('🇲')


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bunny's Bot Info",
                          description="The Info of this bot", color=0x05b1eb)
    embed.add_field(name="Invite Link",
                    value="https://dsc.gg/bunnysbot", inline=False)
    embed.add_field(name="Support Server",
                    value="https://dsc.gg/botstopia", inline=False)
    embed.add_field(name="Servers I am in",
                    value=len(bot.guilds), inline=False)
    embed.add_field(name="My Creator And Developer",
                    value="Bunny Pranav#8468", inline=False)
    embed.set_footer(text="My Creator And Developer : Bunny Pranav#8468")
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


@bot.command()
async def spoilify(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into hidden secrets
    '''
    author = ctx.message.author
    spoilified = ''
    if text == '':
        await ctx.send('Remember to say what you want to convert!')
    else:
        for i in text:
            spoilified += '||{}||'.format(i)
        if len(spoilified) + 2 >= 2000:
            await ctx.send('Your message in spoilers exceeds 2000 characters!')
        if len(spoilified) <= 4:
            await ctx.send('Your message could not be converted!')
        else:
            await author.send('`'+spoilified+'`')
            await ctx.message.delete()
            await ctx.send(spoilified)


@bot.command()
async def emojify(ctx, *, text: str):
    '''
    Converts the alphabet and spaces into emoji
    '''
    author = ctx.message.author
    emojified = ''
    formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
    if text == '':
        await ctx.send('Remember to say what you want to convert!')
    else:
        for i in formatted:
            if i == ' ':
                emojified += '     '
            else:
                emojified += ':regional_indicator_{}: '.format(i)
        if len(emojified) + 2 >= 2000:
            await ctx.send('Your message in emojis exceeds 2000 characters!')
        if len(emojified) <= 25:
            await ctx.send('Your message could not be converted!')
        else:
            await ctx.send(emojified)


@bot.command()
async def botify(ctx, *, message):
    '''
    Creates a webhook, that says what you say. Like echo.
    '''
    pfp = requests.get(ctx.author.avatar_url_as(
        format='png', size=256)).content
    hook = await ctx.channel.create_webhook(name=ctx.author.display_name,
                                            avatar=pfp)

    await ctx.message.delete()
    await hook.send(message)
    await hook.delete()


@bot.command()
async def members(ctx):
    await ctx.send(f'`No of members Are`: **{ctx.guild.member_count}**')

bot.run("Nzk4MTk4MzYxMDY0NjAzNzEx.X_xiJw.VprDLErH56HFgtbSumFHWy1jHIs")
