import hesapla

# a=hesapla.topla(12,23)
# print(a)

# a=[12,23,34,45]
# b=[]

# for i in a:
#     b.append(i)

# print(b)


# b=[i for i in a]
# print(b)

# sayilar=[12,15,20]

# yeni_liste=[i for i in sayilar]
# print(yeni_liste)

# sayilar=[23,34,45,56]
# yeni=[sayi*2 for sayi in sayilar]
# print(yeni)

# zevzek=[23,34,45,56]
# new=[zev+5 for zev in zevzek]
# print(yeni)



# notlar=[12,7,6,3]
# cift_notlar=[]

# for i in notlar:
#     if i % 2==0:
#         cift_notlar.append(i)
#         print(cift_notlar)

# notlar=[12,7,6,3]
# cift_notlar=[i for i in notlar if i % 2 == 0]

# notlar=[12,7,6,3]
# cift_notlar=[i for i in notlar if i % 2 == 0]

# cift_notlar=[i for i in notlar if i % 2 == 0]





# a = [1, 2, 3, 4, 5, 6, 7]
# b = []  

# for i in a:
#     if i > 3 and i % 2 == 0:
#         b.append(i*i)

# print(b)

# b= [i*i for i in a if i > 3 and i%2 == 0]
# print(b)


#birincide olup ikincide olmayanları bulan kod
sayilar1 = [1, 2, 3, 4, 5]
sayilar2 = [1, 2, 3]

farkli_sayilar = list(set(sayilar1) - set(sayilar2))
print(farkli_sayilar)





# sayilar1 = [1, 2, 3, 4, 5]
# sayilar2 = [1, 2, 3]
# farkli_sayilar=[]


# for i in sayilar1:
#     if i not in sayilar2:
#         farkli_sayilar.append(i*i)
# print(farkli_sayilar)





# sayilar=[1,2,3,4,5]
# sayilar1=[1,2,3]
# x=[]

# for i in sayilar:
#   if i not in sayilar1:
#    x.append(i)
# print(x)
   

# sayilar=[1,2,3,4,5]
# sayilar1=[1,2,3]

# farkli_Sayilar=[i*i for i in sayilar if i not  in sayilar1]
# print(farkli_Sayilar)





# a=[[12,23],[1,2,3],[1]]

# for i in a:




# a = [[12, 23], [1, 2, 3], [1]]

# birlesik_liste = []

# for alt_liste in a:
#     birlesik_liste.extend(alt_liste)

# print(birlesik_liste)



# a = [[12, 23], [1, 2, 3], [1]]
# b=[]

# for i in a:
#     for j in i:
#         b.append(j)
# print(b)


# b=[j for i in a for j in i]

# print(b)





# a={'ali':12,'veli':23}

# sayilar=[1,2,3,4,5]
# yeni_dict={}

# for sayi in sayilar:
#     if sayi % 2  != 0:
#         yeni_dict[sayi] = sayi**2

# print(yeni_dict)

# yeni_dict = {sayi : sayi ** 2 for sayi in sayilar if sayi % 2 != 0}
# print(yeni_dict)





































