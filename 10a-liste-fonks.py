# Listelere ait Fonksiyonlar
harf=["a","b","c","d","e","f","g","h"]
# liste_adi.fonksiyon(parametre)

# append() - Listenin en sonuna eleman ekler. Parametre olarak elemanın kendisi yazılır
harf.append("k")
print(harf)

# remove() - Listeden eleman siler. Parametre olarak silinecek elemanın kendisi yazılır
harf.remove("d")
print(harf)

# del ve pop() - Listeden eleman siler. Parametre olarak silinecek elemanın index numarası yazılır
harf.pop(0)
del harf[0]
print(harf)

# reverse() - Liste elemanların sırasını tersine çevirir. Parametresi yoktur.
harf.reverse()
print(harf)

# sort() - Alfabetik (sayılarıda küçükten büyüğe) olarak sıralar.Parametre yoktur.
harf.sort()
print(harf)

sayi=[1,8,9,3,6,9,0,-12]
sayi.sort()
sayi.reverse()
print(sayi)

# index() - Listede arama yaparak index numarasını verir. Parametre olarak elamanın kendisi yazılır
harf.index("h") #4
print(harf.index("h"))

# count() - Listede aranan verinin adedini gösterir
harf.append("h")
print(harf)
print(harf.count("h"))

# list() - Karakter veri tipindeki bir veriyi listeye dönüştürür.

s=list("13651668927970595634537636453")
s.sort()
print(s)

#len - Listenin eleman sayısını verir.
print(len(s))

for x in range(0,len(s)):
  print(int(s[x]),end=" ")






