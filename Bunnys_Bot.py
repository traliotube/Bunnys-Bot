import discord
import random
import requests
import re
import os
import topgg
from discord.ext import commands
from discord.ext import tasks
from bs4 import BeautifulSoup

bot = commands.Bot(
    command_prefix="$",
    case_insensitive=True
)
bot.remove_command('help')
bot.topggpy = topgg.DBLClient(
    bot, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc5ODE5ODM2MTA2NDYwMzcxMSIsImJvdCI6dHJ1ZSwiaWF0IjoxNjQ0NTUwMzQ2fQ.uAXgQVWjGAh7QZUyKrvLihMmem1hHTyLvoZPBUSMWPU")


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
    embed.add_field(name="Developer Website",
                    value="https://bunnyorg.tk/", inline=False)
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
        name="botify", value="Add the bot tag to your Message", inline=False)
    embed.add_field(
        name="emojify", value="Make you text into emoji", inline=False)
    embed.add_field(name="spoilify",
                    value="Make you text ||concealed||", inline=False)
    embed.add_field(
        name="members", value="Gives number of member count in a server", inline=False)
    embed.set_footer(text="A general purpose bot made by Bunny Pranav")
    await author.send(embed=embed)
    await ctx.send(" <:mail:867307286363897868> You Have got Mail!! <:mail:867307286363897868> ")
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
                    value="https://discord.gg/dTehKH5kNE", inline=False)
    embed.add_field(name="Developer Website",
                    value="https://bunnyorg.tk/", inline=False)
    embed.add_field(name="Servers I am in",
                    value=len(bot.guilds), inline=False)
    embed.add_field(name="My Creator And Developer",
                    value="Bunny Pranav#8468", inline=False)
    embed.set_footer(text="My Creator And Developer : Bunny Pranav#8468")
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

# end commands


@bot.event
async def on_dbl_vote(data):
    """An event that is called whenever someone votes for the bot on Top.gg."""
    if data["type"] == "test":
        # this is roughly equivalent to
        # `return await on_dbl_test(data)` in this case
        return bot.dispatch("dbl_test", data)

    print(f"Received a vote:\n{data}")

bot.run("Nzk4MTk4MzYxMDY0NjAzNzEx.X_xiJw.VprDLErH56HFgtbSumFHWy1jHIs")
