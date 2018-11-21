import json


def write_order_to_json(item, quantity, price, buyer, date):
    add_data = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    try:
        with open('orders.json', 'r') as f:
            data = json.loads(f.read())
            data['data'].append(add_data)
    except FileNotFoundError:
        data = {'data': [add_data]}
    with open('orders.json', 'w') as f:
        f.write(json.dumps(data, indent=4))


write_order_to_json('Toys', 11, 565, 'HNM', '11.01.18')
