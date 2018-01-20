import sys
import os
import numpy as np


from Proteina import *

if __name__ == '__main__':

    campioni_path ="../campioni/"
    

    proteina=["b2m_G60", "b2m_n76", "b2m_WT"]
    crop = [[[410,0,512,102],[300,0,512,212], [340,0,512,172]], [[502,126,376,0],[512,0,512,0],[482,182,300,0]], [[512,0,512,0],[482,182,300,0],[512,0,512,0],[512,0,512,0]]]
    
    
    k=0
    for i in proteina:
        date= os.listdir(campioni_path+i)
        date.remove("mediePesate")
        date.remove("numeroPesati")
        p = Proteina(i, crop[k], 0, 1500, date)
        p.graf_media_aree()
        
        k=k+1
    

