from bot import TGBot
from config import TOKEN
from keyboards import START_KB, ORDER, DELIVERY, ABOUT_US, SHOP
from models.model import Cart, User
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = TGBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    User.create_user(str(message.chat.id), username=message.from_user.username)
    Cart.get_or_create_cart(str(message.chat.id))
    print(message.from_user.username)

    start_kb = ReplyKeyboardMarkup()
    buttons = [KeyboardButton(button_name) for button_name in START_KB.values()]
    start_kb.add(*buttons)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}', reply_markup=start_kb)


# Вывод категорий
@bot.message_handler(func=lambda message: message.text == START_KB['categories'])
def categories(message):
    bot.send_categories(user_id=message.from_user.id)


# Вывод подкатегорий, либо же товаров
@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def subcategories(call):
    category_id = call.data.split('_')[1]
    bot.subcategories_or_products(category_id, call.message.message_id, call.message.chat.id, 'Выберите подкатегорию')


# Вывод продуктов в Инлайн режиме
@bot.inline_handler(func=lambda query: query.query.split('_')[0] == 'category')
def product_inline(query):
    category_id = query.query.split('_')[1]
    bot.subcategories_or_products(category_id, query.id, query.from_user.id, 'Выберите подкатегорию')


# Добавление в Корзину
@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'product')
def add_to_cart(call):
    user_id = call.from_user.id

    user_cart = Cart.get_cart(str(user_id))
    user_cart.add_product_to_cart(product_id=call.data.split('_')[1])
    bot.answer_callback_query(call.id, 'Товар добавлено в корзину', show_alert=True)


# Корзина
@bot.message_handler(func=lambda message: message.text == START_KB['cart'])
def get_root_category(call):
    bot.show_cart(str(call.from_user.id))


# Удаление из Корзины
@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'del')
def del_prod_from_cart(call):
    prod_id = call.data.split('_')[1]
    bot.del_product_from_cart(prod_id, call.id, str(call.from_user.id))


# Оформление заказа
@bot.message_handler(func=lambda message: message.text == 'Оформить заказ')
def checkout(message):

    bot.checkout_step_1(str(message.from_user.id))


@bot.message_handler(func=lambda message: User.get_step(str(message.chat.id)) == 1)
def save_name_go_step_2(message):

    bot.checkout_step_2(str(message.from_user.id), message.text)


@bot.message_handler(func=lambda message: User.get_step(str(message.chat.id)) == 2)
def save_name_go_step_3(message):

    bot.checkout_step_3(str(message.from_user.id), message.text)


@bot.message_handler(func=lambda message: User.get_step(str(message.chat.id)) == 3)
def save_name_go_step_4(message):
    bot.checkout_step_4(str(message.from_user.id), message.text)


@bot.message_handler(func=lambda message: User.get_step(str(message.chat.id)) == 4)
def save_name_go_step_5(message):
    bot.checkout_step_5(str(message.from_user.id), message.text)


@bot.message_handler(func=lambda message: User.get_step(str(message.chat.id)) == 5)
def save_name_go_step_6(message):
    bot.checkout_step_6(str(message.from_user.id), message.text)


@bot.message_handler(func=lambda message: message.text == START_KB['order'])
def order(message):
    text = ORDER
    img = 'https://twinsstore.com.ua/img/xcorp_rukzak.jpg.pagespeed.ic.IicNTB0CAP.webp'
    bot.send_message(message.chat.id, f'{text}\n\n{img}', disable_web_page_preview=False)


@bot.message_handler(func=lambda message: message.text == START_KB['delivery'])
def delivery_and_payment(message):
    text = DELIVERY
    img = 'https://www.instagram.com/p/B4VHcBCnZOi/?igshid=lc1vi0ix5qtl'
    bot.send_message(message.chat.id, f'{text}\n{img}', disable_web_page_preview=False)


@bot.message_handler(func=lambda message: message.text == START_KB['about_us'])
def delivery_and_payment(message):
    text = ABOUT_US
    img = 'https://www.instagram.com/p/CLJiwx9nwKa/?igshid=1lzf3lp4ucovt'
    bot.send_message(message.chat.id, f'{text}\n{img}', disable_web_page_preview=False)


@bot.message_handler(func=lambda message: message.text == START_KB['shop'])
def delivery_and_payment(message):
    text = SHOP
    img = 'https://www.instagram.com/p/ByK0jMai8yJ/?igshid=12yrf6bhl2mhq'
    bot.send_message(message.chat.id, f'{text}\n{img}', disable_web_page_preview=False)
"""
WEBHOOK_HOST = https://33.46.32.19:8443
PKEM = '/home/certificates/webhok_pkem.pem'
PKEY = '/home/certificates/webhook_pkey.pem'
bot.set_webhhook(WEBHOOK_HOST, open('r', PKEM))
"""
if __name__ == '__main__':
    bot.polling()
