import sys
import os
from pylab import *
from scipy.ndimage import measurements
from PIL import Image
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt


class Proteina:

    def __init__(self, name, crop, min_area_cutoff, max_area_cutoff, dates):
        self.name   = name 
        self.dates  = dates
        self.crop   = crop
        
        somma_cristalli=np.zeros(13)
        media=np.zeros(13)

        cristalli = np.array([])
        numeroC_array= np.array([])
        numero_cristalli = np.array([])
        media_aree_array = np.array([])
       
        k=0
        for date in dates:
            img_path = "../campioni/"+name+"/"+date+"/img/" #sono una cartella sotto
            temperatures=os.listdir(img_path)
            media_array = np.array([])
            media_aree_array = np.array([])
            numeroC_array = np.array([])
            for temp in temperatures:
                images=os.listdir(img_path+temp)
	        lunghezza = 0
                cristalli = np.array([])
                numero_cristalli = np.array([])
                for i in images:
                    file_path=img_path+temp+"/"+i
                
                    im = Image.open(file_path).convert("L")
                    I  = np.asarray(im)
                
                    lx, ly = I.shape
                    crop_I = I[lx-self.crop[k][0]:lx-self.crop[k][1], ly-self.crop[k][2]:ly-self.crop[k][3]]
                
                    lw,num = measurements.label(crop_I)
                    area = (measurements.sum(crop_I, lw, range(num + 1))/255)*5.3*5.3

                    area = area[(area<=max_area_cutoff)]
                    area = area[(area>min_area_cutoff)]
                
                    cristalli = np.append(cristalli,area[1:])
                    lunghezza=len(area)+lunghezza
                    numero_cristalli=np.append(numero_cristalli, lunghezza)
            
	    	
                media_singola_aree=np.average(cristalli)
                media_aree_array=np.append(media_aree_array,media_singola_aree)
                numeroC_array=np.append(numeroC_array,lunghezza) #(forse ok)

            media=media_aree_array*numeroC_array+media 
            somma_cristalli=numeroC_array+somma_cristalli
            k=k+1

        self.temp = temperatures
        self.media_aree = media/somma_cristalli




    def log(self):
        print "Proteina         = "+self.name
        print "Giorni di Misura = ",(len(self.dates))
        print "Range Temp.      = ",self.temp[0],self.temp[len(self.temp)-1]


    def graf_media_aree(self):
        
        plt.errorbar(self.temp, self.media_aree/np.amax(self.media_aree), fmt='-o')
        plt.xlabel('Temperatura ($^o$C)')
        plt.ylabel('Area Media dei quattro campioni Pesata ($\mu$m$^2$)')
        plt.savefig(self.name+".png", figuresize=(8,6), dpi=80, format="png")
        plt.clf()

    def test2(self):
        return 0
