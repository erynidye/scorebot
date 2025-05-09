import os
import discord
import processing as p

from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import datetime


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())

bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'Bot online as username {bot.user}')


@bot.command(name="position")
async def get_position(ctx, team):

    em = discord.Embed(title=f"Current Position - Team 16-{team}", color=discord.Color.blue())
    data = p.scrape("Platinum")
    rank = data[data['Team Number'] == "16-"+team].index.values[0]
    percent = round((rank/len(data)*100), 2)
    score = data.at[rank, 'Total Score']
    em.add_field(name="Rank", value=f"{rank} out of {len(data)}\nTop {percent}%")
    em.add_field(name="Score", value=f"{score} points\n 400 points possible")
    await ctx.send(embed=em)


@bot.command(name="team")
async def get_team(ctx, team):
    data = p.process_r2()
    index = data[data['Team Name'] == "16-"+team].index.values[0]
    df2 = p.scrape(data.at[index, 'Tier'])
    index2 = df2[df2['Team Number'] == "16-"+team].index.values[0]
    r1score = data.at[index, 'R1 Total Score']
    r2image = data.at[index, 'R2 Image Score']
    r2cisco = data.at[index, 'R2 Cisco Score']
    stateimage = df2.at[index2, 'Score']
    cumulative = data.at[index, 'Cumulative Score'] + stateimage
    division = data.at[index, 'Division/ Category']
    location = data.at[index, 'Location']
    tier = data.at[index, 'Tier']
    em = discord.Embed(title=f"Team 16-{team}", color=discord.Color.blue())
    em.add_field(name="", value=f"{division} | {location} | {tier}")
    em.add_field(name="Scores", value=f"`Round 1 Score: {r1score}`\n{r1score}\n`Round 2 Image Score: {r2image}`\n{r2image}\n`Round 2 Cisco Score: {r2cisco}`\n{r2cisco}\n`State Round Image Score: {stateimage}`\n{stateimage}")
    em.add_field(name="Cumulative Score", value=f'{cumulative} points\n865.0 points possible')
    await ctx.send(embed=em)


@bot.command(name="lb")
async def leaderboard(ctx, tier):
    if tier.lower() == "platinum" or "plat":
        tier = "Platinum"
    elif tier.lower() == "gold":
        tier = "Gold"
    elif tier.lower() == "silver":
        tier = "Silver"
    else:
        tier = "All"
    data = p.scrape(tier)
    data = data.head(15)
    time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    message = f"**Current Scoreboard**\nOpen, {tier}\n*As of {time} ET*\n```{data.drop(columns=['Rank'])}```"
    if tier != "All":
        message += "\nhttps://scoreboard.uscyberpatriot.org/index.php?division=Open&tier="+tier
    else:
        message += "\nhttps://scoreboard.uscyberpatriot.org/index.php?division=Open"
    await ctx.send(message)


@bot.command(name="stats")
async def stats(ctx, tier):
    if tier.lower() == "platinum" or tier.lower() == "plat":
        tier = "Platinum"
    elif tier.lower() == "gold":
        tier = "Gold"
    elif tier.lower() == "silver":
        tier = "Silver"
    else:
        tier = "All"
    data = p.scrape(tier)
    mean = round(data['Total Score'].mean(), 2)
    stdev = round(data['Total Score'].std(), 2)
    max = data['Total Score'].max()
    min = data['Total Score'].min()
    q1 = data['Total Score'].quantile(0.25)
    median = data['Total Score'].quantile(0.5)
    q3 = data['Total Score'].quantile(0.75)
    p.plot(data)
    em = discord.Embed(title="Summary Statistics - Open, "+tier, color=discord.Color.blue())
    em.add_field(name="Mean and Stdev", value=f"Mean: {mean}\nStandard deviation: {stdev}")
    em.add_field(name="Five Number Summary", value=f"Median: {median}\nMaximum: {max}\n75th Percentile: {q3}\n25th Percentile: {q1}\nMinimum: {min}")
    file = discord.File("score.png")
    em.set_image(url="attachment://score.png")
    await ctx.send(embed=em, file=file)



bot.run(TOKEN)
