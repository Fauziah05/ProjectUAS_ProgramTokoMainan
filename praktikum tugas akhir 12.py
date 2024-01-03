class TokoMainan:
    def __init__(self):
        self.stok_mainan = {'Boneka': 10, 'Lego': 15, 'Kartu Uno': 20}
        self.harga_mainan = {'Boneka': 50000, 'Lego': 100000, 'Kartu Uno': 20000}

    def tampilkan_menu(self):
        print("\nSelamat datang di Toko Mainan!")
        print("1. Lihat Stok Mainan")
        print("2. Beli Mainan")
        print("3. Keluar")

    def lihat_stok(self):
        print("\nStok Mainan:")
        for mainan, stok in self.stok_mainan.items():
            print(f"{mainan}: {stok} unit")

    def beli_mainan(self, mainan, jumlah):
        if mainan in self.stok_mainan and jumlah <= self.stok_mainan[mainan]:
            total_harga = self.harga_mainan[mainan] * jumlah
            diskon = self.hitung_diskon(total_harga)
            total_bayar = total_harga - diskon

            print(f"\nAnda telah membeli {jumlah} {mainan}.")
            print(f"Total harga: Rp{total_harga:,}")
            print(f"Diskon: Rp{diskon:,}")
            print(f"Total bayar setelah diskon: Rp{total_bayar:,}")

            self.stok_mainan[mainan] -= jumlah
        else:
            print("\nMaaf, stok tidak mencukupi atau mainan tidak tersedia.")

    def hitung_diskon(self, total_harga):
        if total_harga >= 500000:
            return 20000
        elif total_harga >= 250000:
            return 10000
        else:
            return 0

if __name__ == "__main__":
    toko = TokoMainan()

    while True:
        toko.tampilkan_menu()

        pilihan = input("Silakan pilih menu (1/2/3): ")

        if pilihan == '1':
            toko.lihat_stok()
        elif pilihan == '2':
            mainan = input("Masukkan nama mainan yang ingin dibeli: ")
            jumlah = int(input("Masukkan jumlah mainan yang ingin dibeli: "))
            toko.beli_mainan(mainan, jumlah)
        elif pilihan == '3':
            print("Terima kasih telah berbelanja di Toko Mainan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
