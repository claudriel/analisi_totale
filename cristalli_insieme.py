# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:35:27 2017

@author: Claudia
"""

import sys
import os
import matplotlib
matplotlib.use('Agg')
from pylab import *
from scipy.ndimage import measurements
from PIL import Image
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    dir_campioni_list= os.listdir('.')
        
    dir_campioni_list.remove("cristalli_insieme.py")
    cristalli = np.array([])
    media_array = np.array([])
    
    
   
   #########
   #dir_campioni_list: ['campione_1', 'campione_2', 'campione_3']
   #dir_date_list:['1', '2', '3', '4']
   
   ########
    
    for indice in dir_campioni_list:
        print indice
        dir_date_list= os.listdir(indice)
        dir_date_list.remove("mediePesate")
        
        media_25=np.array([])
        media_30=np.array([])
        media_35=np.array([])
        media_40=np.array([])
        media_45=np.array([])
        media_50=np.array([])
        media_55=np.array([])
        media_60=np.array([])
        media_65=np.array([])
        media_70=np.array([])
        media_75=np.array([])
        media_80=np.array([])
        media_85=np.array([])
        
        numeroC_25=np.array([])
        numeroC_30=np.array([])
        numeroC_35=np.array([])
        numeroC_40=np.array([])
        numeroC_45=np.array([])
        numeroC_50=np.array([])
        numeroC_55=np.array([])
        numeroC_60=np.array([])
        numeroC_65=np.array([])
        numeroC_70=np.array([])
        numeroC_75=np.array([])
        numeroC_80=np.array([])
        numeroC_85=np.array([])
        
        numeroC_array= np.array([])
        media_array = np.array([])
        cristalli = np.array([])
        
        mediePesate_path=indice+'/mediePesate'
        
        for date in dir_date_list:
            print date
            img_path =indice+'/'+date+"/img/"
            working_path =indice+'/'+date+"/histo"
            img_path =indice+'/'+date+"/img/"
            cristalli_path =indice+'/'+date+"/cristalli"
            media_path =indice+'/'+date+"/media"
            
            try: 
                os.stat(media_path)  #contrololla se esiste il cammino "working_path"
            except: 
                os.makedirs(media_path) #se non esiste crealo
        
            dir_temp_list=os.listdir(img_path)
            
            
            try: 
                os.stat(working_path)  #contrololla se esiste il cammino "working_path"
            except: 
                os.makedirs(working_path) #se non esiste crealo
        
            dir_temp_list=os.listdir(img_path)
            
            numeroC_array= np.array([])
            media_array = np.array([])
            cristalli = np.array([])
            
            for temp in dir_temp_list:
                print temp
                dir_img_list=os.listdir(img_path+temp)
                cristalli = np.array([])
                n=0
                
                for k in dir_img_list:
                    #print k
                    file_path=img_path+temp+"/"+k
                    
                    #apro le immagini, holo001,...etc per ogni cartella per ogni ciclo
                    if date != '14luglioPomeriggio':
                            
                        im = Image.open(file_path).convert("L")
                        I  = np.asarray(im)
                   
                        #misuro l'area (5.3 è la dimensione dei pixel della mia camera)
                        lw,num = measurements.label(I)
                        area = (measurements.sum(I, lw, range(num + 1))/255)*5.3*5.3
                    
                    else :
                        lx, ly = I.shape            
                        crop_I = I[ lx-370:lx-15, ly-346:ly-1]
        
        
                        #misuro l'area (5.3 è la dimensione dei pixel della mia camera)
                        lw,num = measurements.label(crop_I)
                        area = (measurements.sum(crop_I, lw, range(num + 1))/255)*5.3*5.3    
               
                    ########
                    #per vedere i cristalli colorati e plottare aree.
                    #plt.figure(1)
                    #plt.imshow(lw)
            
                    #plt.figure(2)
                    #plt.plot(area,'o')
                    #plt.show()
                    ##########
            
                    #maschere : da cosa parto e fino dove arrivo a leggere l'array delle aree
                    area=area[(area <= 1500)]
                    area=area[(area>1)]
                    
                    cristalli = np.append(cristalli,area[0:])
                    n=n+num
                
                ####SALVA I CRISTALLI IN .TXT NELLA CARTELLA CRISTALLI
                #np.savetxt(cristalli_path+'\cristalli'+temp, cristalli)
                
                
                media_singola=np.average(cristalli)
                media_array=np.append(media_array,media_singola)
               
                numeroC_array=np.append(numeroC_array,n)
                
                
                #########
                #HISTOGRAMMA con bin>110
                
                #cristalli=cristalli[(cristalli>110)]
                #weights=np.ones_like(cristalli)/float(len(cristalli))
                #plt.hist(cristalli, bins=4, weights=weights)
                #plt.xlabel('Area xtals')
                #plt.ylabel('Frequenze')
                #plt.savefig(working_path+"/HISTO_TOT"+temp+".png", figuresize=(8,6), dpi=80, format="png")
                #plt.clf() #altrimenti se non lo cancello l'istogramma, mi sovrappone a quello del ciclo prima.
                
            ####salvo array con solo tempe 25, 30, etc di ogni set di capioni
            
            
            media_25_singola=media_array[0]
            media_25=np.append(media_25,media_25_singola)
                        
            media_30_singola=media_array[1]
            media_30=np.append(media_30,media_30_singola)
            
            media_35_singola=media_array[2]
            media_35=np.append(media_35,media_35_singola)
            
            media_40_singola=media_array[3]
            media_40=np.append(media_40,media_40_singola)
            
            media_45_singola=media_array[4]
            media_45=np.append(media_45,media_45_singola)
            
            media_50_singola=media_array[5]
            media_50=np.append(media_50,media_50_singola)
            
            media_55_singola=media_array[6]
            media_55=np.append(media_55,media_55_singola)
            
            media_60_singola=media_array[7]
            media_60=np.append(media_60,media_60_singola)
            
            media_65_singola=media_array[8]
            media_65=np.append(media_65,media_65_singola)
            
            media_70_singola=media_array[9]
            media_70=np.append(media_70,media_70_singola)
            
            media_75_singola=media_array[10]
            media_75=np.append(media_75,media_75_singola)
            
            media_80_singola=media_array[11]
            media_80=np.append(media_80,media_80_singola)
            
            media_85_singola=media_array[12]
            media_85=np.append(media_85,media_85_singola)
            
            
            numeroC_25_singola=numeroC_array[0]
            numeroC_25=np.append(numeroC_25,numeroC_25_singola)
                        
            numeroC_30_singola=numeroC_array[1]
            numeroC_30=np.append(numeroC_30,numeroC_30_singola)
            
            numeroC_35_singola=numeroC_array[2]
            numeroC_35=np.append(numeroC_35,numeroC_35_singola)
            
            numeroC_40_singola=numeroC_array[3]
            numeroC_40=np.append(numeroC_40,numeroC_40_singola)
            
            numeroC_45_singola=numeroC_array[4]
            numeroC_45=np.append(numeroC_45,numeroC_45_singola)
            
            numeroC_50_singola=numeroC_array[5]
            numeroC_50=np.append(numeroC_50,numeroC_50_singola)
            
            numeroC_55_singola=numeroC_array[6]
            numeroC_55=np.append(numeroC_55,numeroC_55_singola)
            
            numeroC_60_singola=numeroC_array[7]
            numeroC_60=np.append(numeroC_60,numeroC_60_singola)
            
            numeroC_65_singola=numeroC_array[8]
            numeroC_65=np.append(numeroC_65,numeroC_65_singola)
            
            numeroC_70_singola=numeroC_array[9]
            numeroC_70=np.append(numeroC_70,numeroC_70_singola)
            
            numeroC_75_singola=numeroC_array[10]
            numeroC_75=np.append(numeroC_75,numeroC_75_singola)
            
            numeroC_80_singola=numeroC_array[11]
            numeroC_80=np.append(numeroC_80,numeroC_80_singola)
            
            numeroC_85_singola=numeroC_array[12]
            numeroC_85=np.append(numeroC_85,numeroC_85_singola)
            
            
            
            #print media_array
            #print media_25, media_30
            
            
            ###MEDIE SINGOLE
            #####SALVO ARRAY CON LE MEDIE DI OGNI TEMPERATURA, formato txt e py
            #np.savetxt(media_path+'\media_array'+date, media_array)
            #np.save(media_path+'\media_array'+date, media_array)
            temperatura= [25,30,35,40,45,50,55,60,65,70, 75, 80, 85]
            #plt.plot(temperatura,media_array, '-ro')
            #plt.xlabel('Temperatura ($^o$C)')
            #plt.ylabel('Media Area Pesata ($\mu$m$^2$)')
            #plt.savefig(media_path+"/"+"medie_"+date+"_singole"+".png", figuresize=(8,6), dpi=80, format="png")
            #plt.show()
        
        media_finale_25=sum(np.multiply(media_25,numeroC_25))/sum(numeroC_25)
        
        somma=0
        for i in media_25:
            dev_25=(i-media_finale_25)*(i-media_finale_25)
            somma=somma+dev_25
        devS_25=np.sqrt(somma/4)
        
       
        media_finale_30=sum(np.multiply(media_30,numeroC_30))/sum(numeroC_30)
        
        somma=0
        for i in media_30:
            dev_30=(i-media_finale_30)*(i-media_finale_30)
            somma=somma+dev_30
        devS_30=np.sqrt(somma/4)
        
        
        media_finale_35=sum(np.multiply(media_35,numeroC_35))/sum(numeroC_35)
        
        somma=0
        for i in media_35:
            dev_35=(i-media_finale_35)*(i-media_finale_35)
            somma=somma+dev_35
        devS_35=np.sqrt(somma/4)
        
        
        media_finale_40=sum(np.multiply(media_40,numeroC_40))/sum(numeroC_40)
        
        somma=0
        for i in media_40:
            dev_40=(i-media_finale_40)*(i-media_finale_40)
            somma=somma+dev_40
        devS_40=np.sqrt(somma/4)
        
        
        media_finale_45=sum(np.multiply(media_45,numeroC_45))/sum(numeroC_45)
        
        somma=0
        for i in media_45:
            dev_45=(i-media_finale_45)*(i-media_finale_45)
            somma=somma+dev_45
        devS_45=np.sqrt(somma/4)
        
        
        media_finale_50=sum(np.multiply(media_50,numeroC_50))/sum(numeroC_50)
        
        somma=0
        for i in media_50:
            dev_50=(i-media_finale_50)*(i-media_finale_50)
            somma=somma+dev_50
        devS_50=np.sqrt(somma/4)
        
        
        media_finale_55=sum(np.multiply(media_55,numeroC_55))/sum(numeroC_55)
        
        somma=0
        for i in media_55:
            dev_55=(i-media_finale_55)*(i-media_finale_55)
            somma=somma+dev_55
        devS_55=np.sqrt(somma/4)
        
        
        media_finale_60=sum(np.multiply(media_60,numeroC_60))/sum(numeroC_60)
        
        somma=0
        for i in media_60:
            dev_60=(i-media_finale_60)*(i-media_finale_60)
            somma=somma+dev_60
        devS_60=np.sqrt(somma/4)
        
        
        media_finale_65=sum(np.multiply(media_65,numeroC_65))/sum(numeroC_65)
        
        somma=0
        for i in media_65:
            dev_65=(i-media_finale_65)*(i-media_finale_65)
            somma=somma+dev_65
        devS_65=np.sqrt(somma/4)
        
        
        media_finale_70=sum(np.multiply(media_70,numeroC_70))/sum(numeroC_70)
        
        somma=0
        for i in media_70:
            dev_70=(i-media_finale_70)*(i-media_finale_70)
            somma=somma+dev_70
        devS_70=np.sqrt(somma/4)
        
        
        media_finale_75=sum(np.multiply(media_75,numeroC_75))/sum(numeroC_75)
        
        somma=0
        for i in media_75:
            dev_75=(i-media_finale_75)*(i-media_finale_75)
            somma=somma+dev_75
        devS_75=np.sqrt(somma/4)
        
        
        media_finale_80=sum(np.multiply(media_80,numeroC_80))/sum(numeroC_80)
        
        somma=0
        for i in media_80:
            dev_80=(i-media_finale_80)*(i-media_finale_80)
            somma=somma+dev_80
        devS_80=np.sqrt(somma/4)
        
        
        media_finale_85=sum(np.multiply(media_85,numeroC_85))/sum(numeroC_85)
        
        somma=0
        for i in media_85:
            dev_85=(i-media_finale_85)*(i-media_finale_85)
            somma=somma+dev_85
        devS_85=np.sqrt(somma/4)
        
        media=[media_finale_25,media_finale_30,media_finale_35,media_finale_40,media_finale_45,media_finale_50,media_finale_55,media_finale_60,media_finale_65,media_finale_70,media_finale_75,media_finale_80,media_finale_85]      
        devS=[devS_25,devS_30,devS_35,devS_40,devS_45,devS_50,devS_55,devS_60,devS_65,devS_70,devS_75,devS_80,devS_85]
        
        np.savetxt(mediePesate_path+"/mediePesate_"+indice, media)
        np.savetxt(mediePesate_path+"/devS_"+indice, devS)
        
        
        plt.errorbar(temperatura,media,yerr=devS,fmt='-o')
        plt.xlabel('Temperatura ($^o$C)')
        plt.ylabel('Area Media dei quattro campioni Pesata ($\mu$m$^2$)')
        plt.savefig(mediePesate_path+"/mediePesate_"+indice+".png", figuresize=(8,6), dpi=80, format="png")
        plt.legend()
        plt.show()
        
        
        
            