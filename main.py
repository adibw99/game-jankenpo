import random

# Daftar pilihan tangan
choices = ["batu", "gunting", "kertas"]

# Loop utama program
while True:
    # Menampilkan menu dan meminta pengguna memilih tingkat kesulitan
    print("Selamat datang di Game Jankenpo!")
    print("1. Mudah")
    print("2. Sedang")
    print("3. Sulit")
    print("4. Keluar")
    level = input("Pilih tingkat kesulitan (1/2/3/4): ")

    if level == "1":
        # Tingkat kesulitan mudah, komputer selalu memilih gunting
        print("Tingkat kesulitan: Mudah")

        while True:
            # Menampilkan menu pilihan tangan dan meminta pengguna memilih
            print("Pilih tanganmu: ")
            print("1. Batu")
            print("2. Gunting")
            print("3. Kertas")
            user_choice = input("Masukkan pilihanmu (batu/gunting/kertas): ")

            # Memilih tangan komputer secara acak dan menampilkan hasil
            computer_choice = "gunting"
            print(f"Komputer memilih: {computer_choice}")

            # Menentukan pemenang berdasarkan aturan jankenpo
            if user_choice == "batu" and computer_choice == "gunting" or \
                user_choice == "gunting" and computer_choice == "kertas" or \
                user_choice == "kertas" and computer_choice == "batu":
                print("Kamu menang!")
            elif user_choice == computer_choice:
                print("Seri!")
            else:
                print("Kamu kalah!")

            # Menampilkan pilihan untuk melanjutkan atau keluar
            play_again = input("Main lagi? (y/n): ")
            if play_again.lower() != "y":
                break

    elif level == "2":
        # Tingkat kesulitan sedang, komputer memilih secara acak
        print("Tingkat kesulitan: Sedang")

        while True:
            # Menampilkan menu pilihan tangan dan meminta pengguna memilih
            print("Pilih tanganmu: ")
            print("1. Batu")
            print("2. Gunting")
            print("3. Kertas")
            user_choice = input("Masukkan pilihanmu (1/2/3): ")

            # Memilih tangan komputer secara acak dan menampilkan hasil
            computer_choice = random.choice(choices)
            print(f"Komputer memilih: {computer_choice}")

            # Menentukan pemenang berdasarkan aturan jankenpo
            if user_choice == "1" and computer_choice == "gunting" or \
                user_choice == "2" and computer_choice == "kertas" or \
                user_choice == "3" and computer_choice == "batu":
                print("Kamu menang!")
            elif user_choice == "1" and computer_choice == "batu" or \
                user_choice == "2" and computer_choice == "gunting" or \
                user_choice == "3" and computer_choice == "kertas":
                print("Seri!")
            else:
                print("Kamu kalah!")

            # Menampilkan pilihan untuk melanjutkan atau keluar
            play_again = input("Main lagi? (y/n): ")
            if play_again.lower() != "y":
                break

    elif level == "3":
        # Tingkat kesulitan sulit, komputer memilih secara acak dengan chance
        print("Tingkat kesulitan: Sulit")

        while True:
            # Menampilkan menu pilihan tangan dan meminta pengguna memilih
            print("Pilih tanganmu: ")
            print("1. Batu")
            print("2. Gunting")
            print("3. Kertas")
            user_choice = input("Masukkan pilihanmu (1/2/3): ")

            # Menghitung chance masing-masing pilihan tangan
            rock_chance = 60
            scissors_chance = 30
            paper_chance = 10

            # Memilih tangan komputer berdasarkan chance
            rand_num = random.randint(1, 100)
            if rand_num <= rock_chance:
                computer_choice = "batu"
            elif rand_num <= rock_chance + scissors_chance:
                computer_choice = "gunting"
            else:
                computer_choice = "kertas"
            print(f"Komputer memilih: {computer_choice}")

            # Menentukan pemenang berdasarkan aturan jankenpo
            if user_choice == "1" and computer_choice == "gunting" or \
                user_choice == "2" and computer_choice == "kertas" or \
                user_choice == "3" and computer_choice == "batu":
                print("Kamu menang!")
            elif user_choice == "1" and computer_choice == "batu" or \
                user_choice == "2" and computer_choice == "gunting" or \
                user_choice == "3" and computer_choice == "kertas":
                print("Seri!")
            else:
                print("Kamu kalah!")

            # Menampilkan pilihan untuk melanjutkan atau keluar
            play_again = input("Main lagi? (y/n): ")
            if play_again.lower() != "y":
                break

    elif level == "4":
        # Keluar dari program
        print("Terima kasih telah bermain! Sampai jumpa lagi.")
        break

else:
    # Menampilkan pesan error jika pilihan tidak valid
    print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
