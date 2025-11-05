print("Selamat datang ke dalam Program Core Class, \n " 
"Silahkan masukkan Username dan Password anda")
kesempatan = 3

for i in range (kesempatan) :
    Username = input("Masukkan Username anda : ")
    password = input("Masukkan Password anda : ")

    if Username == "linalisna21" and password == "Code*123":
        print(f"Login Berhasil! \n Selamat datang, {Username}")
    else:
        Sisa = kesempatan - (i+1)
        if Sisa > 0 :
            print (f"Login Salah! Kesempatan tersisa {Sisa} kali lagi.")
        else :
            print ("Akses ditolak. Anda telah gagal login 3 kali.\n" \
            " Silakan hubungi costumer service untuk mereset password")

