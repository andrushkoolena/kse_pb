import task1
print(task1.rectangle_area(4,6))

import taxes
revenue=15000
tax1=taxes.calculate_vat(revenue)
tax2=taxes.calculate_income_tax(revenue)
together=tax1+tax2
print(together)

import math
korin=math.sqrt(121)
sinusik=math.sin(math.pi/2)
vnyz=math.floor(7.8)
vverh=math.ceil(7.8)
print(korin,sinusik,vnyz,vverh)

import random
kydok1=random.randint(1,6)
kydok2=random.randint(1,6)
suma=kydok1+kydok2
print(kydok1,kydok2,suma)



balans=10000
krok=100
total=0
history=[]
while balans>=100 and total<1000:
    total+=1
    rnumb=random.randint(1,37)
    chosennumb=random.randint(1,37)
    if rnumb==chosennumb:
        balans=balans+36*krok
    else:
        balans=balans-100
    history=history.append(balans)
import matplotlib.pyplot as plt
plt.plot(balans)




    



