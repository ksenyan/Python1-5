empty = False
shipping = False
print ("""Welcome to online shopping! All shipping here is free.
We definitely didn't include it in the price. We have a few offers for you today:
Ceramic mug: $25
One fork: $10
Dishwasher: $500 """)
mug = input("Would you like to purchase the ceramic mug? ")
fork= input("Would you like to purchase the single fork? ")
dishwasher = input("Would you like to purchase the dishwasher? ")
price = float(0)
totalCost = float(0)
totalCost = ("%.2f" % totalCost)
if mug.lower() == "yes" :
    price = (price+25)
if fork.lower() == "yes" :
    price = (price+10)
if dishwasher.lower() == "yes" :
    price = (price+500)
if price == (0) :
    print("Your cart is empty!!")
    empty = True
totalCost = price
if not empty :
    price = float(price)
    country =input("Are you in Canada? ").lower()
    if country == "yes" :
        province = input("Which province are you in? ").lower()
    if country == "yes" and (province == "alberta") :
        totalCost = price
        totalCost = float(price*1.05)
        print ("Your province charges 5% tax.")        
    if country == "yes" and \
    (province == ("ontario" or "new brunswick" or "nova scotia")) :
        totalCost = price
        totalCost = float(price*1.13)
        print ("Your province charges 13% tax.")
    if not country == "yes" :
        totalCost = price
        print("Your country does not charge tax.")
    if country == "yes" and \
    (province != "ontario" and province != "new brunswick" \
    and province != "nova scotia" and province != "alberta") :
        totalCost = price
        totalCost = float(price*1.11)
        print ("Your province charges 11% tax.")
  
           
    totalCost = ("%.2f" % totalCost)   
    print ("Your final cost is "+"$"+str(totalCost))
    print ("Thank you for choosing us!")
    print("Your package will be here in 5 months!")
    
