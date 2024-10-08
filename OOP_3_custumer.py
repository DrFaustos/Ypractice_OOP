class Customer:
    def __init__(self, name):
        self.name = name
        self.__discount = 10  # Приватный атрибут с значением по умолчанию 10

    def get_price(self, original_price):
        # Вычисляем новую цену с учетом скидки
        discounted_price = original_price * (1 - self.__discount / 100)
        return round(discounted_price, 2)

    def set_discount(self, new_discount):
        # Проверяем, чтобы скидка не превышала 80%
        if new_discount > 80:
            self.__discount = 80
        else:
            self.__discount = new_discount


# Примеры использования
customer = Customer("Иван Иванович")

print(customer.get_price(100))  # Исходная цена с темой скидки 10%
customer.set_discount(20)
print(customer.get_price(100))  # Новая цена с скидкой 20%
customer.set_discount(90)  # Скидка больше 80%, будет установлена в 80
print(customer.get_price(100))  # Новая цена с максимальной скидкой 80%
