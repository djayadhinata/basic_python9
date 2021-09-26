NilaiT = 60
NilaiP = 60

if (NilaiT >= 70 and NilaiP >= 70) :
      print("Selamat, anda lulus")
elif(NilaiT >= 70 and NilaiP <= 70):
    print("Anda harus Mengulang Ujian Praktek.")
elif(NilaiT <= 70 and NilaiP >= 70):
    print("Anda harus Mengulang Ujian Teori.")
else :
    print("Anda harus mengulang ujian teori dan praktek.")