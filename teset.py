import telegram
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,CallbackQueryHandler,MessageHandler, filters, JobQueue, BaseHandler


bot_token = "봇 토큰"

url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

channel_id = "채널 || 채팅방 id"


def create_buttons():
    button1 = InlineKeyboardButton('입점문의', url='https://t.me/ggoio', callback_data='button1')
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

async def button_callback(update: Update, context):
    query = update.callback_query
    query_data = query.data
    
    if query_data == 'button1':
        message = '1-1'
    elif query_data == 'button2':
        message = '1-2'
    elif query_data == 'button3':
        message = '2-1'
    elif query_data == 'button4':
        message = '2-2'
    elif query_data == 'button5':
        message = '3-1'
    elif query_data == 'button6':
        message = '3-2'
    elif query_data == 'button7':
        message = '4-1'
    elif query_data == 'button8':
        message = '4-2'
    elif query_data == 'button9':
        message = '링크'            
    else:
        message = '알 수 없는 버튼입니다.'

    # 팝업 메시지 전송
    await query.answer(text=message,show_alert=True)

async def post_message_to_channel():
    bot = telegram.Bot(token=bot_token)
    buttons = create_buttons()
    keyboard = InlineKeyboardMarkup(buttons)
    video_path = '/Users/apple/Desktop/IMG_9826.mp4'
    message = '''
    아파트 정비 사업 이후 처음으로 
우리 증원이 생겼습니다
다시한번 새 주민이자 새 식구를 
박수로 맞이하여 주시길 바랍니다
    '''
    await bot.send_video(chat_id=channel_id, video=open(video_path, 'rb'), reply_markup=keyboard, caption=message)

# 채팅방 입장시 보내는 문구
async def welcome_message(update, context):
    print('입장')
    await post_message_to_channel()

async def run_macro():
    while True:
        await post_message_to_channel()
        await asyncio.sleep(1800)



def main():
    application = ApplicationBuilder().token(bot_token).build()
    # 백그라운드로 실행
    loop = asyncio.get_event_loop()
    loop.create_task(run_macro())
    
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_message))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    application.run_polling( )
    
if __name__ == '__main__':
    main()