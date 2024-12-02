import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import time

# Включаем логирование, чтобы не пропустить сообщение
logging.basicConfig(level = logging.INFO)

# Объект бота, передаем токен
bot = Bot('7931431293:AAGdBWWMxySPPcwmzshAuHEFSzuR8BwZGGY')

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
►/howay - данная команда спрашивает "Как Ваши дела?". \n ⫷⫷ПРИМЕЧАНИЕ⫸⫸\n\
Если Вы хотите ответить на сообщение, то используйте ответ, а перед ним "-" ответы: хорошо, плохо.\n\
►/umn - исследуй эту команду самостоятельно.\n\
►/time - данная команда сообщает время по мск.')


#Хэндлер для команды 'umn'
@dp.message(Command('umn'))
async def msgUmn(message: types.Message):
    await message.answer('Стой, ты не знаешь кто умничка? Так это же ты, \
и даже не пытайся спорить, я лучше знаю!')


@dp.message(Command('time'))
async def msgTime(message: types.Message):
    await message.answer('Время на данный момент: ' + time.strftime('%Y/%m/%d %H:%M', time.localtime()))

#Хэндлэр для команды 'howay'
@dp.message(Command('howay'))
async def msgHoway(message: types.Message):
    await message.answer('Кстати, а как твои дела?')


@dp.message(Command('хорошо', prefix= '-'))
async def msgOtv1(message: types.Message):

    if 'хорошо':
        await message.reply('Супер, я рад за тебя. Надеюсь и в будущем будет все хорошо')

@dp.message(Command('плохо', prefix= '-'))
async def msgOtv2(message: types.Message):

    if 'плохо':
        await message.reply('Грустно, надеюсь у тебя все придет к лучшему')



#Хэндлер для команды 'test'. После "await bot.send_message" в скобках указывается айди чата, который должно прийти соо бота
@dp.message(Command('test'))
async def msgTest(message: types.Message, bot: Bot):
    await bot.send_message(-100123456789, 'GASDHASJD')


#Запуск поллинга для апдейта
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())