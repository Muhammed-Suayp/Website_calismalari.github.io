# a  = ["ali erbey", "ahmet dursun", "veli kaya"]

# # Çıktı ["ali", "erbey", "ahmet", "dursun", "veli", "kaya"]

# b = []
# for i in a:
#     k =  i.split(" ")
#     for v in k:
#         b.append(v)
# print(b)


# a  = ["ali erbey", "ahmet dursun", "veli durmuş"]

# b = []
# for i in a:
#     if i[0] == 'a':
#       b.append(i)
# print(b)  


# b = []
# for i in a:
#     if i.startswith('a'):
#       b.append(i)
# print(b)  


# b = []
# for i in a:
#     if i.startswith('a'):
#         b.append(i.split(' ')[0])
# print(b)  


a  = ["ali erbey", "ahmet dursun", "veli durmuş"]
# b = []
# for i in a:
#     k = i.split(' ')
#     if k[-1].startswith('d'):
#         b.append(i)
# print(b)

# a  = ["ali erbey", "ahmet dursun", "veli durmuş"]

# b = []
# for i in a:
#     b.append(i.title())
    
# print(b)

a = ['sdfcmd0-0-2kd', 'ewrkcmd0-0-12kf']

# çıktı [[0,0,2],[0,0,12]]
# cikti=[]
# for i in a:
#     print(i)
#     k = i.find('cmd')
#     print(i[k:])
#     b = i[k:]
#     v = b.find('k')
#     print(v)
#     print(b[:v])
#     print(b[3:v])
#     n = b[3:v]
#     print(n.split('-'))
#     cikti.append(n.split('-'))
    
# print(cikti)

# cikti2 = []

# for i in cikti:
#     yeni = []
#     for k in i:
#         yeni.append(int(k))
#     cikti2.append(yeni)
# print(cikti2)

a = [2,5,3,9,6]

# cikti[8,17]

# cift = []
# tek = []
# cikti = []

# for i in a:
#     if i % 2 == 0:
#         cift.append(i)
#     else:
#         tek.append(i)
        
# def topla(a):
#     sum = 0
#     for i in a:
#         sum += i
#     return sum    

# cikti.append(topla(cift))
# cikti.append(topla(tek))

# print(cikti)


# ciftToplam, tekToplam = 0, 0

# def ciftTopla(a):
#     ciftToplam += a

# def tekTopla(a):
#     tekToplam += a

# for i in a:
#     if i % 2 == 0:
#         ciftTopla(i)
#     else:
#         tekTopla(i)
        
# cikti = [ciftToplam, tekToplam]

# print(cikti)

a = [{"a":1}, {"b":2}, {3:'c'}]
# cikti = [{"a":2}, {"b":3}, {4:'c'}]

for i in a:
    for k in i.items():
        print(k[0], k[1])
        # print(len(k[0]))
        # print(k[0]*10)
        print(type(k[0])== int)
        
        # c = str(k[0])
        # print(c)
        
        




    
    
    
    
    
