#Return function
# def sum_list(lst)
#     s = 0
#     for element in lst:
#         s += element

#     return s

# print(sum_list([18, 75, -89, 7, 10])) # 21


#Flexible function
# *args usuli
# def summa(*numbers):
#     print(numbers)

# summa(1, 2, 3) # (1, 2, 3)
    
# def my_function(*people):
#     print(f" The youngest person is {people[1]} years old.")

# my_function(" Ali", " Bobur", " Axror")   



# def summa(x, y = 5 *sonlar):
#     return x +y + sum(sonlar)

# print(summa(1, 2, 3, 4, 5)) # 15
# print(summa(5, 12)) # 30


# **kwards(keyword arguments) usuli
# def auto_info(kompaniya, model, **malumotlar):
#     # print(malumotlar){key ; value}
#     # print(type(malumotlar)) dict
#     malumotlar["kompaniya"] = kompaniya
#     malumotlar["model"] = model

#     return malumotlar

# print(auto_info("GM Uzbekistan", "Cobalt", rang="oq", narh=15000))
# print(auto_info("merc", "Gelikvogen", rangi = "qora", narhi = 200000))


def my_function(**kid):
    print("His last name is " + kid["fname"])
my_function(fname = "Tobias", lname = "Refsnes")
    
#AMALIYOT
# 1.Istalgancha sonlarni qabul qilib, hujjat ko'paytmasini qaytaruvchi funksiya yozing
def multiple(*numbers):
    s = 1
    for number in numbers:
        s *= number
        
    return s
    
print(multiple(2, 4, 7)) # 56
print(multiple(1, 3, 5, 7)) # 105
# 2.
#Talabalar haqida ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning va familiyasi 
# samarali argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda boshqariladigan boshqa mumkin bo'lsin.
def student_info(name, lasname, **data):
    data['name'] = name
    data['lastname'] = lastname
    
    return data
print(student_info('Jumagul'"Umrzoqv", year = 2005))




