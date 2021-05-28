# from bot import TGBot
# from config import TOKEN
# from keyboards import START_KB
# from models.model import Cart, User
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
#
#
# bot = TGBot(token=TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     User.create_user(str(message.chat.id))
#     Cart.get_or_create_cart(str(message.chat.id))
#     print(message.from_user.username)
#
#     kb = ReplyKeyboardMarkup()
#     buttons = [KeyboardButton(button_name) for button_name in START_KB.values()]
#     kb.add(*buttons)
#     bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}', reply_markup=kb)
#
#
# @bot.message_handler(func=lambda message: message.text == START_KB['order'])
# def orders(message):
#
#     results = []
#
#     order_banana = {
#         'title': '',
#         'text': '',
#         'image': ''
#     }
#     order_backpack = {
#         'title': '',
#         'text': '',
#         'image': ''
#     }
#     order_clothes = {
#         'title': '',
#         'text': '',
#         'image': ''
#     }
#
#     for order in order_banana, order_backpack, order_clothes:
#         kb = InlineKeyboardMarkup()
#
#         button = InlineKeyboardButton(text='Добавить в корзину', callback_data=f'{product_lookup}_{product.id}')
#
#         kb.add(button)
#         result1 = InlineQueryResultArticle(
#             id=str(product.id),
#             title=order.title,
#             description=order.,
#             thumb_url=product.image,
#             reply_markup=kb,
#
#             input_message_content=InputTextMessageContent(
#                 parse_mode='HTML',
#                 disable_web_page_preview=False,
#                 message_text=f"{product.title} \n{product.description} <a href='{product.image}'>&#8204</a>"
#             )
#
#         )
#         results.append(result1)
#
#     bot.answer_inline_query(message.chat.id, results, cache_time=0)
#
