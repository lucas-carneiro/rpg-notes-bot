# RPG Notes Bot
Bot para Discord que transcreve falas importantes durante a sessão de RPG e faz um resumo de anotações sobre a sessão.

## Comandos
`!start <language> <top>`
join my voice channel, **start** recording, listen to messages only from you, store the **top** audios in memory

`!stop`
**stop** recording, transcribe the **top** audios using **language**, then write notes from it in the same chat channel than the command

## Chamada API feita para Whisper
```bash
curl https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer <Open API Private Key>" \
  -H "Content-Type: multipart/form-data" \
  -F file="@rpg.m4a" \
  -F model="whisper-1" \
  -F prompt="O audio foi extraido de uma sessao de rpg D&D 5e" \
  -F language="pt"
```

## Resultado
> bem pessoal agora vocês estão chegando em Waterdeep e lá vocês irão encontrar o famoso mago Gandalf que além de ter poderes também é um grande conhecedor de magias de fogo ele será capaz de ensinar novos truques para vocês mas para isso vocês terão que conseguir alguns itens para ele então não encontrem antes de terem seis rabos de dragão e um olho de beholder aí então ele irá ajudar a ensinar magias para vocês

Apesar de não termos o áudio em questão para comparar, o resultado de fato foi extremamente próximo do original por conta do **prompt** utilizado.

## Custo
### Whisper API
$0.006/min = custo da API de transcrição da Open AI

1 sessão = 2h = $0.72

1 semana = 2 sessões = $1.44

1 mês = 4 semanas = $5.76

restante da campanha = 8 meses = **\$46.08**

top 10 audios = 10 minutos > 8 meses = $46.08 / 12 = **\$3.84**

### Local Whisper + Chat API
top 10 audios = 4360 tokens (input) + 3120 tokens (output)
full = 52320 tokens (input) + 37440 tokens (output)

| Product | Context | Input     | Output   | Top 10 Price                | Full Price |
|---------|---------|-----------|----------|-----------------------------|------------|
| GPT-4   | 8k      | 0.00003   | 0.00006  | 0.1308 + 0.1872   = 0.318   | 3.816      |
| GPT-4   | 32k     | 0.00006   | 0.00012  | 0.2616 + 0.3744   = 0.636   | 7.632      |
| GPT-3.5 | 4k      | 0.0000015 | 0.000002 | 0.00654 + 0.00624 = 0.01278 | 0.15336    |
| GPT-3.5 | 16k     | 0.000003  | 0.000004 | 0.01308 + 0.01248 = 0.02556 | 0.30672    |

restante da campanha = 8 meses:
0.318 * 64 = 20.352
0.636 * 64 = 40.704
0.01278 * 64 = 0.81792
0.02556 * 64 = 1.63584
3.816 * 64 = 244.224
7.632 * 64 = 488.448
0.15336 * 64 = 9.81504
0.30672 * 64 = 19.63008

mais barato: top 10 w/ GPT-3.5 4k = **\$0.82**
