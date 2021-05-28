from telebot import TeleBot
from telebot.types import \
    InlineKeyboardMarkup,\
    InlineKeyboardButton, \
    InlineQueryResultArticle, \
    InputTextMessageContent, \
    ReplyKeyboardMarkup, \
    KeyboardButton

from config import TOKEN, MANAGER_ID
from models.model import Category, Product, User, Cart
from keyboards import START_KB


bot = TeleBot(token=TOKEN)


class TGBot(TeleBot):

    def __init__(self, token, *args):
        super().__init__(token, *args)

    def send_categories(self, user_id, callback_lookup='category', force_send=True):
        category = Category.objects.filter(is_root=True)

        kb = InlineKeyboardMarkup()
        buttons = [
            InlineKeyboardButton(text=cat.title, callback_data=f'{callback_lookup}_{str(cat.id)}')for cat in category
        ]
        kb.add(*buttons)
        if not force_send:
            return kb
        self.send_message(user_id, text='Выберите категорию', reply_markup=kb)

    def subcategories_or_products(self,
                                  category_id,
                                  message_id,
                                  user_id=None,
                                  text=None,
                                  category_lookup='category',
                                  product_lookup='product',
                                  force_send=True):

        if not (all([user_id, text])) and force_send:
            raise Exception('Force send cannot be used without user_id or text')

        # Берем категорию
        category = Category.objects.get(id=category_id)

        kb = InlineKeyboardMarkup(row_width=2)

        # Проверяем есть ли у категории Под категории
        if category.subcategories:

            # Проверяем все подкатегории нашей Категории
            for cat in category.subcategories:

                # Если у нашей под категории есть еще подкатегории.
                # Создаем Inline кнопки в сообщении
                if cat.subcategories:
                    buttons = [
                        InlineKeyboardButton(text=cat.title, callback_data=f'{category_lookup}_{cat.id}')
                        for cat in category.subcategories
                    ]

                    # back = InlineKeyboardButton(text='Назад', callback_data=f'{category_lookup}_{category.id}')
                    # buttons.append(back)

                # Иначе будем отправлять кнопки с switch_inline_query_current_chat
                else:
                    buttons = [
                        InlineKeyboardButton(text=cat.title,
                                             switch_inline_query_current_chat=f'{category_lookup}_{cat.id}') for
                        cat in category.subcategories
                    ]

                    # back = InlineKeyboardButton(text='Назад', callback_data=f'{category_lookup}_{category_id}')
                    # buttons.append(back)

            # Добавляем все созданные кнопки
            kb.add(*buttons)

            self.edit_message_text(category.title, message_id=message_id, chat_id=user_id, reply_markup=kb)

        else:
            results = []

            for product in category.get_products():

                kb = InlineKeyboardMarkup()

                button = InlineKeyboardButton(text='Добавить в корзину',
                                              callback_data=f'{product_lookup}_{product.id}')

                kb.add(button)
                result1 = InlineQueryResultArticle(
                    id=str(product.id),
                    title=product.title,
                    description=product.description,
                    thumb_url=product.image,
                    reply_markup=kb,

                    input_message_content=InputTextMessageContent(
                        parse_mode='HTML',
                        disable_web_page_preview=False,
                        message_text=f"{product.title} \n{product.description} <a href='{product.image}'>&#8204</a>"
                    )

                )
                results.append(result1)

            self.answer_inline_query(message_id, results, cache_time=0)

    def show_cart(self, user_id, del_product_lookup='del'):

        cart = Cart.get_cart(user_id)

        cart_product = cart.get_cart_products()

        item_f = cart_product.item_frequencies('product')

        kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        b2 = [KeyboardButton('Оформить заказ')]
        kb2.add(*b2)

        if item_f:

            for product_id, s in item_f.items():

                product = Product.get_product(id=product_id)

                text = (f'{product.title} \n'
                        f'{product.description} \n'
                        f'{product.category.title}\n'
                        f'{product.image}\n'
                        f'Количество: {s}')

                kb = InlineKeyboardMarkup(row_width=1)

                buttons = [
                    InlineKeyboardButton(text='Удалить товар с корзины',
                                         callback_data=f'{del_product_lookup}_{product.id}')
                ]

                kb.add(*buttons)

                self.send_message(user_id, text, reply_markup=kb)

            self.send_message(user_id, 'Чтобы купить нажмите на кнопку "Оформить заказ"', reply_markup=kb2)
        else:

            self.send_message(user_id, 'Ваша корзина пуста')

    def del_product_from_cart(self, prod_id, message_id, user_id):

        cart = Cart.get_cart(user_id)
        cart.delete_product_from_cart(prod_id)

        self.answer_callback_query(message_id, "Товар удален", show_alert=True)

        self.show_cart(user_id)

    def checkout_step_1(self, user_id):

        User.set_step_checkout(user_id, 1)

        self.send_message(user_id, 'Введите ваше Имя')

    def checkout_step_2(self, user_id, response_first_name):

        User.update_user(user_id, first_name=response_first_name)
        User.set_step_checkout(user_id, 2)

        self.send_message(user_id, 'Введите вашу Фамилию')

    def checkout_step_3(self, user_id, response_last_name):

        User.update_user(user_id, last_name=response_last_name)
        User.set_step_checkout(user_id, 3)

        self.send_message(user_id, 'Введите ваш номер')

    def checkout_step_4(self, user_id, response_phone):

        User.update_user(user_id, phone_number=response_phone)
        self.send_message(user_id, 'Введите ваш Город')
        User.set_step_checkout(user_id, 4)

    def checkout_step_5(self, user_id, response_city):

        User.update_user(user_id, city=response_city)
        self.send_message(user_id, 'Введите отделение Новой почты или самовывоз?\n'
                                   'Самовывоз возжможен только из Киева по адресу:\n Киев, ул. Крещатик 46A')
        User.set_step_checkout(user_id, 5)

    def checkout_step_6(self, user_id, response_np):

        User.update_user(user_id, np=response_np)
        User.set_step_checkout(user_id, 6)

        # For Test
        user = User.get_user(user_id)

        message = (f'Вот что вы ввели \n'
                   f'Имя: {user.first_name} \n'
                   f'Фамилия: {user.last_name} \n'
                   f'Номер: {user.phone_number} \n'
                   f'Город: {user.city}\n'
                   f'Отделение новой почты{user.np}\n'
                   )
        self.send_message(user_id, 'Заказ оформлен. С вами свяжется наш Менеджер')

        start_kb = ReplyKeyboardMarkup()
        buttons = [KeyboardButton(button_name) for button_name in START_KB.values()]
        start_kb.add(*buttons)
        self.send_message(user_id, message, reply_markup=start_kb)

        # Отправка менеджеру
        message_for_manager = (f'Имя: {user.first_name} \n'
                               f'Фамилия: {user.last_name} \n'
                               f'Номер: {user.phone_number} \n'
                               f'Город: {user.city}\n'
                               f'Отделение новой почты: {user.np}\n'
                               f'username: {user.username}\n'
                               )

        self.send_message(manager_id, f'У тебя заказ от\n{message_for_manager}')

        cart = Cart.get_cart(user_id)

        cart_product = cart.get_cart_products()

        item_f = cart_product.item_frequencies('product')

        if item_f:

            for product_id, s in item_f.items():

                product = Product.get_product(id=product_id)

                text = (f'{product.title} \n'
                        f'{product.description} \n'
                        f'{product.category.title}\n'
                        f'{product.image}\n'
                        f'Количество: {s}')

                kb = InlineKeyboardMarkup(row_width=1)

                self.send_message(user_id, text, reply_markup=kb)

            manager_id = MANAGER_ID
            self.send_message(manager_id)

            Cart.archive_cart(user_id)
            Cart.get_or_create_cart(user_id)
