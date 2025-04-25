from aiogram.filters.command import Command
from aiogram.types import Message
from urllib.parse import quote
from aiogram import Router, F

# questions and answer
questions_and_answers = [
    {'question': 'Столица Франции?', 'correct_answer': 'Париж'},
    {'question': 'Самый глубокий океан?', 'correct_answer': 'Тихий'},
    {'question': 'Самая высокая гора?', 'correct_answer': 'Эверест'}
]

# dict to store users' answers
current_question_index = {}

# initialize router
quiz_router = Router(name='quiz_router')

# router stars
@quiz_router.message(Command('quiz'))
async def quiz_start(message: Message):
    global questions_and_answers
    current_question_index[message.from_user.id] = 0  # Индекс первого вопроса
    question = questions_and_answers[current_question_index[message.from_user.id]]['question']
    await message.answer(question)

# handle answer
@quiz_router.message(F.text)
async def process_answer(message: Message):
    global questions_and_answers, current_question_index
    index = current_question_index.get(message.from_user.id, 0)
    correct_answer = questions_and_answers[index]['correct_answer'].lower().strip()
    user_answer = message.text.lower().strip()

    if user_answer == correct_answer:
        await message.answer('Верно! Следующий вопрос:')
    else:
        await message.answer('Неверно :( Попробуйте снова!')

    # Переходим к следующему вопросу
    next_index = index + 1
    if next_index >= len(questions_and_answers):
        del current_question_index[message.from_user.id]

        url = 't.me/sf_nice_telegram_bot'
        title = quote('Очень классный бот')
        description = quote('Реально очень классный бот')

        text = f'http://vk.com/share.php?url={url}&title={title}&description={description}&noparse=true'
        await message.answer(text)
    else:
        current_question_index[message.from_user.id] = next_index
        question = questions_and_answers[next_index]['question']
        await message.answer(question)
