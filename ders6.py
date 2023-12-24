# a = ["ali erbey", "ahmet dursun", "veli kaya"]
# b=[]
# for i in a:
#     k = i.split(" ")
#     for v in k:
#         b.append(v)
# print(b)      


# a = ["ali erbey", "ahmet dursun", "veli kaya"]
# b=[]
# for i in a:
#     if i.startswith('a'):
#         b.append(i.split(' ')[0])
# print(b)


# a = ["ali erbey", "ahmet dursun", "veli durmuş"]
# b=[]
# for i in a:
#     k= i.split(' ')
#     if k[-1].startswith('d'):
#         b.append(i)
# print(b)


# a = ["ali erbey", "ahmet dursun", "veli kaya"]
# b=[]
# for i in a:
#     k= i.title()
#     b.append(k)
# print(b)   


# a = ['sdfcmd0-0-2kd', 'ewrkcmd0-0-1kf']
# cikti=[]
# for i in a:
#     k= i.find('cmd')
#     b = i[k:]
#     v = b.find('k')
#     n = b[3:v]
#     cikti.append(n.split('-'))

# print(cikti) 

# cikti2=[]
# for i in cikti:
#     yeni=[]
#     for k in i:
#         yeni.append(int(k))
#     cikti2.append(yeni)
# print(cikti2)        


# a = [2,5,3,6,9]
# sum1=0
# sum2=0
# cikti=[]
# tek=[]
# cift=[]
# for i in a:
#     if i%2 ==0:
#       cift.append(i)  


# a = [{"a":1},{"b":2},{3:'c'}]    
# b =[]    
# for i in a:
#     k = i.values()
#     for v in k:
#         v +=1
#         b.append(v)
        


a = "12,23,34,45,56,78"
a = a.split("---")
print(a)
