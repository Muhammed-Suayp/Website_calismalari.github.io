# boy = float(input("boyunuzu giriniz (m) : "))
# kilo = float(input("kilonuzu giriniz (m) : "))
# bki = kilo / (boy * boy) 
# print(bki)


"""
# Aritmetik Operatorler
    +
    -
    /
    *
    %
    ** (üs alma)
    // (taban bölme)
"""

# print(10 % 3)
# print(10 ** 3)  # 10 üssü 3


# print(10 / 3)
# print(10 // 3)

# sayi1 = int(input("bir sayı giriniz : "))
# result = sayi1 % 2

# if result == 1:
#     print("tek")
# else:
#     print("cift")







"""
    Atama Operatorleri
          = 
          += 
          -=
          *=
          /=
          %=
          //=
          **=
"""

# a = 2
# a += 4 #     a = a + 4
# print(a)

# a = 2
# b = 6
# b += a # b = b + a
# print(b)

# a = 2
# a++
# print(a)

# a = 2
# a += 1
# print(a)

"""
    Karşılaştırma Operatörleri
         ==
         != 
         >
         <
         >=
         <= 
"""

# print(3 == 5)
# print(3 == 3)

# print( 3 != 5)
# print(3 != 3)


"""
    Mantıksal Operatorler
          and
          or 
          not

"""

# print(3>2 and 5>2)
# print(3>2 and 5>6)

# print(3>2 && 5>2) -> pythonda geçerli değildir


"""
    And (&&)
    ----------
    0   0   = 0
    0   1   = 0
    1   0   = 0
    1   1   = 1
"""


"""
    or (||)
    ----------
    0   0   = 0
    0   1   = 1
    1   0   = 1
    1   1   = 1
"""

# print(5>3 or 3<5)


"""
    not (!)
    ----------
    1 = 0
    0 = 1
"""

# print(not(5>3))


# list
# ogrenciler = ["ali", "ahmet"]
# print(ogrenciler)
# print(ogrenciler[0])

# a = [10.2, 45, 'ali', True]
# print(a)

# a = []
# print(a)
# print(type(a))

# a  = [12, [45,56], "ali", [23,[99,88]]]
# print(a[3])
# print(a[3][1][1])

# a = [12,23,45,56,78,99]
# print(a[0])
# print(a[2:5])
# print(a[:3])
# print(a[2:])
# print(a[1:5:2])
# print(a[-1])
# print(a[-6])
# print(a[-2:-5])
# print(a[-5:-2])

# print(a[-2:-5:-1])


# print(a[::-3])

# a = [12,23,45,56,78,99,44,11,88]
# print(a[-3:]) #[56, 78, 99]
# print(a[0:-3])
# print(a[3:-7:-1])
# print(a[-5:2:1])


# print(list(range(5)))
# print(list(range(5,8)))
# print(list(range(5,12,2)))

for i in range(10,100,5):
    print(i)
    
a = 2

if a > 1:
    print("dfdsf")
    
"""
    for (int i = 0; i < 10 ; i++) {
        printf(i);
    }

"""



