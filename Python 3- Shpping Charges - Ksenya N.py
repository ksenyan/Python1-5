
shipping =False
print ("""Welcome to online shopping! We have a few offers for you today:
Ceramic mug: $35
One fork: $15
Dishwasher: $500 """)
mug = input("Would you like to purchase the ceramic mug? ")
fork= input("Would you like to purchase the single fork? ")
dishwasher = input("Would you like to purchase the dishwasher? ")
price = int(0)

if mug.lower() == "yes" :
    price = (price+35)
if fork.lower() == "yes" :
    price = (price+15)
if dishwasher.lower() == "yes" :
    price = (price+500)
if price == (0) :
    print("Your cart is empty!!")
    
if price < (50) :
    price = (price + 10)
    print ("We charge $10 for shipping because your total is under $50.")
else :
    print ("Shipping is free!")
price = ("%.2f" % price)
print ("Your final cost is "+"$"+str(price))
print ("Thank you for choosing us!")
print("Your package will be here in 5 months!")
    
