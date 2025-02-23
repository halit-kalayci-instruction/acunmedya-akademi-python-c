# Programlama nedir?
# Python
print("Hello World!")  
# string => metinsel veri.

# değişkenler
# python type-safe (tip güvenilir) değildir.
age = 50 #int-integer
# geçici hafızada (ram) age ismine 50 değeri olduğunu atadım.
print(age)

age = 25 #int-integer
print(age)
print( type(age) )


age = "Merhaba" #str-string
print(age)
# c#-java type safe
# python-js type safe değil

print( type(age) )

# operatörler

# aritmetik operatörler (matematiksel işlem)
print(1+1)  #2 int
print(5-1) #4 int
print(5*2) #10 int
print(25/5) #5.0 float,double,decimal
print(25//5) #5 int
print(104//5) # 20,8 => çift olduğu için aşağıya yuvarlar => 20
print(5**3) # 5üssü3 => 125
print(100%3) #1 => mod operatör
#

# atama operatörleri

name = "Halit"
number = 50
number += 10 # number = number + 10
number -= 5 # number = number - 5
print(number)

number2 = 5
number2 **= 3 # number2 = number2 ** 3
print(number2)
#

# bool, boolean => 2 değere sahiptir -> True,False

# karşılaştırma operatörleri
print(1 == 1) #ben sol taraf ile sağ tarafın eşit olmasını istiyorum ==
print(1 == 2)
print(10 > 5)
print(10 >= 10)
print(10 <= 10)
print( 1 != 2 )

#genelde stringlerde bu operatörler tercih edilmez.
# < > <= >= -> Sözlük Sırasına göre UNICODE değerine göre sıralanır.
print("halit" == "aaaaa")
print("car" > "bus")
print("apple" > "Apple") # 'A' => 65, 'a' -> 97
#

# mantıksal operatörler -> and,or,not
print("****")
print(1==1 and 10 > 5) #ve-and => true-true -> true dışında false verir.
print(1==1 and 5 < 3) # false

print(1==1 or 10 > 5) #veya-or => true-false -> true , true-true -> true (Bir tanesinin true olması yeterli.)
print(1==1 or 5 < 3) # true
#
print("*****")
print( 1==1 and 5 > 3 or 10==10 and 5 >= 5 ) #true
print( 1==1 and 5 < 3 or 10==10 and 5 >= 5 ) #true
print( 1==1 and 5 < 3 or 10==10 and 5 >= 6 ) #false
# soldan, not -> and -> or

# parantez önceliği

print(   (1==1 and 2>5) or 6>=6 and (10 > 5 or 5 ==5)   )

print(not 1==1)  #true- not => false
#




a=5
b=a #5
b+=4 #9
print(a) # 5
print(b) # 9

students = [  "Emir","Yasin","Emirhan","Barış","Zeynep", 5, True, 10.1 ,2  ]
students2 = students
students2.append("Ahmet")
print(students)
print(students2)

# döngüler,karar blokları, fonksiyonlar
# oop, modules, pip
# yapay zeka için python..

#döngüler

# bir işlevi (fonksiyon) belirli ya da belirsiz sayıda tekrar etmek için kullanılır.
# for - iteration,iterasyon => her bir tekrara verilen isim
# indentation -> scopeları belirleyen boşluklar {}
# scope -> (kapsam) bir kod bloğunun sahip olduğu kapsama alanı
for i in range(5): #i
    print(i)
    print("merhaba") #main>for scope'u
print("For bitti") #main scope'u

for i in range(8,10): #i => isim benzerliği
    print(i)
print("***")
for i in range(5,50,5):
    print(i)

students3 = ["Ali","Aybüke","Büşra","Deniz"]
#print(students3[2])

for student in students3:
    print("Hesaplama yapılıyor: " + student)
print("****")
for student in students3:
    if student == "Büşra":
        continue #continue => döngüye sonraki elemandan devam et.
    print("Hesaplama yapılıyor: " + student)
print("****")
for student in students3:
    if student == "Büşra":
        break #break => döngüyü manual olarak bitirmeyi hedefler.
    print("Hesaplama yapılıyor: " + student)
#

# while
# koşul ile çalışıyor.
#while 10 == 10: # while sonsuz döngüye (infinite loop) girme riski olan bir döngüdür.
    #print("While")

x = 50
while x < 100:
    print(x)
    x += 1
#

user_input = input("Lütfen bir değer giriniz, çıkmak için q tuşuna basınız.")

while user_input != "q":
    print(f"Verdiğiniz değer: {user_input}")
    user_input = input("Lütfen bir değer giriniz, çıkmak için q tuşuna basınız.")

