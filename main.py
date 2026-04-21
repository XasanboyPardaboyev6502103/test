from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from asyncio import run
from buttons import k_button,i_button


TOKEN="6509243694:AAFiUY2QQr4vqSi7hOoGVr2Z3w1mREM6n-4"

bot=Bot(token=TOKEN)
dp=Dispatcher()

@dp.message(F.text=="IT haqida")
async def it_haqida(message:types.Message):
    await message.answer(f"""

IT - «Information Technology» so‘zining qisqartmasi bo‘lib, axborot texnologiyasi degan ma’noni anglatadi.

IT so‘zini ishlatganda, aslo «IT texnologiyalari» deb gapirilmaydi. Boisi, gapni to‘liq yozib, o‘zbekchaga o‘girsak «Axborot texnologiyalari texnologiyalari» ko‘rinishida namoyon bo‘ladi, bu esa biroz g‘alati eshitiladi.


""")

@dp.callback_query(F.data=="foundation")
async def foundation(callback:types.CallbackQuery):
    await callback.message.answer("Foundation haqida balo battar")

@dp.message(F.text=="IT kurslarimiz")
async def it_kurslarimiz(message:types.Message):
    await message.answer(f"bizning kurslarimiz",reply_markup=i_button)


@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer(f"salom {message.from_user.full_name}",reply_markup=k_button)



async def main():
    await dp.start_polling(bot)


run(main())

