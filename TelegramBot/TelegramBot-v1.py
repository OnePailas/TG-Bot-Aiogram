import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить сообщение
logging.basicConfig(level = logging.INFO)

# Объект бота, передаем токен
bot = Bot(token = '7931431293:AAGdBWWMxySPPcwmzshAuHEFSzuR8BwZGGY')

#Диспетчер
dp = Dispatcher()


#Хэндлер для команды 'start'
@dp.message(Command('start'))
async def cmdStart(message: types.Message):
    await message.reply('Привет, я начинающий программист OnePailas создал телеграм бота на библиотеке "Aiogram". \n\
Цель создания: получить больше опыта в программировании. Изучить новую библиотеку, тем самым получить больше знаний.\n\
Ознакомться со списком функций бота можно с помощью команды /help')
    

#Хендлэр для команды 'help'
@dp.message(Command('help'))
async def msgHelp(message: types.Message):
    await message.reply('А вот и список доступных команд:\n\
►/howay - данная команда спрашивает "Как Ваши дела?".\n ⫷⫷ПРИМЕЧАНИЕ⫸⫸\n\
Есди Вы хотите ответить на сообщение, то используйте команду "/result" и ответы: хорошо, отлично, плохо, не очень.')


#Хэндлер для команды 'umn'
@dp.message(Command('umn'))
async def msgUmn(message: types.Message):
    await message.answer('Стой, ты не знаешь кто умничка? Так это же ты, \
и даже не пытайся спорить, я лучше знаю!')


#Хэндлер для команды 'test'. После "await bot.send_message" в скобках указывается айди чата, который должно прийти соо бота
@dp.message(Command('test'))
async def msgTest(message: types.Message, bot: Bot):
    await bot.send_message(-100123456789, 'GASDHASJD')


#Хэндлэр для команды 'howay'
@dp.message(Command('howay'))
async def msgHoway(message: types.Message):
    await message.answer('Кстати, а как твои дела?')


#Запуск поллинга для апдейта
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())