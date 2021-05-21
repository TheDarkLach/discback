import discord
import os
import time
from keep_alive import keep_alive
from discord.ext import commands

#client = discord.Client()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(activity=discord.Game(name="with these bitches hearts"))


@client.event
async def on_message(message):
    if client.user != message.author:
        if 'yasa' in message.content:
            await message.channel.send('lol hate that guy')
        if 'utsho' in message.content:
          await message.channel.send('What a sexy beast')
        if 'lacina' in message.content:
          await message.channel.send('what a fucking reatrd')
        if 'penley' in message.content:
          await message.channel.send(':bite: haha W')
        

    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):
    # Steals your reaction by removing the original and adding it's own
    if not user.bot and reaction.message.content == "try me":
        await reaction.remove(user)
        await reaction.message.add_reaction(reaction.emoji)


@client.event
async def on_message_delete(message):
  if message.author == client.user:
    return
  if message.content == "@everyone":
    return
  if "@" in message.content:
    return
  elif message.content == "@here":
    return
  await message.channel.send('{}: {}'.format(message.author, message.content))

@commands.command()
async def react(ctx):
  vote_msg = await ctx.channel.send("boobs?")
  await vote_msg.add_reaction('👍')
  await vote_msg.add_reaction('👎')
  time.sleep(10)
  vote_msg = await vote_msg.channel.fetch_message(vote_msg.id) # refetch message
  # default values
  positive = 0
  negative = 0
  for reaction in vote_msg.reactions:
    if reaction.emoji == '👍':
        positive = reaction.count - 1 # compensate for the bot adding the first reaction
    if reaction.emoji == '👎':
      negative = reaction.count - 1
  await ctx.channel.send(f'Vote Result: {positive} straight people and {negative} gays')

client.add_command(react)


"""@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content[::-1])"""



keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
