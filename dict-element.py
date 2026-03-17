mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
}

print(mahsulotlar.keys())
fruits = ['olma', 'anor', 'uzum', 'anjir', 'shaftoli']

bozorlik = ['anor', 'uzum', 'non', 'anjir']
for mahsulot in mahsulotlar:
    print(mahsulot)


for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} som")

        print(sorted(mahsulotlar.keys())) 
print("Dokonimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot)