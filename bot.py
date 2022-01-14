import asyncio
import config
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
import imdb
import random

bot = SimpleLongPollBot(tokens=config.settings['TOKEN'],
                        group_id=config.settings['VK_GROUP_ID'])
ia = imdb.IMDb()

@bot.message_handler(bot.regex_filter(r'(?i)(.*?)(фильм|кино|посмотреть)(.*?)'))
async def greet(event: SimpleBotEvent) -> str:
    top = ia.get_popular100_movies()
    random.shuffle(top)

    title = top[0]
    movie_id = top[0].movieID
    movie_url = f'https://www.imdb.com/title/tt{movie_id}/'
    emoji = '&#127829;'
    
    msg_text = f'Советую посмотреть: {title} {emoji}'

    await event.answer(msg_text)
    await event.answer(message=movie_url)


bot.run_forever()


