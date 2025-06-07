#task 1
a=[1,2,3,4]
b=sum(a)
print(b)

#task2

a=[1,2,3,4]
b=min(a)
print(b)

#task3

nums=[1,2,3,4,5,6]
print(nums[::-1])

 #task4

nums=[1,2,3,4,5,6]
for i in nums:
  if i%2!=0:
    print(i)

#task5
number=int(input("Enter a number:"))
a=[1,2,3,4,5,6]
for i in a:
  multip=i*number
  print(multip)

#task2.1

a=[1,2,3,4,5,6,7]
x=int(input("Введіть число:"))
new_list=[]
for i in a:
  if i>x:
    new_list.append(i)
print(new_list)


#task2.2

a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
  if i>0:
    average=sum(a)/len(a)
print(average)

#task2.3

a=[1,2,3,4,5,6,7,8,9,10]
list1=[]
number=int(input("Введіть число зі списку:"))
for i in a:
  if i<number:
    list1.append(i)
print(max(list1))

#task2.4

a=[1,2,3,4,5,6,7,8,9,10]
y=int(input("Введіть число :"))
total=0
for i in a:
  if i%y==0:
    total+=i
else:
  if total==0:
    print("Число не є дільником у")
  else:
    print(total)

#task2.5

a=[1,2,3,4,5,6,7,8,9]
degree2=[]
for i in a:
  kvadrat=i**2
  degree2.append(kvadrat)
print(degree2)

#task2.6
a=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4]
dodatni=[]
for i in a:
  if i>0:
    dodatni.append(i)
print(dodatni)

#task2.7

words=["deactivate", "eliminate", "decode","importer", "deduct", "think"]
filtered=[]
for word in words:
  if word.startswith('de'):
    filtered.append(word)
print(filtered)
#Використала метод startswith, який знайшла в інтернеті, який повертає True or False

#task2.8

n=int(input("Введіть кількість чисел для обчислення суми:"))
a=[1,2,3,4,5,6,7,8,9]
kilkist=len(a)
if n>kilkist or n==0 or n<0:
  print("Оберіть іншу кількість чисел")
else:
  numbers=a[:n]
  suma=sum(numbers)
print(suma)

#task2.9

words=["text","mom", "cat", "dad"]
for i in words:
  new=i[::-1]
  if i==new:
    print(f"Слово {i} є паліндромом")

#task2.10

a=[1,2,3,4,5,6,7,8,9]
b=[]
n=int(input("Введіть число для перевірки на подільність"))
for i in a:
  znachennya= i%n==0
  b.append(znachennya)
print(b)

#task3.1
a=[1,2,3,4,5,6,7,8,9,10]
x=int(input("Введіть число Х:"))
y=int(input("Введіть число У:"))
new_list=[]
for i in a:
  if i%x==0 and i%y!=0:
    new_list.append(i)
print(new_list)

#task3.2

list1=[[1,2],[3,4],[5,6]]
final_list=[]
for list2 in list1:
  for list3 in list2:
    final_list.append(list3)
print(final_list)

#task3.3

words="Hello. My name is Anton"
task=""
for i in words:
  if i.isupper()==True:
    task=task+i
print(task)
#Знайшла інформацію про роботу з рядками та метод для перевірки на великі літери isupper в інтернеті

#task3.4

numbers=[1,2,3,3,4,4,4,4,5,5,6,6,6,7,8,9,9,9]
chastota={}
for i in numbers:
  if i in chastota:
    chastota[i]+=1
  else:
    chastota[i]=1
list1=[]
for number, count in chastota.items():
  list1.extend([number]*count)
list1.sort(reverse=True)
print(list1)

# """Task 3.5"""

a=[1,2,3,4,5]
b=[6,7,8,9,10]
final_list=[]
for i in a:
  if i%2==0:
    final_list.append(i)
for i in b:
  if i%3==0:
    final_list.append(i)
print(final_list)

#task3.6

slovnyk={"monday":10,"tuesday":20,"wednesday":30}
total=0
for i in slovnyk:
  total=total+slovnyk[i]
print(total)

# """Task 3.7"""

a=[1,2,3,4,5,6,7,8,9]
for i in range(len(a)):
  if a[i]<=2:
    a[i]=3
print(a)

# """Task 3.8"""

a=["car","dedicate", "museum", "coffee"]
x=(input("Введіть cлово:"))
total=0
for i in a:
  if len(i)>len(x):
    total+=1
print(total)

# """Task 3.9"""

a=["cat","dog","monkey"]
b=[1,2,3]
new_list=[]
for i in range(0,len(a)):
  new_list.append(a[i])
for i in range(0,len(b)):
  new_list.append(b[i])
print(new_list)

# """Task 3.10"""

nums=[1,2,3,4,5,6,7,8,9]
x=int(input("Введіть число Х:"))
y=int(input("Введіть число Y:"))
for i in range(len(nums)):
  if nums[i]>x:
    nums[i]=nums[i]*y
print(nums)