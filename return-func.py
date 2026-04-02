#1
def bolinish():
  for i in range(2, 11):
     if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi.")
a = int(input("Xoxlagan son kirit"))            
bolinish(a) 
 #2   
def add(a, b):
    return a + b
    
print(add(3, 4))
value = add(5, 8)
print(value)
    

#3
def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

print(toliq_ism_yasa("Olim", "Qodirov"))
print(toliq_ism_yasa("Anvar", "Aliyev"))
#4
def is_even(number):
   if number % 2 == 0:
      return "Juft"
    else:
      return "Toq"
   
print(is_even(4)) # Juft
result = is_even(7)
print(result) # Toq 
 #5
#Terner operatori yordamida yuqoridagi funksiyani quyidagicha yozish mumkin:
def is_even(number):
    return "Juft" if number % 2 == 0 else "Toq"

print(is_even(4)) # Juft
print(is_even(7)) # Toq

#6
vowels = ['a', 'e', 'i', 'o', 'u']
def count_vowels(text):
    count = 0
    for char in text:
       if char == vowels[0] or char == vowels[1] or char == vowels[2] or char == vowels[3] or char == vowels[4]:
          count += 1

    return count
print(count_vowels("javascript")) # 3
print(count_vowels("bbb")) # 0
print(count_vowels("programming")) # 3
