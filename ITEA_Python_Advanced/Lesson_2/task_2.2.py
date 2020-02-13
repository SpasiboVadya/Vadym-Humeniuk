from random import randint


class Store:

    sold_at_all_stores = 0

    def __init__(self, name, store_sale):
        self._name = name
        self._store_sale = store_sale
        Store.sold_at_all_stores += store_sale

    def raise_sales(self, add_sale):
        self._store_sale += add_sale
        Store.sold_at_all_stores += add_sale


Store1 = Store('Apple Store', 100)
Store1.raise_sales(randint(1, 50))
print(Store1)

Store2 = Store('StarBucks', 1000)
Store2.raise_sales(randint(10, 100))
print(Store2)

Store3 = Store('Adidas', 500)
Store3.raise_sales(randint(5, 50))
print(Store3)

print(Store.sold_at_all_stores)