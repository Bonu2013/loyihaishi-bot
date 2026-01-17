from aiogram import Bot,Dispatcher,F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
import asyncio

TOKEN= "8216869872:AAEg_-_Ei2438UnUvqgv64vv3vuxL-B-igM"
bot=Bot(token=TOKEN)
dp=Dispatcher()


list1=[7997652702,5474407510,6163218781,6556750018,6405694392,6183363496,547577939,1716549072]

buttons=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Uy"),KeyboardButton(text="Maktab")],
        [KeyboardButton(text="qo'shimcha darsga")],
        [KeyboardButton(text="Contact",request_contact=True),KeyboardButton(text="Location",request_location=True)]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_handler(msg:Message):
    foydalanuvni_taxi=msg.from_user.id
    if foydalanuvni_taxi in list1:
        await msg.answer(f"Assalomu Alaykum bu bolalar uchun mos taxi  bot!")
        await msg.answer(f'Sizning ID raqamingiz: {msg.from_user.id}' , reply_markup=buttons)
    else:
        await msg.answer(f"Assalomu Alaykum sizga bu botga kirishga ruhsat yo'q, bopt paka!")


@dp.message(F.text=="Uy")
async def uy(msg:Message):
    await msg.answer("Siz uy tugmasini bosdingiz , xozir yetib keladi uyingizga taxi!",reply_markup=ReplyKeyboardRemove())

@dp.message(F.text=="Maktab")
async def maktab(msg:Message):
    await msg.answer("Siz maktab tugmasini bosdingiz, xozir maktabga taxi yetib keladi ,bolangizni olib ketish uchun!",reply_markup=ReplyKeyboardRemove())

@dp.message(F.text=="qo'shimcha darsga")
async def qoshimcha_darsga(msg:Message):
    await msg.answer("Siz qo'shimcha darsga tugmasini bosdingiz, xozir qo'shimcha darsga taxi yetib keladi ,bolangizni olib ketish uchun!",reply_markup=ReplyKeyboardRemove())

@dp.message(F.contact)
async def contact_handler(msg: Message):
    phone = msg.contact.phone_number
    await msg.answer(
        f" Telefon raqamingiz qabul qilindi: {phone}",
        reply_markup=ReplyKeyboardRemove()
    )

@dp.message(F.location)
async def location_handler(msg: Message):
    lat = msg.location.latitude
    lon = msg.location.longitude
    await msg.answer(
        f"Joylashuv qabul qilindi:\nLat: {lat}\nLon: {lon}",
        reply_markup=ReplyKeyboardRemove()
    )

@dp.message(F.voice)
async def save_audio(msg:Message):
    audio_id=msg.voice.file_id
    manzil=f'./media2/audio/{msg.voice.file_id}.ogg'

    await msg.bot.download(audio_id,manzil)
    await msg.answer("Audio saqlandi")
import os

@dp.message(F.photo)
async def save_photo(msg:Message):
    rasm_id=msg.photo[-1].file_id
    manzil=f'./media1/foto/{msg.photo[-1].file_id}.jpg'

    await msg.bot.download(rasm_id,manzil)
    await msg.answer("Rasm saqlandi")

@dp.message(F.text=="Video")
async def menu(msg:Message):
    video=FSInputFile("media2/video/1716549072.mp4")
    await msg.answer_video(video,caption="Bu video yozuv bilan tagida chiqadi")

@dp.message(F.video)
async def video_save(msg:Message):
    video=msg.video
    await bot.download(video.file_id,f"media/video/{msg.video.file_id}.mp4")
    await msg.answer("Videoingiz saqlandi")

async def main():
    print("Bot is start...")
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main()) 