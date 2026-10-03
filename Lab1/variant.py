order_name = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")

item1_name = "Упаковки корма"
print(f"\nПозиция 1: {item1_name}")
item1_count = int(input("Введите количество: "))
item1_price = float(input("Введите цену за единицу (руб.): "))

item2_name = "Игрушки"
print(f"\nПозиция 2: {item2_name}")
item2_count = int(input("Введите количество: "))
item2_price = float(input("Введите цену за единицу (руб.): "))

print("\nДоставка и оплата")
# Добавлен запрос скидки
discount_percent = float(input("Введите скидку на товары (в % от 0 до 100): "))
delivery_cost = float(input("Введите стоимость доставки (руб.): "))
money_paid = float(input("Введите внесенную сумму (руб.): "))

item1_cost = item1_count * item1_price
item2_cost = item2_count * item2_price

# Расчет стоимости товаров до скидки
goods_cost_raw = item1_cost + item2_cost

# Расчет скидки (применяется только к стоимости товаров)
discount_rub = goods_cost_raw * (discount_percent / 100)
goods_cost = goods_cost_raw - discount_rub

# Итоговая сумма с учетом скидки на товары и стоимости доставки
total_cost = goods_cost + delivery_cost
total_count = item1_count + item2_count
change = money_paid - total_cost

print("\n" + "="*40)
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer_name}")
print("="*40)

print(f"{item1_name} | {item1_count} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_count} | {item2_price:.2f} | {item2_cost:.2f}")
print("-"*40)

# Обновленный блок итогов с выводом скидки
print(f"Стоимость товаров без скидки: {goods_cost_raw:.2f} руб.")
print(f"Скидка ({discount_percent:.1f}%): {discount_rub:.2f} руб.")
print(f"Стоимость товаров со скидкой: {goods_cost:.2f} руб.")
print(f"Стоимость доставки: {delivery_cost:.2f} руб.")
print(f"Общее количество единиц: {total_count} шт.")
print("-"*40)
print(f"Общая сумма с доставкой: {total_cost:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
print("="*40)
