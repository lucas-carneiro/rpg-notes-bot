import os
import discord
from discord import option
from stt import stt

DEFAULT_TOP = 10
DEFAULT_LANGUAGE = 'pt'

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description='Starts recording, listens to messages only from you, and stores the top audios in memory.')
@option('top', description=f'Set how many audio parts will be used. Each part can be 1 minute long. Default: {DEFAULT_TOP}')
@option('language', description=f'Set the audio language. Examples: en, es, it. Default: {DEFAULT_LANGUAGE}')
async def start(ctx, top=DEFAULT_TOP, language=DEFAULT_LANGUAGE):
    voice = ctx.author.voice
    if voice:
        channel = await voice.channel.connect()
        channel.start_recording(discord.sinks.WaveSink(), stt, ctx.author.id, ctx.channel, top, language)
        await ctx.respond('Started recording!')
    else:
        await ctx.respond('You need to join a voice channel before I can start!')

@bot.slash_command(description='Stops recording, transcribes the top audios using language, and return transcriptions and notes.')
async def stop(ctx):
    if ctx.voice_client:
        await ctx.respond('Processing...')
        print('stop recording')
        ctx.voice_client.stop_recording()
        print('stopped recording')
    else:
        await ctx.respond('I need to start before I can stop!')

bot.run(os.environ.get('DISCORD_KEY'))
