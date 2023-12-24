# a = {12,2,3,6,78,34,5}


# list=[]
# toplam=0
# toplam2=0

# for i in a:
#    if i % 2== 0 :  
#     toplam = toplam+i
#     print(toplam)
#    else :
#     toplam2=toplam+i

# print(toplam) 
# print(toplam2)    


# a = {12,25,3,35,78,34,5}
# list=[]
# for i in a:
#    if i % 5 == 0:
#     b=list.append(i)

# print(list)   
 

# a = {12,2,3,6,78,34,5}
# b = {5,22,6,35}
# c=[]

# for i in a:
#     if i not in b:
#         i += 1
#         c.append(i)

# for i in b:
#     if i not in b:
#         i += 1
#         c.append(i)

# print(c)    


# a = {12,2,3,6,78,34,5}
# b = {5,22,6,35}
# c=[]

# for i in range(len(a)):
#     yeap = False
#     for j in range(len(b)):
#         print(a[i],b[j])
#         if a[i]== b[j]:
#             yeap = True
#     if not yeap:
#         c.append(a[i])

# for i in range(len(b)):
#     yeap = False
#     for j in range(len(a)):
#         print(b[i],a[j])
#         if b[i]== a[j]:
#             yeap = True
#     if not yeap:
#         c.append(b[i])    

# print(c)            



# FONKSİYONLAR

# def topla(a,b):
#     print("topla fonksiyonu")
#     c = a+b
#     return c

# a = topla(12,34)
# print(a)

# def topla(a,b):
#      print("topla fonksiyonu")
#      c = a+b
#      return c

# k = [12,23,34,45]    
# a = topla(k)
# print(a) 


# def yeap(*a):
#    print(a)

# yeap(22,45)   

# def yeap(*a):
#     sum =0
#     for i in a:
#         sum += i
#         return sum
 
 
# print(yeap(22,45))

# def yeap(isim = 'ali'):
#     print(isim)

# yeap('emre')  
# yeap()  


# print(12,34,56,sep='---')