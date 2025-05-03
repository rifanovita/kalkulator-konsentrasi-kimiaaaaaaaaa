print("KALKULATOR KIMIA SEDERHANA")
print("1. Hitung Molaritas (mol/L)")
print("2. Hitung Normalitas (eq/L)")

pilih = input("Pilih 1 atau 2: ")

mol_atau_eq = float(input("Masukkan mol atau ekivalen zat: "))
volume = float(input("Masukkan volume larutan (liter): "))

hasil = mol_atau_eq / volume

if pilih == "1":
    print("Molaritas =", hasil, "mol/L")
elif pilih == "2":
    print("Normalitas =", hasil, "eq/L")
else:
    print("Pilihan tidak valid.")
