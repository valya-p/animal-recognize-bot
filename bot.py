import asyncio
import logging
import sys

import cv2
import os
import keras
import numpy as np
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import tensorflow as tf
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('BOT_TOKEN')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

class_name_en = [
    'бабОчка',
    'котик',
    'чикен',
    'корова му-му-му',
    'собака',
    'наш слон',
    'лошадь',
    'егор шип',
    'павук',
    'белка (не из доты 2)',
]


@dp.message(F.photo)
async def command_start_handler(message: Message, bot: Bot, model) -> None:
    photo = message.photo[-1]
    photo = await bot.download(file=photo)
    img = cv2.imdecode(np.frombuffer(photo.read(), np.uint8), 1)
    img = tf.image.resize(img, (256, 256))
    prediction_d = model.predict(np.expand_dims(img.numpy() / 255., axis=0))
    prediction_name = class_name_en[np.argmax(prediction_d)]
    await message.reply(f'Мой предикт, что это {prediction_name}')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    model = keras.saving.load_model("model.keras")
    await dp.start_polling(bot, model=model)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())