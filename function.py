def yosh_xisobla(tugulgan_yil=1995, isim="Olim"):
    yil = 2026 - tugulgan_yil
    print(f"{isim}ning yoshi: {yil}")
    
yosh_xisobla(1988 , "Ismoil")
yosh_xisobla()

def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

    def solishtirish(a, b):
        if a > b:
            print(f"{a} katta {b} dan")
        elif a < b:
            print(f"{a} kichik {b} dan")
        else:
            print(f"{a} va {b} teng")
    solishtirish(10, 5)
    solishtirish(3, 7)
    solishtirish(4, 4)