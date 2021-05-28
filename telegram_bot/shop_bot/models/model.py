from mongoengine import *
connect('shop')


class User(Document):
    STATES = (
        ('products', 'products'),
        ('categories', 'categories')
    )

    telegram_id = StringField(max_length=32, required=True, unique=True)
    username = StringField(max_length=128)
    first_name = StringField(max_length=64)
    last_name = StringField(max_length=64)
    phone_number = StringField(max_length=20)
    state = StringField(choices=STATES)
    email = EmailField()
    step = IntField(max_length=10, default=0)
    city = StringField(max_length=32)
    np = StringField(max_length=128)

    @classmethod
    def create_user(cls, user_id, username):
        try:
            cls.objects.create(telegram_id=user_id, username=username)
        except Exception as e:
            print('User')

    @classmethod
    def get_user(cls, user_id):
        return cls.objects.get(telegram_id=user_id)

    @classmethod
    def update_user(cls, user_id, **kwargs):
        user = cls.get_user(user_id)
        user.update(**kwargs)

    @classmethod
    def set_step_checkout(cls, user_id, step):
        user = cls.get_user(user_id)
        user.step = step
        user.save()

    @classmethod
    def get_step(cls, user_id):
        user = cls.get_user(user_id)
        return user.step


class Cart(Document):
    user = ReferenceField(User)
    is_archived = BooleanField(default=False)

    @classmethod
    def get_or_create_cart(cls, user_id):
        user = User.objects.get(telegram_id=user_id)
        cart = cls.objects.filter(user=user, is_archived=False)

        if not cart:
            cart = cls.objects.create(user=user)
        return cart

    @classmethod
    def archive_cart(cls, user_id):
        cart = cls.get_cart(user_id)
        cart.is_archived = True
        cart.save()

    @classmethod
    def get_archive_cart(cls, user_id):
        user = User.objects.get(telegram_id=user_id)
        return cls.objects.filter(user=user, is_archived=True)

    @classmethod
    def get_archive_cart_by_id(cls, user_id, id_cart):
        user = User.objects.get(telegram_id=user_id)
        return cls.objects.get(user=user, id=id_cart, is_archived=True)

    @classmethod
    def get_cart(cls, user_id):
        user = User.objects.get(telegram_id=user_id)
        return cls.objects.get(user=user, is_archived=False)

    def get_cart_products(self):
        return CartProduct.objects.filter(cart=self)

    def add_product_to_cart(self, product_id):
        CartProduct.objects.create(
            cart=self,
            product=Product.get_product(id=product_id)
        )

    def delete_product_from_cart(self, product):
        CartProduct.objects.filter(
            cart=self,
            product=product
        ).first().delete()


class CartProduct(Document):
    cart = ReferenceField(Cart)
    product = ReferenceField('Product')


class Attributes(EmbeddedDocument):
    height = FloatField()
    weight = FloatField()
    width = FloatField()


class Category(Document):
    title = StringField(min_length=1, max_length=255, required=True)
    subcategories = ListField(ReferenceField('self'))
    parent = ReferenceField('self')
    is_root = BooleanField(default=False)
    description = StringField(max_length=4096)

    def is_parent(self):
        return bool(self.parent)

    def add_subcategory(self, cat_obj):
        cat_obj.parent = self
        cat_obj.save()

        self.subcategories.append(cat_obj)
        self.save()

    @classmethod
    def create(cls, **kwargs):
        kwargs['subcategories'] = []
        if kwargs.get('parent') == True:
            kwargs['is_root'] = False

        return cls(**kwargs).save()

    def get_products(self):
        return Product.objects.filter(
            category=self
        )

    def __str__(self):
        return self.title


class Product(Document):
    title = StringField(min_length=1, max_length=255, required=True)
    article = StringField(max_length=32, required=True)
    description = StringField(max_length=8192)
    image = StringField(required=True)
    price = IntField(min_value=1, required=True)
    in_stock = IntField(min_value=0, default=0)
    discount_price = IntField(min_value=1)
    attributes = EmbeddedDocumentField(Attributes)
    extra_data = StringField(max_length=4096)
    category = ReferenceField(Category, required=True)

    @classmethod
    def get_product(cls, **kwargs):
        return cls.objects.get(**kwargs)

    def get_price(self):
        return self.price if not self.discount_price else self.discount_price
