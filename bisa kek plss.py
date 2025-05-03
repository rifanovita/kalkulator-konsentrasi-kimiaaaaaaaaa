print("=== KALKULATOR KONSENTRASI KIMIA ===")
print("1. Hitung Molaritas (mol/L)")
print("2. Hitung Normalitas (eq/L)")

pilih = input("Pilih 1 atau 2: ")

jumlah = float(input("Masukkan jumlah mol atau ekivalen: "))
volume = float(input("Masukkan volume larutan (liter): "))

if pilih == "1":
    molaritas = jumlah / volume
    print("Molaritas =", molaritas, "mol/L")
elif pilih == "2":
    normalitas = jumlah / volume
    print("Normalitas =", normalitas, "eq/L")
else:
    print("Pilihan tidak valid.")
