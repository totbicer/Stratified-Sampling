#!/usr/bin/env python 3
# -*- coding: UTF-8 -*-
karsilama= """
_____________________________________________________________________________________
S T R A T I F I E D    S A M P L I N G    P R O G R A M 
                                   Version: (P).3.1
by Tülin (Otbiçer) ACAR \u00A9 2019 (P)arantez Education Research Consultancy and Publishing
https://parantezanaliz.com & totbicer@gmail.com
_____________________________________________________________________________________"""
print(karsilama)

def girdiler_al(mesaj:str) -> int:

    while True:
        girdi = input(mesaj)
        try:
            girdi = int(float(girdi))
        except ValueError:
            print("You logged in incorrectly. You must enter a naturel number greater than zero.")
            girdi=1
            continue

        if girdi<=0:
            print("You logged in incorrectly. You must enter a naturel number than zero.")
        else:
            alinan_veri = girdi
            break
    return alinan_veri

def main():

    evren = girdiler_al("1# The size of the universe defined and limited (N) : ")
    orneklem = girdiler_al("2# The sample size (Ss) : ")
    tabaka_sayisi = girdiler_al("3# Number of stratum (h) : ")
    N=int(evren)
    O=int(orneklem)
    tlar = []

    for i in range(tabaka_sayisi):
        veri = girdiler_al("4# Enter the unit/observation number on the {}. stratum (Nh): ".format(i+1))
        tlar.append(veri)

    if sum(tlar) != evren:
        print("\nError. Check the number of units / observations in the stratums, the size of the universe or the number of stratum. The number of the universe and the number of units in the stratums should be equal. \n\n")
        main()
        
    else:
        for sayi in tlar:
            print("\n Universe representation rate= {}, number of sample for stratum (Fh)= {}" .format(round((sayi/N),2), int((sayi/N)*O)))

if __name__ == "__main__":
    main()

    a=input()
