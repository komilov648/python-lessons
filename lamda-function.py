#lamda function - anonymous (maxfiy, ma'lum)function
# lambda argumnts  : expression(ifoda, bajaradigan vazifasi)
x =lambda a : a % 5
print(x(12)) # 2
product = lambda x, y : x ** y
print(product(3, 2)) # 9
print(product(8, 3)) # 512


# map() va filter()
numbers = list(map(int, input().split()))
sonlar = [5, 8,-8, 0, 13]
sonlar2 = []
for son in sonlar:
    sonlar2.append(son * 2)
print(sonlar2) # [10, 16, -16, 0, 26]

print(list(map(lambda x : x * 2, sonlar))) # [10, 16, -16, 0, 26]


# map(func, iterable)
print(list(map(lambda x : x * 2, sonlar)))
print(list(map(lambda x: x % 3, sonlar)))

# filter(func, iterable)
print(list(filter(lambda x: x > 5, sonlar)))
students = ['Elbek', 'Lobar', "G'ulomjon", "Behruz", "Lola"]
new_list = list(map(lambda ism: ism.lower() , students))
print(list(filter(lambda ism: ism.startswith('l'), new_list)))

def func(x):
    return x + 5

print(list(map(func, sonlar)))