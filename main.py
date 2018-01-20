import sys
import os
import numpy as np


from Proteina import *

if __name__ == '__main__':

    campioni_path ="../campioni/"
    date= os.listdir(campioni_path+"b2m_G60")
    date.remove("mediePesate")
    date.remove("numeroPesati")


    p1 = Proteina("b2m_G60", [[410,0,512,102],[340,0,512,172],[300,0,512,212]], 0, 1500, date)

