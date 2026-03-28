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
