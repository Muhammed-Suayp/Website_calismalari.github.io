# a=open('deneme.txt', 'w')
# print(a)
# a.write("bu dosyaya yazilacak") #dosya yazmak için

a=open('deneme.txt','r') #dosya okumak için
#print(a.read())
#print(a.read(7))
# print(a.readline())
# print(a.readlines()[2]) #readline satır satır okur   readline imleç neredeyse kaldığı yerden devam eder "\"


# print(a.readline())
# print("-------")
# print(a.readline())
# print("-------")

# a.close() #dosya kapatmak için

# with open('deneme.txt','r') as a:
#     print(a.read())
#     a.seek(0)
#     print('------')
#     print(a.readline())
#     print(a.tell())
#     a.seek(a.tell() + 15)
#     print(a.read())


# a = open('deneme.txt','a')
# a.write("sdfsdf\n")
 

# a = open('deneme.txt','r+')
# b = a.readlines()

# print(b)
# b.insert(1,'ahmet\n')
# print(b)
# a.close()
# a=open('deneme.txt','w')
# a.writelines(b)


# try:
#   print(5/0)
# except:
#   print("bir hata oluştu") ##hata tespit ediyor çok çok önemli

# def topla():
#    sayi1 = int(input("Birinci sayiyi giriniz :"))
#    sayi2 = int(input("ikinci sayiyi giriniz :"))
#    print(sayi1/sayi2)

# try:
#    topla()
# except:
#    print('hata') 



#    def topla():
#    sayi1 = int(input("Birinci sayiyi giriniz :"))
#    sayi2 = int(input("ikinci sayiyi giriniz :"))
#    print(sayi1/sayi2)
   
# try:
#    topla()
# except Exception as e:
#    print('hata',e) 



# try:
#     print(a)
# except Exceptin as e:
#     print('hata: ',e)


# try:
#     sayi1 = int(input("Birinci sayiyi giriniz :")
#     print(sayi1)
#     print(5/sayi1)

# try:
#     print(a.read())
# except Exception as e:
#     print('hata var:',e)
# else:
#     print('resule sakso')
# finally:


import random
print(random.random())