# coding: utf-8
from layer_native import *


apple     = 100
apple_num = 2
tax       = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# forward
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

# backward
d_price = 1
d_apple_price, d_tax = mul_tax_layer.backward(d_price)
d_apple, d_apple_num = mul_apple_layer.backward(d_apple_price)

print('price:', int(price))
print('d_apple:', d_apple)
print('d_apple_num:', int(d_apple_num))
print('d_tax:', d_tax)
