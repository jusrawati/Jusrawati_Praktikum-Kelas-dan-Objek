class KelilingLingkaran(object):
    def __init__(self,r):
        self.jarijari = r
    def hitungKeliling(self):
        return 2 * 3.14 * self.jarijari
    def cetakdatakeliling(self):
        print('-KELILING')
        print('phi\t        :  3,14')
        print('jarijari\t: ', self.jarijari)
    def cetakkeliling(self):
        print('Kelilingnya\t= ', self.hitungKeliling())

class LuasLingkaran(object):
    def __init__(self,r):
        self.jarijari = r
    def hitungLuas(self):
        return 3.14 * (self.jarijari * self.jarijari)
    def cetakdataluas(self):
        print('-LUAS')
        print('phi\t        :  3,14')
        print('jarijari\t: ', self.jarijari)
    def cetakluas(self):
        print('Luasnya\t	= ', self.hitungLuas())

def main():
   #lingkaran pertama
    Lingkaran11 = KelilingLingkaran(4)
    Lingkaran12 = LuasLingkaran(4)

    print('LINGKARAN 1')
    Lingkaran11.cetakdatakeliling()
    Lingkaran11.cetakkeliling()
    Lingkaran12.cetakdataluas()
    Lingkaran12.cetakluas()

    print(' ')

    #lingkaran kedua
    Lingkaran21 = KelilingLingkaran(8)
    Lingkaran22 = LuasLingkaran(8)

    print('LINGKARAN 2')
    Lingkaran21.cetakdatakeliling()
    Lingkaran21.cetakkeliling()
    Lingkaran22.cetakdataluas()
    Lingkaran22.cetakluas()

if __name__ == "__main__":
    main()
