# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 11:40:02 2021

@author: Nik
"""

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":

    print ("\t \t Aplikasi PERHITUNGAN GAJI KARYAWAN CV. LOGOS")

    print ("=======================================================")
    
 #Nilai :
     
    Kode_Golongan=["1","2","3"]
    Gajipokok=[2500000,4500000,6500000]
    TunjanganIstri=[0.01,0.03,0.05]
    Tunjangan_Anak=0.02
    Biaya_Jabatan=0.005
    Iuran_pensiun=15500
    Iuran_Organisasi=3500
    
#Input 
    nama=input("Masukan Nama Karyawan \t: ")
    Golongan = input("Masukan Golongan               = ")
    Jenis_Kelamin=input("Masukan Jenis Kelamin Pria/Wanita \t: ")
    Status_Perkawinan=input("Masukan Kawin / Tidak Kawin\t: ")
    jml_anak=input("Masukan Jumlah Anak \t\t: ")
       
#MENENTUKAN PILIHAN
    index = 0 
    while index < len(Kode_Golongan):
        if Kode_Golongan[index] == Golongan: 
          Gajipokok[index]
        if Jenis_Kelamin== "Pria" and Status_Perkawinan =="Kawin": 
            Tunjangan_Istri=Gajipokok[index] * float(TunjanganIstri[index])
        else: 0
        
        if int(jml_anak) >=0 :
            TunjanganAnak =( Gajipokok[index])*float(Tunjangan_Anak)
        else :0
        
        Gaji_Bruto = (Gajipokok)[index]+(TunjanganAnak)+Tunjangan_Istri
    
#Perhitungan Biaya
        BiayaJabatan=Gaji_Bruto*Biaya_Jabatan
        Gaji_Netto=(Gaji_Bruto)-(Iuran_Organisasi+Iuran_pensiun)
        
#OUT PUT

        print("==================SLIP GAJI=========================")        
        import datetime
        saat_ini= datetime.datetime.now()
        print ("\t\t\t Tanggal:",saat_ini)
        print("Data Karyarawan======================================")
        print("Nama                         : " + str(nama) )
        print("Golongan                     : " + (Golongan))
        print("Jenis Kelamin                : " + (Jenis_Kelamin))
        print("Status Pernikahan            : " + (Status_Perkawinan))
        print("Pendapatan==========================================")
        print("Gaji Pokok                   : " + str(Gajipokok[index]))
        print("Tunjangan Istri              : " + str(Tunjangan_Istri))
        print("Tunjangan Anak               : " + str(TunjanganAnak))
        print("Gaji Bruto                   : " + str(Gaji_Bruto))
        print("Potongan============================================")
        print("Biaya Jabatan                : " + str(BiayaJabatan))
        print("Iuran pensiun                : " + str(Iuran_pensiun) )
        print("Iuran Organisasi             : " + str(Iuran_Organisasi))
        print("Potongan============================================")
        print("Gaji Bersih Yang diterima    : " + str(Gaji_Netto))
        
        index = index + 1
 #inputan untuk break
        JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
        if JawabUlang== "t" or JawabUlang =="T":
           break