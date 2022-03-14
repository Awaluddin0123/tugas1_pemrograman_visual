print("Perhitungan Aritmatika")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("==================================")
P = int(input("Masukkan Pilihan (1/2/3/4):"))
bp = int(input("Masukkan Angka Pertama :"))
bk = int(input("Masukkan Angka Kedua :"))

if P == 1:
    jlh = bp+bk
    print(bp,"+",bk,"=",jlh)

elif P == 2:
    krg = bp-bk
    print(bp,"-",bk,"=",krg)

elif P == 3:
    kali = bp*bk
    print(bp,"*",bk,"=",kali)

elif P == 4:
    bagi = bp/bk
    print(bp,"/",bk,"=",bagi)    

else :
    print("Gagal")