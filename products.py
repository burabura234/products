products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    p = []
    p.append(name)
    p.append(price)
#    上三行可簡寫為
#   p = [name, price]
    products.append(p)
#   products.append(p) 可以直接簡寫為 [name, price]就不用p了
print(products)
for p in products:
	print(p[0], '的價格是 ', p[1], '元')
print(products[0][1])