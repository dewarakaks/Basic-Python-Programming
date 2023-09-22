def pangkat(x, n):
    if n == 0:
        return 1
    elif n > 0:
        if n % 2 == 0:
            temp = pangkat(x, n // 2)
            return temp * temp
        else:
            return x * pangkat(x, n - 1)
    else:
        return 1 / pangkat(x, -n)

while True:
    try:
        x = float(input("Masukkan angka (x): "))
        n = int(input("Masukkan pangkat (bilangan bulat): "))

        hasil_pangkat_n = pangkat(x, n)
        hasil_pangkat_n_per_2 = pangkat(x, n // 2)

        print(f"{x} pangkat {n} adalah {hasil_pangkat_n}")
        print(f"{x} pangkat {n/2} adalah {hasil_pangkat_n_per_2}")

        ulangi = input("Apakah Anda ingin mencoba lagi? (ya/tidak): ")
        if ulangi.lower() != "ya":
            break
    except ValueError:
        print("Masukkan angka yang valid untuk x dan pangkat.")
