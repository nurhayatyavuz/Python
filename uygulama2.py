
#3 basamaklı sayılardan rakamlarının kütlerinin toplamına eşit olanları bulma 

liste= []
for sayi in range(100,1000):
    toplam = 0
    gecici_sayi= sayi
    while gecici_sayi!= 0:
        basamak=gecici_sayi%10
        toplam += basamak ** 3
        gecici_sayi //= 10
    if toplam==sayi:
        liste.append(sayi)

print(liste)
