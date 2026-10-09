def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif")

    print(f"Umur kamu: {umur}")


try:
    cek_umur(20)
    cek_umur(-5)

except ValueError as error:
    print(f"Error: {error}")
