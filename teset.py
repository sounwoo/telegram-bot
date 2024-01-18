import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,CallbackQueryHandler


bot_token = "토큰 아이디"

url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

channel_id = "채널 아이디"

messge = 'test1'

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

def post_message_to_channel():
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    buttons = create_buttons()
    keyboard = InlineKeyboardMarkup(buttons)
    data = {
        'chat_id': channel_id,
        'text': messge,
        'reply_markup': keyboard.to_json(),
        'parse_mode': 'HTML'
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('메시지가 성공적으로 게시되었습니다.')
    else:
        print('메시지 게시에 실패하였습니다.')

if __name__ == '__main__':
    post_message_to_channel()
    application = ApplicationBuilder().token(bot_token).build()
    
    application.add_handler(CallbackQueryHandler(button_callback))
    
    application.run_polling()