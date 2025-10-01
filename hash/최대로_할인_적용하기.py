price = [30000, 2000, 1500000]
coupon = [20,40]

price.sort(reverse=True)
coupon.sort(reverse=True)

price_index =0
coupon_index = 0
max_discounted_price =0

while price_index < len(price) and coupon_index < len(coupon):
    discount_price =price[price_index] * (100 - coupon[coupon_index]) // 100
    max_discounted_price += discount_price
    price_index += 1
    coupon_index += 1

while price_index < len(price):
    max_discounted_price += price[price_index]
    price_index += 1


print(max_discounted_price)