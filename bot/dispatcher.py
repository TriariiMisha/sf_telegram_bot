from aiogram import Dispatcher

from quiz.router import quiz_router


dp = Dispatcher()

# dp.message.register(command_start_handler, CommandStart())
# dp.message.register(echo_handler)
dp.include_router(quiz_router)
