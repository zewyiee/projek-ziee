# Program Perhitungan BMI sederhana
def BMI_Formula(Mass, Height):
    BMI = Mass / (Height**2)
    return BMI  # Mengembalikan nilai BMI

# Variabel Category
Category1 = "Underweight"
Category2 = "Normal"
Category3 = "Overweight"
Category4 = "Obese"

# Biodata user
print("Selamat datang di penghitung BMI!")
User = input("Masukkan Nama Anda: ")
print(f"{User}, silahkan masukkan berat dan tinggi badan anda!")

Mass = int(input("Masukkan berat badan anda: "))
Height = float(input("Masukkan tinggi badan anda (dalam m): "))

# Eksekusi Program
BMI = BMI_Formula(Mass, Height)  # Simpan hasil BMI

# Program persyaratan
if BMI < 18:
    print(Category1)
elif 18 <= BMI < 25:
    print(Category2)
elif 25 <= BMI < 30:
    print(Category3)
elif BMI >= 30:
    print(Category4)
else:
    print("Error")