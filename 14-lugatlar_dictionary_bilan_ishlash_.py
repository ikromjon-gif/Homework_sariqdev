# -*- coding: utf-8 -*-


# 14-DARS DICTIONRY/LUGATLAR bilan ishlash
# HOMEWORK


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
tyil = otam['tyil']
vil = otam['viloyat']
print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa"
    }

taom = taomlar['ali']
print(f"Alining sevimli taomi {taom}")
print(f'Hasanning sevimli taomi {taomlar["hasan"]}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# PYTHON IZOHLI LUGATI

python={
    "int":"butunsonlar bilan ishlash",
    'float':'onlik sonlar bilan ishlash',
    'string':'matnlar bilan ishlash',
    'lower()':"matnlarni kichik harf qilib beradi",
    'upper()':'matnlarni katta harf bilan yozadi',
    'title()':'matnlarni bosh harifini katta bilan yozadi',
    'for':'takrorlanish aperatori',
    'if':'shart va tarmoqlnish operatori',
    'list':'royxatlar bilan ishlash',
    'tuple':'ozgarmas royxat ',
    'del':'elementni ochirish',
    'range':'malum oraliqda sonlarni shakllantirish',
    'reverse':'qiymatni teskarisiga chiqarish',
    '0:5':'oraliqdagi qiymatlarni olish',
       }

kalit=input('iltimos kalit sozni kiriting>>>>>').lower()
##print(f" {python.get (kalit,'bunday kalit soz royxatda yoq')}")

tarjima=python.get(kalit)
if tarjima==None:
  print(f'uzur bunday kalit soz yoq,boshqasini kiriting!')
else:
  print (f'vazifasi: {tarjima} ')

