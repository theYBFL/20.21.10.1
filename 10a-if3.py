#0-50 1
#50-60 2
#60-70 3
#70-85 4
#85-100 5

n1=int(input("1.not "))
n2=int(input("2.not "))
ort=(n1+n2)/2 #90 - 0-100

print(ort)

if ort>0 and ort<50:
  print("1")
elif ort>=50 and ort<60:
  print("2")
elif ort>=60 and ort<70:
  print("3")
elif ort>=70 and ort<85:
  print("4")
else:
  print("5")