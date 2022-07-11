import os # operating system


products = []
# 確認檔案
if os.path.isfile('products.csv'):
    print('yeah! 有耶!')
    # 讀取檔案
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #繼續
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

else:
    print('找不到檔案...')
    
#使用者輸入
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
#印出購買紀錄
for p in products:
	print(p[0], '的價格是 ', p[1], '元')
#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')