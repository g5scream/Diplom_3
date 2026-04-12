def create_order(page):  # Создаёт заказ и возвращает его номер с префиксом '0'
    page.add_ingredients()
    page.place_order()
    number = page.get_order_number()
    if not number.startswith('0'):
        number = '0' + number
    page.close_order_modal()
    return number