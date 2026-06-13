# discount module

TAX_RATE = 0.13

# apply discount
def apply_discount(price, percent):

    return price - (price * percent / 100)

# apply VAT
def apply_tax(price):

    return price + (price * TAX_RATE)

# final price after discount and tax
def final_price(price, discount_pct):

    discounted = apply_discount(price, discount_pct)

    return apply_tax(discounted)