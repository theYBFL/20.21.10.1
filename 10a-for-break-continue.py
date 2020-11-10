#break - continue arasındaki fark

for i in range(1,6):
  if i==2 or i==4:
    continue #döngüyü burada keser ve dönügünün başına döner
  print(i)

print()

for i in range(1,6):
  if i==2 or i==4:
    break #döngüyü burada sonlandırır
  print(i)