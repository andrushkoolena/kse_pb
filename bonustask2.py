total_sum=0
while True:
  salary=float(input("Введіть ваш місячний дохід або '0' для виходу:"))
  if salary==0:
    break
  elif salary<0:
    print("Дохід не може бути від'ємним")
    continue
  else: 
    total_sum=total_sum+salary
    print("Ваш дохід збережено:", total_sum)