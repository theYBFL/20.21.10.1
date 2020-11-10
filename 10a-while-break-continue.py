### while döngüsünde break-continue kullanımı ###
#break - Döngü break ifadesinin olduğu yerde sonlanır ve döngünün dışına çıkılır.
#continue - Döngü continue ifadesinin olduğu yerde kesilir ve döngünün başına dönülür.

while True:
  print("""
  1-Para çekme
  2-Para yatırma
  3-Fatura ödeme
  0-Çıkış
  """)
  secim=input("Seçiminiz ")
  if secim=="1":
    print("Paranızı çekiniz")
  elif secim=="2":
    print("Paranızı yatırınız")
  elif secim=="3":
    print("Faturanızı ödeyiniz")
  elif secim=="0":
    print("Güle güle")
    break
  else:
    print("Tekrar deneyiniz.")


  