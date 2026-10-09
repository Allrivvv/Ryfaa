def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"


print(sapa("Ani"))
print(sapa(salam="Hai", nama="Budi"))


def total(*angka):
    return sum(angka)


print(total(1, 2, 3, 4))


def data_mahasiswa(**data):
    for k, v in data.items():
        print(f"{k}: {v}")


data_mahasiswa(nama="Rina", jurusan="Sistem Informasi")
