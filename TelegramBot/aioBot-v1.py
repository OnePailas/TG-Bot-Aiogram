import asyncio
import logging 

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

logging.basicConfig(level = logging.INFO)

bot = Bot('7220477419:AAGaTs34Ot7iFRLXbFjErtGphkBWqD0ks1o')
dp = Dispatcher()

@dp.message(Command('start'))
async def Start1(message: types.Message):
    await message.reply('Привет. Я - OnePailas, написал телеграм бота,\n\
для прохождения практики после изучения библиотеки "AioGram". \n\
Список команд - /cl, либо кнопочка снизу', reply_markup = opencl)

@dp.message(Command('tart', prefix = ('s', 'S')))
async def StartC(message: types.Message):
    await message.reply('Привет. Я - OnePailas, написал телеграм бота,\n\
для прохождения практики после изучения библиотеки "AioGram". \n\
Список команд - /cl, либо кнопочка снизу', reply_markup = opencl)

@dp.message(Command('l', prefix = ('c', 'C')))
async def CL(message: types.Message):
    await message.reply(texts.format(name = message.from_user.full_name), reply_markup = cl)

@dp.message(Command('cl'))
async def Cl(message: types.Message):
    await message.reply(texts.format(name = message.from_user.full_name), reply_markup = cl)

@dp.message(Command('mn', prefix = ('u', 'U')))
async def UmnC(message: types.Message):
    await message.reply('Ты умничкаа')

@dp.message(Command('umn'))
async def Umnc(message: types.Message):
    await message.reply('Ты умничкаа')

opencl = [[InlineKeyboardButton(text = '📝Список команд', callback_data = 'opencllllllllll')]]
opencl = InlineKeyboardMarkup(inline_keyboard = opencl)

cl = [[InlineKeyboardButton(text = 'Umn', callback_data = 'umnnnnnnnnnn')],
    [InlineKeyboardButton(text = 'Hello', callbalck_data = 'helllllo')]]
cl = InlineKeyboardMarkup(inline_keyboard = cl)

texts = 'Привет, {name}, данная команда Вам расскажет, какие команды доступны и что они выполняют. \
Также команды можно писать без "/", так как уже были добавлены префиксы, которые позволяют так писать, но если удобно со "/", \
то и это доступно. \n\
А теперь попробуй данные команды:\n\
\n\
/start - Команда для старта собственно бота\n\
\n\
/umn - Тестовая команда, которая сообщает вам, что вы умнчика'

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

