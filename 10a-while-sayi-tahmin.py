sayi=78 #Tahmin edilecek sayı
sayac=1

while True:
  tahmin=int(input("0-100 arası bir sayı tahmin et? "))

  if tahmin>sayi:
    print("Daha küçük bir sayı tahmin et!")
    
  elif tahmin<sayi:
    print("Daha büyük bir sayı tahmin et!")
    
  else:
    print("Bravooo!!!",sayac,"defada bildin")
    break
    
  sayac+=1

print("Oyun bitti")