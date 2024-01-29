import telegram
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,CallbackQueryHandler,MessageHandler, filters

bot_token = "6587824191:AAHOA32W7OmfJZRYW5QQz8Lr3yBD08DQBgk"

url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
channel_id = "-1002109782386"

def create_buttons():
    button1 = InlineKeyboardButton('입점문의', url='https://t.me/gdaisy0', callback_data='button1')
    button2 = InlineKeyboardButton('입점문의', callback_data='button2')
    button3 = InlineKeyboardButton('입점문의', callback_data='button3')
    button4 = InlineKeyboardButton('입점문의', callback_data='button4')
    button5 = InlineKeyboardButton('입점문의', callback_data='button5')
    button6 = InlineKeyboardButton('입점문의', callback_data='button6')
    button7 = InlineKeyboardButton('입점문의', callback_data='button7')
    button8 = InlineKeyboardButton('입점문의', callback_data='button8')
    button9 = InlineKeyboardButton('메이킹 봇세팅',url="https://t.me/+a9mmZS5rMHo0NDRl", callback_data='button9')
    buttons = [[button1, button2], [button3,button4],[button5,button6],[button7,button8],[button9]]
    return buttons

def switch_case(x):
    match x:
        case 'button1':
            return '1-1'
        case 'button2':
            return '1-2'
        case 'button3':
            return '2-1'
        case 'button4':
            return '2-2'
        case 'button5':
            return '3-1'
        case 'button6':
            return '3-2'
        case 'button7':
            return '4-1'
        case 'button8':
            return '4-2'
        case _:
            return '알수 없는 버튼'
            
async def button_callback(update: Update, context):
    query = update.callback_query
    query_data = query.data

    # 팝업 메시지 전송
    await query.answer(text=switch_case(query_data),show_alert=True)

async def post_message_to_channel():
    try:
        bot = telegram.Bot(token=bot_token,)
        buttons = create_buttons()
        keyboard = InlineKeyboardMarkup(buttons)
        video_path = 'https://velog.velcdn.com/images/suonwoo/post/2688a7ef-c327-40a9-a97c-7176b6a3cec7/image.mp4'
        message = '''
아파트 정비 사업 이후 처음으로 
우리 증원이 생겼습니다
다시한번 새 주민이자 새 식구를 
박수로 맞이하여 주시길 바랍니다
        '''
        
        await bot.send_video(chat_id=channel_id, video=video_path, reply_markup=keyboard, caption=message, read_timeout=30, write_timeout=30)
    except Exception as e :
        print(f"1에러 발생{e}")
# 채팅방 입장시 보내는 문구
async def welcome_message(update, context):
    await post_message_to_channel()

async def run_macro():
    while True:
        await post_message_to_channel()
        await asyncio.sleep(300)

def main():
    try:
        application = ApplicationBuilder().token(bot_token).build()
        # 백그라운드로 실행
        loop = asyncio.get_event_loop()
        loop.create_task(run_macro())
        
        application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_message))
        application.add_handler(CallbackQueryHandler(button_callback))
        
        application.run_polling( )
    except Exception as e:
        print(f"2에러 발생{e}")

if __name__ == '__main__':
    main()
    