#mendefinisikan kelas
class MyFile(object):
    def __init__(self, namafile):
        #mengakses file
        self.file = open(namafile)
    def __del__(self):
        #menutup file
        self.file.close()
    def bacadata(self):
        for baris in self.file:
            print(baris, end="")

def main():
    #membuat objek dari kelas MyFile
    f = MyFile("E:/Tugas TeKom/SEMESTER 3/Pemrograman Lanjut/Praktikum Kelas dan Objek/Beritaku.txt")

    #memanggil metode bacadata()
    f.bacadata()

if __name__ == "__main__":
    main()
