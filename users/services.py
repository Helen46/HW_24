import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(course_name):
    """Создает продукт в stripe"""

    print(stripe.api_key)
    print(STRIPE_API_KEY)

    return stripe.Product.create(name=course_name)


def create_stripe_price(product, amount):
    """Создает цену в stripe"""
    return stripe.Price.create(
        product=product.get("id"),
        currency="rub",
        unit_amount=int(amount) * 100,
    )


def create_stripe_session(price):
    """Создает сессию в stripe"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/course/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


# def convert_rub_to_dollars(payment_sum):
#     """ Конвертирует рубли в доллары """
#
#     c = CurrencyRates()
#     rate = c.get_rate('RUB', 'USD')
#     return int(payment_sum * rate)
