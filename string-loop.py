text = "Hey guys, welcome to my course!"
#string ichida har bir belgining o'z indeks raqami bor. Indekslar 0 dan boshlanadi.
#string uzunligini aniqlash uchun len() funksiyasidan foydalanamiz
print(len(text)) # 35
print(text[0]) # H  
print(text[4]) # g
print(text[10]) # w 
print(text[-1]) # !
print(text[3])#
length = len(text)
# oxirgi belgini olish uchun length-1 indeksidan foydalanamiz
print(text[length-1]) # !           


#for loop yordamida string ichidagi har bir belgini alohida-alohida chiqarish
# 1 - usul
for char in text:
    print(char)

# 2 - usul
for index in range(len(text)):
    print(index, text[index])
# in operatori yordamida string ichida ma'lum bir belgining bor yoki yo'qligini tekshirish
print("welcome" in text) # True
print("hi" in text) # False
print("$$" in text) # False

import math

S, P = map(int, input().split())
D = S * S - 4 * P
sqrt_D = int(math.sqrt(D))

if D < 0:
    print(-1)
else:
    if sqrt_D * sqrt_D != D:
        print(-1)
    else:
        x1 = (S + sqrt_D) // 2
        x2 = (S - sqrt_D) // 2
       
        print(x1, x2)
      