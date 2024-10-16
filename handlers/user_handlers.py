from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from lexicon.lexicon import LEXICON_RU
from aiogram import Router, F

router = Router()

genre_button = InlineKeyboardButton(
    text='Выбрать жанр',
    callback_data='genre_button_pressed'
)

year_button = InlineKeyboardButton(
    text='Выбрать от какого года',
    callback_data='year_button_pressed'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[genre_button],
                     [year_button]]
)

top_movie_genres = ("1. Action\n 2. Comedy\n 3. Drama\n 4. Thriller\n 5. Adventure\n "
                    "6. Horror\n 7. Science Fiction\n 8. Romance\n 9. Fantasy\n 10. Animation\n")

top_movie_genres_dict = {
    1: 'Action',
    2: 'Comedy',
    3: 'Drama',
    4: 'Thriller',
    5: 'Adventure',
    6: 'Horror',
    7: 'Science Fiction',
    8: 'Romance',
    9: 'Fantasy',
    10: 'Animation'
}


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Нажми на кнопку жанр и выбери жанр/год',
        reply_markup=keyboard
    )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.callback_query(F.data == 'genre_button_pressed')
async def genre_button_process(callback: CallbackQuery):
    if callback.message.text != 'Выбрать жанр':
        await callback.message.edit_text(
            text=top_movie_genres,
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()


@router.callback_query(F.data == 'year_button_pressed')
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Выбрать от какого года':
        await callback.message.edit_text(
            text='Напиши ОТ какого года предлагать кино',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()
