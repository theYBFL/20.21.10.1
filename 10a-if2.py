k_adi=input("Kullanıcı adınız giriniz: ")
parola=input("parolanızı giriniz: ")

#and or not

if k_adi=="patron" and parola=="12345":
  print("Hoşgeldin patron...")
  print("Ana sayfaya yönlendiriliyorsunuz")
else:
  print("Kullanıcı adınız veya parolanız yanlış")
  print("Tekrar deneyiniz.")


x=5
y=4

if not x>y:
  print("küçük ya da eşit")
else:
  print("büyük")