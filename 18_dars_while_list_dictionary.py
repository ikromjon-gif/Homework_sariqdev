# -*- coding: utf-8 -*-
"""18- dars WHILE /LIST /DICTIONARY.ipynb


# 18- DARS WHILE-bilan birgalikda lugat va list yordamida ishlash

# yaqin dostlaringiz royxatini tuzing
dostlar=[]
n=1
while True:
  savol=f'\n{n} chi Yaqin dostingiz ismini kiriting '
  dosm=input(savol)
  dostlar.append(dosm)
  takrorlash=input('yana ism qo`shamizmi (ha/yoq)?')
  n+=1
  if takrorlash!='ha':
    break
print('\nDostlaringiz royxati:')
for ism in dostlar:
  print(ism.title())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dostlar malumotlarini kiritadigan lugat qiling

dostlar={}
n=1
ishora=True
while ishora:
    ism=input(f'\n{n} dostingizni ismini kirirting ')
    yosh=input('dostingizni yoshini kiriting ')
    dostlar[ism]=yosh
    takrorlash=input('yana dostingiz qoshasizmi (ha/yoq)? ')
    n+=1
    if takrorlash!='ha':
      break
for ism,yosh in dostlar.items():
  print(f'\n{ism.title()}  {yosh} yoshda')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
mashinalar royxatidan bir xil elementni o`chirish

cars=['soueast_s09','kia sportage','soueast_s09','nexia','damas','hyundai']
while 'soueast_s09' in cars:
  cars.remove('soueast_s09')

print(cars)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
talabalar =['asqar','sanjar','bekzod','gulom','qamar']
ustozbaho={}
while talabalar:
  talaba=talabalar.pop()5
  baho=input(f'iltimos {talaba.title()} ni bahosini kiriting bahosini kiriting>>>')
  ustozbaho[talaba]=baho
print(ustozbaho.items())


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# HOME WORK

1.Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
buyurtmalar=[]
while True:
  mahsulot=input(f' \nDasturni yakunlash uchun "exit" YOZING!\nMahsulot nomini kirirting >>>>')
  if mahsulot=='exit':
     break
  buyurtmalar.append((mahsulot))
print('\nSizning buyutmangiz quyidagilar:')
for n in buyurtmalar:
  print( f'{n.title()}')


# 2.e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

royxat={}
while True:
  nomi=input('\niltimos mahsulot Nomini kiriting >>>')
  narxi=input('iltimos mahsulot Narxini kiriting >>')
  takrorlash=input('yana Mahsulot kiritasizmi (ha/yoq)?')
  royxat[nomi]=narxi
  if takrorlash!='ha':
    break
print('\nSiz kiritgan tovarlar royxati :\n')
for m,n in royxat.items():
  print(f'{m.title()}ni narxi {n} sum')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 3-Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

mahsulotlar=['anor','olcha','gilos','behi','sabzi','tuxum','kakat']
royxat={}
while True:
  nomi=input('\niltimos mahsulot Nomini kiriting >>>')
  narxi=input('iltimos mahsulot Narxini kiriting >>')
  takrorlash=input('yana Mahsulot kiritasizmi (ha/yoq)?')
  royxat[nomi]=narxi
  if takrorlash!='ha':
    break
print('\nSiz kiritgan tovarlar royxati :\n')

for mahs in mahsulotlar:
   if mahs in royxat:
      print(f'{mahs} ning narxi {royxat[mahs]} sum ')
   else:
      print(f'{mahs} bozorda yoq')

