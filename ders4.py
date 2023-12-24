# a = [] # list #
# print(type(a))
# b = {'ali':21, 'veli':34} # dictionary
# print(b)


# tuple (immutable) -> degismez

# a = (12,34,54)
# print(type(a))
# print(a[0])

# --------------------------
# list
# dictionary
# tuple

# a = [12,34,56]
# print(a[0])
# a[0] = 99
# print(a)

# a = (12,34,56)
# print(a[0])
# a[0] = 99 #' tuple' object does not support item assignment
# tuple elemanları değiştirilemezdir.

a = [12,23,34]
# print(a[3]) #  list index out of range

# a.append(67)
# print(a)


# a.append(67,78,89) # list.append() takes exactly one argument (3 given)
# print(a)

# a.extend([11,22,33])
# print(a)

""" 
List methodları
-------------------
append -> eleman ekler
extend -> dizi ekler
insert -> belirli bir alana ekleme yapar
pop -> eleman çıkartır
remove -> eleman çıkartır
del -> nesneleri silebilirsiniz

"""

# a = [12,23,34]
# b = [99,56,67]
# c = a + b
# print(c)

# a = [12,23,45]
# a.insert(1,99)
# print(a) # [12, 99, 23, 45]

# a = [12,34,56]
# a.pop()
# print(a)

# a = [12,34,56]
# a.pop(0)
# print(a)

# a = [12,34,45,67]
# a.remove(45)
# print(a)

# a = [12,34,56]
# a.clear()
# print(a)

# a = [12,45,56,67]
# print(a.index(45))

# b = [12,45,56,67,99,34,45,65423,234,34,00,23,234,54]
# start = b.index(99)
# end = b.index(00)
# print(start, end)
# print(b[start:end])

# a = [34,56,67,78]
# del a[2]
# print(a)

# a = [12,34,45]
# del a
# print(a)

# a = [34,56,78,89,23,56]
# print(a.count(56))


# a = [34,56,78,89,23,56] 
# print(a.count(99)) # eleman yoksa 0 verir

# a = [1,2,3,4]
# a.reverse()
# print(a)


# a = [23,2,5,6]
# a.sort()
# print(a)


# a = [12,34,56,78]
# b = a
# b[0] = 99
# print(a)
# print(b)

# a = [12,34,56,78]
# b = a.copy()
# b[0] = 99
# print(a)
# print(b)

# a = [12,34,56,78]
# a[1:3] = [99,11]
# print(a)

# a = [12,23,34,54,65,76,34,56,67,78,99,23,00,11,23,34,99,67,89434,34,54,00]

# a = (12,34,45,56,34)
# print(a)
# print(type(a))

# print(a.index(45))
# print(a.count(34))
# print(a[1:4])

# a = 12,34,45,56
# print(a)
# print(type(a))

# a = "ali", "ahmet", "ayse"
# print(a)


# a = {'id': 2, 'bookTitle': 'Saatleri ayarlama enstitüsü'}
# print(type(a))
# print(a['id'])
# print(a['bookTitle'])


# posts = [
#     {'id': 1, 'bookTitle': 'Saatleri ayarlama enstitüsü'},
#     {'id': 2, 'bookTitle': 'Clockwork Orange'},
#     {'id': 3, 'bookTitle': 'Suç ve Ceza'},
#     {'id': 4, 'bookTitle': 'Sefiller'},
#     {'id': 5, 'bookTitle': 'Şahsultan'}
# ]

# print(posts[0]['bookTitle'])
# print(posts[1]['bookTitle'])
# print(posts[2]['bookTitle'])
# print(posts[3]['bookTitle'])
# print(posts[4]['bookTitle'])

# print(len(posts))
# for i in range(len(posts)):
#     print(posts[i]['bookTitle'])



# a = {'id': 1, 'bookTitle': 'Saatleri ayarlama enstitüsü'}
# print(a.keys())
# print(a.values())
# print(a.items())

# for i in a.items():
#     print(i[1])

a = {'id': 1, 'bookTitle': 'Saatleri ayarlama enstitüsü'}


# b = {
#     "products": [
#         {
#             "id": 1,
#             "title": "iPhone 9",
#             "images": [
#                 "resim1",
#                 "resim2"
#             ]
#         },
        
#     ]
# }

# print(type(b))
# print(b['products'][0]['images'][0])
# print(b['products'][0]['images'][1])


# b = [{
#     "products": [
#         {
#             "id": 1,
#             "title": "iPhone 9",
#             "images": [
#                 "resim1",
#                 "resim2"
#             ]
#         },
        
#     ]
# },
#      {
#     "products": [
#         {
#             "id": 2,
#             "title": "iPhone 9",
#             "images": [
#                 "resim1",
#                 "resim2"
#             ]
#         },
#          {
#             "id": 3,
#             "title": "iPhone 9",
#             "images": [
#                 "resim5",
#                 "resim2"
#             ]
#         },
        
#     ]
# },
     
#      ]

# print(b[1]['products'][1]['images'][0])


# a = {1: 'Elma', 2: 'Portakal'}
# a.clear()
# print(a)


# a = {1: 'Elma', 2: 'Portakal'}
# b = a.copy()
# print(b)

# a = {1: 'Elma', 2: 'Portakal'}
# print(a[4])
# print(a.get(4))
# print(a.get(4, "yok"))

# a = {1: 'Elma', 2: 'Portakal'}
# print(a.pop(2))
# print(a)

# a = {1: 'Elma', 2: 'Portakal'}
# print(a.setdefault(2,"muz"))
# print(a.setdefault(5, "muz"))


# a = {1: 'Elma', 2: 'Portakal'}
# b = {1: 'Elma', 2: 'Muz'}
# a.update(b)
# print(a)











