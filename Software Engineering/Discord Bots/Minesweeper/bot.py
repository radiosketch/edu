import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command
async def minesweeper():
    '''
    Start a game of minesweeper!
    TODO https://discordpy.readthedocs.io/en/stable/
    '''



TOKEN = 'MTA1MjY5MjQzMzIzMTY5MTgxNw.GvaeDG.Z1HnPi4DcaavkaMfL0iFqQz3ffh-c2xvaGoyPQ'
client.run(TOKEN)
