python_dictionary = {
    "integer": "butun son",
    "float": "o'nlik son",
    "string": "matn",
    "boolean": "mantiqiy qiymat",
}

text = input("Kalit so'zni kiriting: ")
print(python_dictionary.get(text))
if python_dictionary.get(text) == None:
    print("Bunday kalit so'z mavjud emas.")
else:
    print(python_dictionary.get(text))