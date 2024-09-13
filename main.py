actualprice = 100
sellprice = 200
#formula
profit = sellprice - actualprice
loss = actualprice - sellprice
#conditions
if(sellprice>actualprice):
    print("The profit is",profit)
else:
    print("The Loss is",loss)