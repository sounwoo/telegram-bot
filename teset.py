import requests
import telegram
import time
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,CallbackQueryHandler


bot_token = "token"

url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
# https://api.telegram.org/bot6750955458:AAErXF6BZPv4l6m7SJZFlw2_aFsOuI-Sue8/getUpdates
# 그룹방 id -4149801195
# 채널 id -1002137269394
channel_id = "채널id"


def create_buttons():
    button1 = InlineKeyboardButton('test 1', callback_data='button1')
    button2 = InlineKeyboardButton('test 2', callback_data='button2')
    button3 = InlineKeyboardButton('test 3', callback_data='button3')
    button4 = InlineKeyboardButton('네이버 링크',url="https://naver.com", callback_data='button4')
    buttons = [[button1, button2,button3], [button4]]
    return buttons

async def button_callback(update: Update, context):
    query = update.callback_query
    query_data = query.data
    
    # 팝업 메시지 작성
    if query_data == 'button1':
        message = 'test 1'
    elif query_data == 'button2':
        message = 'test 2를 클릭하셨습니다!'
    elif query_data == 'button3':
        message = 'test 3'
    elif query_data == 'button4':
        message = '네이버'
    else:
        message = '알 수 없는 버튼입니다.'

    # 팝업 메시지 전송
    await query.answer(text=message,show_alert=True)

async def post_message_to_channel():
    bot = telegram.Bot(token=bot_token)
    buttons = create_buttons()
    keyboard = InlineKeyboardMarkup(buttons)
    photo_path = '이미지 경로'
    messge = 'test1'
    await bot.send_photo(chat_id=channel_id, photo=open(photo_path, 'rb'), reply_markup=keyboard, caption=messge)
    
    

def send_chat():
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    messge = '매크로 테스트'
    data = {
        'chat_id': channel_id,
        'text': messge,
        'parse_mode': 'HTML'
    }
    requests.post(url, json=data)


def run_macro():
    while True:
        send_chat()
        time.sleep(5)

if __name__ == '__main__':
    async def main():
        await post_message_to_channel()
    asyncio.run(main())
    run_macro()
    application = ApplicationBuilder().token(bot_token).build()
    
    application.add_handler(CallbackQueryHandler(button_callback))
    
    application.run_polling()