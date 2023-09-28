# print("Hello world i'm learning python")

# user_prompt = "Enter a todo:"
# text = input(user_prompt)
# print(text)

# user_prompt = "enter a to do"
# todo_1 = input(user_prompt)
# todo_2 = input(user_prompt)
# todo_3 = input(user_prompt)
#
# todos = [todo_1, todo_2, todo_3]
# print(todos)

# name = "M. fauzan Alfahza"
# age = 15
# height = 1.6
# isLazy = True
#
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(isLazy))

# fullname = "M.Fauzan Alfahza"
# print(fullname)
# print(type(fullname))

# user_input = int(input("Input :"))
# print(user_input)
# print(type(user_input))

# my_hobies =["Main", "Belajar", "Jalan", "Berenang"]
# print(my_hobies)

# name = input("MASUKAN NAMA : ")
# age = int(input("MASUKAN UMUR : "))
# height = float(input("MASUKAN TB: "))
# isHappy = bool(input("T/F : "))
#
# print("Nama saya", name.title())
# print("umur saya", age)
# print("Tinggi saya", height)
# print("Apakah saya bahagia", isHappy)

# user_prompt =  "Enter a todo : "
# while 2 > 1 :
#     todo = input(user_prompt)
#     print(todo)
#     print("Next to do")

# user_prompt = "Enter a to do : "
# i = 1
# while i <= 5 :
#     todo = input(user_prompt)
#     print(todo)
#     i+=1
#
# Pelajaran = "Masukan pelajaran :"
# i = 1
# while i <= 5 :
#     Mapel = input(Pelajaran)
#     print(Mapel.capitalize())
#     i += 1

# user_prompt = "Enter a to do : "
# i = 1
# todos = []
#
# while i < 5:
#     todo = input(user_prompt)
#     print(todo.title())
#     todos.append(todo)
#     print(todos)
#     i += 1

# Presiden_RI = "Nama presiden : "
# i = 1
# todos = []
# while i <= 7 :
#     presiden = input(Presiden_RI)
#     print(presiden.title())
#     todos.append(presiden)
#     print(todos)
#     i += 1

# password = input("Enter a password : ")
#
# while password != "pass123" :
#     password = input("Enter a password : ")
#
# print("Password Correct")

# joke = ("Hantu, hantu apa yang sopan : ")
# answer = "Nunsewu"
# kesempatan_maximal = 3
# kesempatan = 0
#
# while kesempatan < kesempatan_maximal :
#     joke = input("Hantu, hantu apa yang sopan : ")
#
#     if joke == answer:
#         print("Jawaban benar")
#         break
#
#     else :
#         print("Jawaban salah")
#         kesempatan += 1
#
#         if kesempatan == kesempatan_maximal:
#             print("The answer is", answer)

# joke = input("hantu apa yang sopan : ")
# answer = "Nunsewu"
# i = 1
#
# if joke != answer :
#     joke = input("hantu apa yang sopan : ")
#     i += 1
#
#     while i <= 3 :
#         joke = input("hantu apa yang sopan : ")
#         print("The answer is",answer)
#         break
#
# else :
#     print("Answer correct")

# Nilai = int(input("Masukan nilai : "))
# KKM = int(input("Masukan KKM : "))
# Absensi = int(input("Masukan jumlah hadir : "))
#
# if Nilai >= KKM and Absensi > 0 :
#     print("Kamu lulus")
#
# elif Nilai < KKM and Absensi == 0 :
#     print("kamu harus remedi")
#
# else :
#     print("Kamu tidak pernah turun")

# Buku = int(input("Jumlah buku : "))
# Total = float(input("Berapa total pembelian : "))
#
# if Buku >= 5 and Total > 100.000 :
#     print("anda dapat diskon 20%")
#
# else :
#     print("Anda ga dapat diskon")

# muda 0 - 16 tahun
# remaja 17 - 25 tahun
# dewasa 26 - 45 tahun
# sisanya lansia

# Umur = int(input("Masukan usia : "))
#
# if Umur <= 16 :
#     print("Anda golongan muda")
#
# elif Umur > 16 and Umur <= 25 :
#     print("Anda golongan remaja")
#
# elif Umur > 25 and Umur <= 45 :
#     print("Anda golongan dewasa")
#
# else :
#     print("Anda golongan lansia")

# my_hobies = ["Main", "Belajar", "Jalan", "Berenang"]
# print(my_hobies[3])

# biodata = {
#     "Nama" : "M. Fauzan alfahza",
#     "Alamat" : "Jl.Sungai Dama",
#     "Umur" : 15,
#     "Pelajar" : True
# }
#
# print("Nama saya", biodata["Nama"], "Saya tinggal di", biodata["Alamat"], "Umur saya", biodata["Umur"])

# biodata = {
# }
# print(biodata)
#
# biodata["Nama"] = input("Masukan nama : ")
# biodata["Tahun_lahir"] = int(input("Masukan Tahun Lahir :"))
# biodata["Umur"] = 2023 - biodata["Tahun_lahir"]
# biodata["Alamat"] = input("Masukan alamat :")
# biodata["Pelajar"] = bool(input("Apakah anda pelajar : "))
# print(biodata)

# biodata = {
# }
# print(biodata)
#
# biodata["Nama"] = input("Masukan nama : ")
# print(biodata)
# biodata["NISN"] = int(input("Masukan NISN : "))
# print(biodata)
# biodata["Mapel"] = input("Masukan mapel : ")
# print(biodata)

# Umur = int(input("Masukan umur : "))
# data_pribadi = []
# i = 1
#
# if Umur >= 18 :
#     while i <= 2 :
#         data = input("Masukan data pribadi anda : ")
#         data_pribadi.append(data)
#         print(data_pribadi)
#         i += 1
#
# else :
#     print("Belum cukup umur")

# Nama = input("Masukan Nama : ")
# Umur = int(input("Masukan Umur : "))
#
# if Umur >= 18 :
#     SIM = bool(input("Isi jika punya, jika tidak skip aja : "))
#     if SIM :
#         print("Anda Boleh Mengemudi")
#     else :
#         print("Anda Tidak Boleh Mengemudi")
# else :
#     print("Anda Tidak Boleh Mengemudi")

# SIM = bool(input("isi aja"))
# print(SIM)

# a = 10
# for i in range(a) :
#     print("Perulangan ke-" + str(i))

# film = ['film a', 'film b', 'film c']
# for i in film :
#     print("Sekarang tayang", i)

# jawab = 'ya'
# hitung = 0
# while (jawab == 'ya') :
#     hitung += 1
#     jawab = input("Ulang lagi tidak?")
#
# print(f"Total perulangan: {hitung}")

# hitung = 0
# while True :
#     hitung += 1
#     ulang = input("Masih Ingin mengulangi?")
#     if ulang == 'tidak' or ulang == 'Tidak' :
#         break
#
# print(f"Total perulangan: {hitung}")
#
# number = [
#    2, 3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20
# ]
# a = 2
# for a in number :
#     if a % 2 != 0 :
#         print(a)
#

# def prima(a):
#     if a % 1 != 0 :
#         if a % 2 != 0 :
#             if a % 3 != 0:
#                 if a % 4 != 0:
#                     if a % a-1 != 0:
#                         return a
#     return a
# print(prima(10))

# def is_prime(number) :
#     for i in range(2, number + 1) :
#         if number % i != 0:
#             print(i)
# print(is_prime(20))

# for num in range(2,0):
#     prime = True
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False
#     if prime:
#        print (num)

# number = 20
# print(2)
# for i in range(number) :
#     if  i > 1 :
#         if i % 2 != 0 :
#             if i % 9 != 0 :
#                 if i % 15 != 0 :
#                     print(i)

# todos = []
# while True :
#     user_action = input("Type add / show")
#
#     match user_action :
#         case 'add' :
#             todo = input("Enter a todo : ")
#             todos.append(todo)
#         case 'show' :
#             print(todos)

# saldo = 20_000
# isInsert = bool(input("Apakah kartu masuk ? "))
# while True :
#     user_action = input("Type cek rekening, lakukan transaksi atau keluar : ")
#
#     match user_action :
#         case 'lakukan transaksi' :
#             transaksi = input("Masukan Nomor rekening : ")
#         case 'cek rekening' :
#             print('saldo anda Rp',saldo)
#         case 'keluar' :
#             action = input("Apakah anda yakin ingin keluar ?")
#             if action :
#                 break
#
# print("Terima kasih")

# birth_year = int(input("Masukan tahun lahir : "))
# age =  2023 - birth_year
# datas = []
# while age > 18 :
#     user_action = input("Type Add, Show or Exit : ").strip().capitalize()
#     match user_action :
#         case 'Add' :
#              data = input("Masukan data : ").strip().capitalize()
#              datas.append(data)
#         case 'Show' :
#             for i in datas :
#                 print(i)
#         case 'Exit' :
#              break
# print("Bye")

# birth_year = int(input("Masukan tahun lahir : "))
# age =  2023 - birth_year
# games = []
# while age > 18 :
#     user_action = input("Type beli, checkout or proses bayar : ").strip()
#     match user_action :
#         case 'beli' :
#              game = input("Masukan game : ").strip()
#              games.append(game)
#         case 'checkout' :
#             for i in games :
#                 print(i)
#         case 'proses bayar' :
#              bayar = bool(input("Apakah pembayaran berhasil : "))
#              if bayar :
#                  print("Pembayaran berhasil")
#              else :
#                  print("Pembayaran gagal")
#                  break
# print("Bye")

# birth_year = int(input("Masukan tahun lahir : "))
# age =  2023 - birth_year
# datas = []
# while age > 18 :
#     user_action = input("Type add, show or exit : ").strip()
#     match user_action :
#         case 'add' :
#              data = input("Masukan data : ").strip()
#              datas.append(data)
#         case 'show' :
#             for i in datas :
#                 print(i)
#         case 'exit' :
#              break
#         case default :
#             print("Please Type the command correctly")
# print("Bye")

# birth_year = int(input("Masukan tahun lahir : "))
# age =  2023 - birth_year
# games = []
# while age > 18 :
#     user_action = input("Type beli, checkout or proses bayar : ").strip()
#     match user_action :
#         case 'beli' :
#              game = input("Masukan game : ").strip()
#              games.append(game)
#         case 'checkout' :
#             for i in games :
#                 print(i)
#         case 'proses bayar' :
#              bayar = bool(input("Apakah pembayaran berhasil : "))
#              if bayar :
#                  print("Pembayaran berhasil")
#              else :
#                  print("Pembayaran gagal")
#                  break
#         case default :
#             print("Perintah anda salah")
# print("Bye")

# Pulsa = 500_000
# print("silahkan pilih menu ")
#
# while True :
#     print("1. beli Masa aktif", "2. beli paket darurat", "3. Cek Pulsa", "4. Keluar")
#     a = int(input("Silahkan pilih menu diatas : "))
#     match a :
#         case 1 :
#             print("1a.Paket 200Gb", "2a. Paket 150Gb, 3a. Keluar")
#             b = input("pilih paket anda : ")
#             match b :
#                 case '1a' :
#                     print("Paket 200Gb dibeli")
#                 case '2a' :
#                     print("Paket 150Gb dibeli")
#                 case '3a' :
#                     continue
#                 case default :
#                     print('input salah')
#         case 2 :
#             print("1b. Paket 800Mb", "2b. Paket Paket 150Mb", "3b. Keluar")
#             c = input("Pilih Paket Anda : ")
#             match c :
#                 case '1b':
#                     print("Paket 800Mb dibeli")
#                 case '2b':
#                     print("Paket 150Mb dibeli")
#                 case '3b':
#                     continue
#                 case default :
#                     print("input salah")
#         case 3 :
#             print("Pulsa anda sisa Rp.",Pulsa)
#             continue
#         case 4 :
#             print("Terima Kasih")
#             break


# def nama_lengkap(parameter) :
#     print(parameter)
# nama_lengkap("M.Fauzan")

# def bersihin_rumah(p1, p2, p3) :
#     print(p1, p2, p3)
# bersihin_rumah('sapu', 'kemoceng', 'sekop')

# def luas_persegi_panjang(p, l):
#     luas = p * l
#     print("Luas Persegi panjang : ", int(luas))
# luas_persegi_panjang(4, 6)

# def luas_persegi(s):
#     luas = s * s
#     return luas
# print("Luas persegi : %d " %luas_persegi(8))

# def luas_trapesium(a, t) :
#     luas = (a * t) / 2
#     return luas
# print("Luas Trapesium : %d" %luas_trapesium(9, 8))

# def luas_lingkaran(r) :
#     luas = 3.14 * r**2
#     return luas
# print('luas lingkaran : %f' %luas_lingkaran(8))

# def volume_persegi(s):
#     volume = s**3
#     return volume
# print("volume persegi : %d" %volume_persegi(2))

# sisi = int(input('Masukan nilai sisi : '))
# def volume_persegi(s):
#     volume = s**3
#     return volume
# print("volume persegi : %d" %volume_persegi(sisi))

# todos = []
#
# print("Welcome to task list app")
# while True:
#     user_action = input("Type Add/Show/Edit/Exit :").strip().title()
#     match user_action:
#         case 'Add':
#             todo = input("Enter a To Do :").capitalize()
#             todos.append(todo)
#         case 'Show':
#             for i in range(len(todos)):
#                 number = i +1
#                 print(number, todos[i])
#         case 'Exit':
#             break
#         case 'Edit':
#             number = int(input("Number of Task : "))
#             new_todo = input("Enter a New Task : ")
#             todos[number] = new_todo
#         case default:
#             print("Incorrect Command")
# print("Good Bye")

menus = ['beli masa aktif', 'beli paket darurat', 'cek pulsa', 'keluar']
Pulsa = 500_000
print("silahkan pilih menu ")

while True :
    for i in range(len(menus)) :
        number = i + 1
        print(number, menus[i])
    a = int(input("Silahkan pilih menu diatas : "))
    match a :
        case 1 :
            print("1a.Paket 200Gb", "2a. Paket 150Gb, 3a. Keluar")
            b = input("pilih Menu : ")
            match b :
                case '1a' :
                    print("Paket 200Gb dibeli")
                case '2a' :
                    print("Paket 150Gb dibeli")
                case '3a' :
                    continue
                case default :
                    print('input salah')
        case 2 :
            print("1b. Paket 800Mb", "2b. Paket Paket 150Mb", "3b. Keluar")
            c = input("Pilih Menu : ")
            match c :
                case '1b':
                    print("Paket 800Mb dibeli")
                case '2b':
                    print("Paket 150Mb dibeli")
                case '3b':
                    continue
                case default :
                    print("input salah")
        case 3 :
            print("Pulsa anda sisa Rp.",Pulsa)
            continue
        case 4 :
            print("Terima Kasih")
            break