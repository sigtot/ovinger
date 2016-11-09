#Del 8 - Opptaksgrenser
# -*- coding: utf-8 -*-
fil=open("poenggrenser_2011.csv","r")
poenggrenser=fil.read().splitlines()
fil.close()

def drittstudier(fil):
    for linje in fil:
        print(linje)

drittstudier(poenggrenser)
