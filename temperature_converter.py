def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("=== Konversi Suhu ===")
print("1. Celcius ke Fahrenheit")
print("2. Fahrenheit ke Celcius")
pilih = input("Pilih (1/2): ")

if pilih == "1":
    c = float(input("Masukkan suhu dalam Celcius: "))
    print(f"Hasil: {celsius_to_fahrenheit(c):.2f} °F")
elif pilih == "2":
    f = float(input("Masukkan suhu dalam Fahrenheit: "))
    print(f"Hasil: {fahrenheit_to_celsius(f):.2f} °C")
else:
    print("Pilihan tidak valid.")
