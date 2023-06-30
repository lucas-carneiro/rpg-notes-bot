import os
import discord
import whisper
import openai

openai.api_key = os.environ.get('OPEN_AI_KEY')

PROMPT = 'Esta conversa foi feita durante um jogo de Dungeons & Dragons 5e, com uma equipe formada por elfo Erdan, hobbit Feijir, humana Yrda e humano Alev.'
QUESTION = 'O texto abaixo foi transcrito de um modelo de reconhecimento de voz. Corrija os erros encontrados nele sabendo que se trata de uma sessão de RPG utilizando o sistema Dungeons & Dragons 5e, e retorne apenas um resumo que somente contenha os fatos mais importantes listados em bullet points.'

# speech to text
async def stt(sink: discord.sinks, user, channel, top, language):
    print('starting stt')
    await sink.vc.disconnect()
    for user_id, audio in sink.audio_data.items():
        if user_id == user:
            filename = createAudioFile(audio)
            transcription = transcribeAudio(filename, language)
            os.remove(filename)
            await channel.send(f'Transcription:\n{transcription}')
            notes = takeNotes(transcription)
            await channel.send(f'Notes:\n{notes}')

def createAudioFile(audio):
    audio: discord.sinks.core.AudioData = audio
    filename = 'audio.wav'
    with open(filename, 'wb') as f:
        f.write(audio.file.getvalue())
    return filename

def transcribeAudio(filename, language):
    model = whisper.load_model('base')
    result = model.transcribe(filename, initial_prompt=PROMPT, language=language)
    return result['text']

def takeNotes(transcription):
    result = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': f'{QUESTION}\n{transcription}'}])
    print(f'{result.model} usage: {result.usage.prompt_tokens} input tokens + {result.usage.completion_tokens} output tokens = {result.usage.total_tokens} tokens')
    return result.choices[0].message.content

