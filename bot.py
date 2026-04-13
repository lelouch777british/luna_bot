import os
import telebot
from deepseek import DeepSeekAPI

TELEGRAM_TOKEN = "8671491498:AAHJHSg-K-mblv9bLE1i3q1Z6rJ62QsgnyI"
DEEPSEEK_API_KEY = "sk-27846af24ac241c98e52b2cb4ff20dde"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
deepseek = DeepSeekAPI(api_key=DEEPSEEK_API_KEY)

@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
    if message.voice:
        # расшифровка голосового сообщения
        file_info = bot.get_file(message.voice.file_id)
        audio_file = bot.download_file(file_info.file_path)
        with open("voice.ogg", "wb") as f:
            f.write(audio_file)
        user_text = "расшифровка недоступна, но я запомню, что ты говорила"
    else:
        user_text = message.text

    response = deepseek.chat(user_text, context=f"Яся — девушка, физика, балкон, шрамы, Луна")
    bot.reply_to(message, response)

bot.polling()