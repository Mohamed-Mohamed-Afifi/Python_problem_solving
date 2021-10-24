fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}
print(fruitPrices['apples'])
orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
def buyLotsOfFruit(orderList):
    sum=0;
    for num in orderList:
        sum +=num[1]*fruitPrices[num[0]]
    return sum;

print("cost Of",orderList,"is",buyLotsOfFruit(orderList))