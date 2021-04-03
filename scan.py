#!usr/bin/python

#Import urllib
import urllib

def banner():
    print "hidyatcode.com"
    print "My Channel hidayatcode"

def scan():
#Memasukkan url target ke dalam suatu variabel bernama "target"
    target = raw_input("Masukkan target:")

#Apabila url tidak diawali dengan http maka akan ditambahkan.Urllib tidak dapat membuka url tanpa protokol http/https
    if not target.startswith("http://"):
        target = "http://"+target

#Menambahkan /robots.txt di akhir url untuk proses scan
    scanrobot = target+"/robots.txt"
   
#Buka url dengan urllib kemudian disimpan di variabel bernama "robots"
    robots = urllib.urlopen(scanrobot)

#Apabila halaman dapat dibuka (HTTP Response code 200 OK) maka akan dilanjutkan ke membedakan antara halaman error dengan file robots.txt yg asli
    if robots.getcode() == 200:

#Karena pada robots.txt tak ada tag html,maka disini menggunakan tag html untuk membedakan antara robots.txt asli atau bukan
        html = "<html>"

#Simpan seluruh isi halaman di dalam variabel "baca"
        baca = robots.read()

#Apabila ada tag <html> dalam halaman maka kondisi ini berlaku untuk memberitahu pengguna bahwa robots.txt tidak ada
        if html in baca:
            print "Robots.txt tidak ada!"

#Memberitahukan bahwa ada robots.txt kemudian memperlihatkannya kepada pengguna scanner
        else:
            print "Isi robots.txt:",baca

#Apabila http response code bukan 200 OK maka kondisi ini berlaku
    else:
        print "Robots.txt tidak ada!"

#Urutkan semua fungsi kedalam satu fungsi "utama"

def utama():
    banner()
    scan()

#Panggil fungsi "utama"

utama()

   