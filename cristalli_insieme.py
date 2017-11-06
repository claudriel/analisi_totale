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
cutoff=150
binnaggio=10

if __name__ == '__main__':
    
    campioni_path ="./campioni/"
    dir_campioni_list= os.listdir(campioni_path)
        
    cristalli = np.array([])
    numero_cristalli = np.array([])
    media_array = np.array([])
    area_histo=np.zeros(binnaggio)
    frequenze_histo=np.zeros(binnaggio)   
    
   #########
   #dir_campioni_list: ['campione_1', 'campione_2', 'campione_3']
   #dir_date_list:['1', '2', '3', '4']
   
   ########
    fig=0
    for indice in dir_campioni_list:
        print indice
        dir_date_list= os.listdir(campioni_path+indice)
        dir_date_list.remove("mediePesate")
        dir_date_list.remove("numeroPesati")
        
        numeroC_array= np.array([])
        media_array = np.array([])
        cristalli = np.array([])
        numero_cristalli = np.array([])
        area_histo=np.zeros(binnaggio)
        frequenze_histo=np.zeros(binnaggio)   
        
        mediePesate_path=campioni_path+indice+'/mediePesate'
        medieInsieme_path=campioni_path+indice+'/mediePesate/medie'
        numeroPesati_path=campioni_path+indice+'/numeroPesati'
        numeroInsieme_path=campioni_path+indice+'/numeroPesati/numero'
        
        area_histo_tot=0
        frequenze_histo_tot=0
        somma_cristalli=np.zeros(13)
        media=np.zeros(13)
        dev=np.zeros(13)
        for date in dir_date_list:
            print date
            img_path =campioni_path+indice+'/'+date+"/img/"
            working_path =campioni_path+indice+'/'+date+"/histo"
            img_path =campioni_path+indice+'/'+date+"/img/"
            cristalli_path =campioni_path+indice+'/'+date+"/cristalli"
            media_path =campioni_path+indice+'/'+date+"/media"
            numero_cristalli_path = campioni_path+indice+'/'+date+"/numero_cristalli"
            
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
            numero_cristalli = np.array([])
            area_histo=np.zeros(binnaggio)
            frequenze_histo=np.zeros(binnaggio)  
            
            if date == "28giugno":
                i=0
                for temp in dir_temp_list:
                    print temp
                    dir_img_list=os.listdir(img_path+temp)
                    cristalli = np.array([])
                    numero_cristalli = np.array([])
                    lunghezza=0
                
                    for k in dir_img_list:
                        file_path=img_path+temp+"/"+k
                             
                        im = Image.open(file_path).convert("L")
                        I  = np.asarray(im)
                        
                        lx, ly = I.shape
                        crop_I = I[lx-502:lx-126, ly-376:ly]
            
                        lw,num = measurements.label(crop_I)
                        area = (measurements.sum(crop_I, lw, range(num + 1))/255)*5.3*5.3
                        
                        area=area[(area <= 1500)]
                        area=area[(area>cutoff)]
                    
                        cristalli = np.append(cristalli,area[0:])
                        lunghezza=len(area)+lunghezza
                        numero_cristalli=np.append(numero_cristalli, lunghezza)
                        
                    #np.savetxt(cristalli_path+'\cristalliOOOOOOOOO'+temp, cristalli)
                    media_singola=np.average(cristalli) #media di una temperatura di un campione (in base al ciclo)
                    media_array=np.append(media_array,media_singola) #alla fine del ciclo array con medie da 25->85 di un campione
                    numeroC_array=np.append(numeroC_array,lunghezza) #stessa cosa per cristalli
            
#                    FIGURA 1. aree cristalli in funzione della frequenza, histo e non
#                    weights=np.ones_like(cristalli)/float(len(cristalli))
                    plt.figure(1)
                    a=plt.hist(cristalli, bins=binnaggio,histtype='step',lw=2, label=temp)
                    
                    colori=['navy','mediumblue','blue','royalblue','dodgerblue','aqua','gold','orange','coral','tomato','red','firebrick','maroon']
                    plt.figure(2)
                    x=(a[1][0:binnaggio]+a[1][1:binnaggio+1])/2
                    y=a[0]
#                    
#                    plt.plot(x,y,color=colori[0+i],marker='o',label=temp)
#                    plt.legend(bbox_to_anchor=(0,1.01,1,0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=7)
#                    plt.savefig(working_path+"/HISTO_10_"+temp+date+".png", figuresize=(8,6), dpi=80, format="png")
#                    plt.xlabel('Area cristalli ($\mu$m$^2$)')
#                    plt.ylabel('Frequenze')
#                    i=i+1
##                    plt.hist(cristalli, bins=4, weights=weights)
##                    
##                    plt.savefig(working_path+"/HISTO_TOT"+temp+".png", figuresize=(8,6), dpi=80, format="png")
#                    
#                    
                    frequenze_histo=np.vstack([frequenze_histo,y])
                    area_histo=np.vstack([area_histo,x])
#                
                area_histo_tot=area_histo+area_histo_tot
                
                frequenze_histo_tot=frequenze_histo+frequenze_histo_tot
               # plt.clf() #cancella da un campione all'altro,le temperature me le sovrappone
               
                media=media_array*numeroC_array+media
                dev=np.vstack([dev,media_array])
                somma_cristalli=numeroC_array+somma_cristalli
            
            elif date == "29giugnoPomeriggio":
                i=0               
                for temp in dir_temp_list:
                    print temp
                    dir_img_list=os.listdir(img_path+temp)
                    cristalli = np.array([])
                    lunghezza=0
                
                    for k in dir_img_list:
                        file_path=img_path+temp+"/"+k
                             
                        im = Image.open(file_path).convert("L")
                        I  = np.asarray(im)
                        
                        lx, ly = I.shape
                        crop_I = I[ lx-482:lx-182, ly-300:ly]
            
                        lw,num = measurements.label(crop_I)
                        area = (measurements.sum(crop_I, lw, range(num + 1))/255)*5.3*5.3
                        
                        area=area[(area <= 1500)]
                        area=area[(area>cutoff)]
                       
                        cristalli = np.append(cristalli,area[0:])
                        lunghezza=len(area)+lunghezza
                        numero_cristalli=np.append(numero_cristalli, lunghezza)
                
                    #np.savetxt(cristalli_path+'\cristalliOOOOOOOOO'+temp, cristalli)
                    media_singola=np.average(cristalli)
                    media_array=np.append(media_array,media_singola)
                    numeroC_array=np.append(numeroC_array,lunghezza) #stessa cosa x numeri
            
#                    FIGURA 1. aree cristalli in funzione della frequenza, histo e non
                    #weights=np.ones_like(cristalli)/float(len(cristalli))
                    plt.figure(1)
                    a=plt.hist(cristalli, bins=binnaggio,histtype='step',lw=2, label=temp)
                    
                    colori=['navy','mediumblue','blue','royalblue','dodgerblue','aqua','gold','orange','coral','tomato','red','firebrick','maroon']
                    plt.figure(2)
                    x=(a[1][0:binnaggio]+a[1][1:binnaggio+1])/2
                    y=a[0]
#                   
#                    plt.plot(x,y,color=colori[0+i],marker='o',label=temp)
#                    plt.legend(bbox_to_anchor=(0,1.01,1,0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=7)
#                    plt.savefig(working_path+"/HISTO_10_"+temp+date+".png", figuresize=(8,6), dpi=80, format="png")
#                    plt.xlabel('Area cristalli ($\mu$m$^2$)')
#                    plt.ylabel('Frequenze')
#                    i=i+1
##                    plt.hist(cristalli, bins=4, weights=weights)
##                    
##                    plt.savefig(working_path+"/HISTO_TOT"+temp+".png", figuresize=(8,6), dpi=80, format="png")
#                   
                    area_histo=np.vstack([area_histo,x])
                    
                    frequenze_histo=np.vstack([frequenze_histo,y])
                   
                
                area_histo_tot=area_histo+area_histo_tot
               
                frequenze_histo_tot=frequenze_histo+frequenze_histo_tot
                #plt.clf()
                
                media=media_array*numeroC_array+media
                dev=np.vstack([dev,media_array])
                somma_cristalli=numeroC_array+somma_cristalli
            
            elif date == "14luglioPomeriggio":
                i=0
                for temp in dir_temp_list:
                    print temp
                    dir_img_list=os.listdir(img_path+temp)
                    cristalli = np.array([])
                    lunghezza=0
                
                    for k in dir_img_list:
                        file_path=img_path+temp+"/"+k
                             
                        im = Image.open(file_path).convert("L")
                        I  = np.asarray(im)
                        
                        lx, ly = I.shape
                        crop_I = I[ lx-482:lx-182, ly-300:ly]
            
                        lw,num = measurements.label(crop_I)
                        area = (measurements.sum(crop_I, lw, range(num + 1))/255)*5.3*5.3
                        
                        area=area[(area <= 1500)]
                        area=area[(area>cutoff)]
                    
                        cristalli = np.append(cristalli,area[0:])
                        lunghezza=len(area)+lunghezza
                        numero_cristalli=np.append(numero_cristalli, lunghezza)
                        
                
                    #np.savetxt(cristalli_path+'\cristalliOOOOOOOOO'+temp, cristalli)
                    media_singola=np.average(cristalli)
                    media_array=np.append(media_array,media_singola)
                    numeroC_array=np.append(numeroC_array,lunghezza)
            
#                    FIGURA 1. aree cristalli in funzione della frequenza, histo e non            
                    #weights=np.ones_like(cristalli)/float(len(cristalli))
                    plt.figure(1)
                    a=plt.hist(cristalli, bins=binnaggio,histtype='step',lw=2, label=temp)
                    
                    colori=['navy','mediumblue','blue','royalblue','dodgerblue','aqua','gold','orange','coral','tomato','red','firebrick','maroon']
                    plt.figure(2)
                    x=(a[1][0:binnaggio]+a[1][1:binnaggio+1])/2
                    y=a[0]
#                    
#                    plt.plot(x,y,color=colori[0+i],marker='o',label=temp)
#                    plt.legend(bbox_to_anchor=(0,1.01,1,0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=7)
#                    plt.savefig(working_path+"/HISTO_10_"+temp+date+".png", figuresize=(8,6), dpi=80, format="png")
#                    plt.xlabel('Area cristalli ($\mu$m$^2$)')
#                    plt.ylabel('Frequenze')
#                    i=i+1
##                    plt.hist(cristalli, bins=4, weights=weights)
##                    
##                    plt.savefig(working_path+"/HISTO_TOT"+temp+".png", figuresize=(8,6), dpi=80, format="png")
                    area_histo=np.vstack([area_histo,x])
                    frequenze_histo=np.vstack([frequenze_histo,y])
                    
                
                frequenze_histo_tot=frequenze_histo+frequenze_histo_tot
                area_histo_tot=area_histo+area_histo_tot
                
                #plt.clf()
               
                media=media_array*numeroC_array+media
                dev=np.vstack([dev,media_array])
                somma_cristalli=numeroC_array+somma_cristalli
                 
            else:
                i=0
                for temp in dir_temp_list:
                    print temp
                    dir_img_list=os.listdir(img_path+temp)
                    cristalli = np.array([])
                    lunghezza=0
                
                    for k in dir_img_list:
                    #print k
                        file_path=img_path+temp+"/"+k
                    
                    #apro le immagini, holo001,...etc per ogni cartella per ogni ciclo
                                                
                        im = Image.open(file_path).convert("L")
                        I  = np.asarray(im)
                   
                        #misuro l'area (5.3 è la dimensione dei pixel della mia camera)
                        lw,num = measurements.label(I)
                        area = (measurements.sum(I, lw, range(num + 1))/255)*5.3*5.3

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
                        area=area[(area>cutoff)]
                    
                        cristalli = np.append(cristalli,area[0:])
                        lunghezza=len(area)+lunghezza
                        numero_cristalli=np.append(numero_cristalli, lunghezza)

                    #np.savetxt(cristalli_path+'\cristalliOOOOOOOOO'+temp, cristalli)
                    media_singola=np.average(cristalli)
                    media_array=np.append(media_array,media_singola)
                    numeroC_array=np.append(numeroC_array,lunghezza)
            

#                    FIGURA 1. aree cristalli in funzione della frequenza, histo e non
               
                    #weights=np.ones_like(cristalli)/float(len(cristalli))
                    plt.figure(1)
                    a=plt.hist(cristalli, bins=binnaggio,histtype='step',lw=2, label=temp)
                    
                    colori=['navy','mediumblue','blue','royalblue','dodgerblue','aqua','gold','orange','coral','tomato','red','firebrick','maroon']
                    plt.figure(2)
                    x=(a[1][0:binnaggio]+a[1][1:binnaggio+1])/2
                    y=a[0]
#                    
#                    plt.plot(x,y,color=colori[0+i],marker='o',label=temp)
#                    plt.legend(bbox_to_anchor=(0,1.01,1,0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=7)
#                    plt.savefig(working_path+"/HISTO_10_"+temp+date+".png", figuresize=(8,6), dpi=80, format="png")
#                    plt.xlabel('Area cristalli ($\mu$m$^2$)')
#                    plt.ylabel('Frequenze')
#                    i=i+1
#                    plt.hist(cristalli, bins=4, weights=weights)
#                    
#                    plt.savefig(working_path+"/HISTO_TOT"+temp+".png", figuresize=(8,6), dpi=80, format="png")
                    area_histo=np.vstack([area_histo,x])
                    frequenze_histo=np.vstack([frequenze_histo,y])
                    
                
                frequenze_histo_tot=frequenze_histo+frequenze_histo_tot
                area_histo_tot=area_histo+area_histo_tot
                
                #plt.clf() #cancella da un campione all'altro,le temperature me le sovrappone
            
                
                media=media_array*numeroC_array+media
                dev=np.vstack([dev,media_array])
                somma_cristalli=numeroC_array+somma_cristalli
                 
            ######FIGURA 2. MEDIE AREE SINGOLE PER OGNI CAMPIONE in funzione della temperatura
            #####SALVO ARRAY CON LE MEDIE DI OGNI TEMPERATURA, formato txt e py
            #np.savetxt(media_path+'\media_array'+date, media_array)
            
            #np.save(medieInsieme_path+"/media_array_"+date, media_array)
            #temperatura= [25,30,35,40,45,50,55,60,65,70, 75, 80, 85]
            #plt.plot(temperatura,media_array, '-ro')
            #plt.xlabel('Temperatura ($^o$C)')
            #plt.ylabel('Media Area ($\mu$m$^2$)')
            #plt.savefig(media_path+"/"+"medie_"+date+"_singole"+".png", figuresize=(8,6), dpi=80, format="png")
            #plt.show()
            #plt.clf()
            
            
            ###FIGURA 3. NUMERO CRISTALLI SINGOLI
            #np.save(numeroInsieme_path+'/numeroC_'+date, numero_cristalli_media_array)
            #np.savetxt(numeroInsieme_path+'/sigmaC_'+date, numero_cristalli_sigma_array)
#            temperatura= [25,30,35,40,45,50,55,60,65,70, 75, 80, 85]
#            plt.plot(temperatura,numero_cristalli_media_array, '-ro')
#            plt.xlabel('Temperatura ($^o$C)')
#            plt.ylabel('Media Numero Cristalli')
#            plt.savefig(numero_cristalli_path+"/"+"NumeroCristalli_"+date+"_singole"+".png", figuresize=(8,6), dpi=80, format="png")
#            plt.show()
#            plt.clf()
#            
        media_finale=media/somma_cristalli
        
        if indice == "b2m_n76":
            diff=np.subtract(dev[1:],media_finale)*np.subtract(dev[1:],media_finale) #sottratto da ogni media singola la media tra le quattro
            somma=diff[0]+diff[1]+diff[2]
            deviazione=np.sqrt(somma/4)
        else:
            diff=np.subtract(dev[1:],media_finale)*np.subtract(dev[1:],media_finale) #sottratto da ogni media singola la media tra le quattro
            somma=diff[0]+diff[1]+diff[2]+diff[3]
            deviazione=np.sqrt(somma/4)
            
#           FIGURA 4. MEDIA PESATA DEI QUATTRO CAMPIONI
       # np.savetxt(mediePesate_path+"/mediePesate_"+indice, media)
       # np.savetxt(mediePesate_path+"/devS_"+indice, devS)
        
#        def func(x, A, B, C, D):
#            return A + B*(1/(1+np.exp((-(x)+C)/D)))
#        if indice == "b2m_n76":
#            xdata = np.linspace(0, 85, 2000)
#            plt.xlim([20,90])
#            plt.errorbar(temperatura,media_finale,yerr=deviazione,fmt='-o')
#            plt.plot(xdata, func(xdata, 287.70441,-113.95215,63.75305,2.81386), 'r-', label='fit')
#            plt.xlabel('Temperatura ($^o$C)')
#            plt.ylabel('Area Media dei quattro campioni Pesata ($\mu$m$^2$)')
#            plt.savefig(mediePesate_path+"/mediePesate_"+indice+".png", figuresize=(8,6), dpi=80, format="png")
#            plt.legend()
#            plt.show()
#        
#        else:
#            xdata = np.linspace(0, 85, 2000)
#            plt.xlim([20,90])
#            plt.errorbar(temperatura,media_finale,yerr=deviazione,fmt='-o')
#            plt.plot(xdata, func(xdata, 264.659,-65.4014,79.0663,1.55474), 'r-', label='fit')
#            plt.xlabel('Temperatura ($^o$C)')
#            plt.ylabel('Area Media dei quattro campioni Pesata ($\mu$m$^2$)')
#            plt.savefig(mediePesate_path+"/mediePesate_"+indice+".png", figuresize=(8,6), dpi=80, format="png")
#            plt.legend()
#            plt.show()
        

#           FIGURA 5. QUA FACCIO GRAFICO histo totale (a punti)
        eugenio=0
        claudio=[25,30,35,40,45,50,55,60,65,70,75,80,85]
        colore=['navy','mediumblue','blue','royalblue','dodgerblue','aqua','gold','orange','coral','tomato','red','firebrick','maroon']
        for count in range(1,14):
            plt.plot(area_histo_tot[count,:],frequenze_histo_tot[count,:],color=colore[0+eugenio],marker='o',label=claudio[count-1])
            plt.xlabel('Area cristalli ($\mu$m$^2$)')
            plt.ylabel('Frequenze')
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            eugenio=eugenio+1
        
        plt.show()
       # plt.savefig(working_path+"/HISTO_TOT_area"+".png", figuresize=(8,6), dpi=80, format="png")
        plt.clf()   
#        
     #FIGURA 6. QUA FACCIO GRAFICO CON LE QUATTRO MEDIE
#    temp=[25,30,35,40,45,50,55,60,65,70, 75, 80, 85]
#    for pippo in dir_campioni_list:
#        mediePesate_path=campioni_path+pippo+'/mediePesate'
#        file_list2=os.listdir(mediePesate_path)
#        file_list2.remove("pesate")
#        for lallo in file_list2:
#            
#            file_list3=os.listdir(mediePesate_path+'/medie/.')
#            plt.figure(fig)
#            print lallo
#            for gino in file_list3:
#                print gino
#                mediaInsieme = np.load(mediePesate_path+'/medie/'+gino)
#                
#                plt.plot(temp,mediaInsieme,'-o',label=gino)
#                plt.legend()
#                plt.xlabel('Temperatura ($^o$C)')
#                plt.ylabel('Area Media ($\mu$m$^2$)')
#        #print media
#        plt.savefig(mediePesate_path+'/pesate'+"/medie_"+pippo+".png", figuresize=(8,6), dpi=80, format="png")
#        plt.show()
#        #np.savetxt('media_pesata'+' '+i,media)
#    fig=fig+1    



    #FIGURA 7. QUA FACCIO GRAFICO CON il NUMEORO DEI CRISTALLI DEI QUATTRO CAMPIONI INSIEME
#    temp=[25,30,35,40,45,50,55,60,65,70, 75, 80, 85]
#    for pippo in dir_campioni_list:
#        numeroPesati_path=campioni_path+pippo+'/numeroPesati'
#        file_list2=os.listdir(numeroPesati_path)
#        file_list2.remove("pesati")
#        for lallo in file_list2:
#            
#            file_list3=os.listdir(numeroPesati_path+'/numero/.')
#            plt.figure(fig)
#            print lallo
#            for gino in file_list3:
#                print gino
#                numeroInsieme = np.load(numeroPesati_path+'/numero/'+gino)
#                if gino == "numeroC_14luglioMattina":
#                    sigma=[4.053087069493993333e+00,1.245920859036499273e+01,1.100006724024634330e+01,1.077695035822605263e+01,1.080204067943815360e+01,1.016498312765622991e+01,9.587564148729420310e+00,9.178014313867794982e+00,8.903165925868336217e+00,8.823612585174762657e+00,9.176037457228011007e+00,9.941280086782962044e+00,1.197928952965663285e+01]
#                    
#
#
#                elif gino == "numeroC_14luglioPomeriggio":
#                    
#                    sigma=[4.560085382777920415e+00,6.842993004120191181e+00,6.427106060093633388e+00,5.676164414075874021e+00,5.375316145924726285e+00,5.322115143338037591e+00,5.310910679886105434e+00,5.513289149729108551e+00,5.580812083455966466e+00,6.097002680940998509e+00,6.210139440698201341e+00,6.847579490013182557e+00,7.583965965956674715e+00]
#
#                elif gino == "numeroC_21giugno":
#                   sigma=[7.437809214893842835e+00,1.692214813884856994e+01,1.489765655867294036e+01,1.370395733886975265e+01,1.233808746795320310e+01,1.194585637573290171e+01,1.151718603678927266e+01,1.115414455834253360e+01,1.086634495583715498e+01,1.051351499198600159e+01,1.157958252008588573e+01,1.237513867154557978e+01,1.380592860237386610e+01]
#                elif gino == "numeroC_27luglio":
#                    sigma=[3.206493411812973093e+00,7.479357726641756798e+00,8.117412969719154603e+00,7.397472137422480998e+00,8.346105229845942830e+00,7.758031654413669820e+00,8.704601799509228854e+00,9.667491918796725869e+00,1.143263651894149291e+01,1.177977181442832588e+01,1.183474824470478381e+01,1.179126687694589037e+01,1.195279524894831091e+01]
#                elif gino == "numeroC_28giugno":
#                    sigma=[2.173849944859681305e+00,4.129558625067553557e+00,5.412018184411649280e+00,4.953183185451457859e+00,2.511806441116260835e+00,3.431493542030070731e+00,3.805166217240503190e+00,3.730769230769230838e+00,4.613398607536328910e+00,4.554788002750512099e+00,2.000000000000000000e+00,5.000000000000000000e-01,1.443204849176439764e+00]
#                elif gino == "numeroC_29giugnoMattina":
#                    
#                    sigma=[2.336993466302048184e+00,2.070860096303354325e+00,1.881473047482309369e+00,2.391970666341677987e+00,3.187475490101845832e+00,3.394071871053662814e+00,5.311811588333846146e+00,5.858531620762944314e+00,5.784683325862350678e+00,5.795298324587384364e+00,5.788345414499594277e+00,5.779180614189919574e+00,5.789976622080717839e+00]
#                else: 
#                    sigma=[5.441458210408428364e+00,6.644474280297761659e+00,6.105041513938828324e+00,5.553390336611431444e+00,6.397433842042730134e+00,6.248586296394132766e+00,6.307034177099224870e+00,6.270010495989818189e+00,6.762645992266204331e+00,7.498580680156338829e+00,7.966077160467201601e+00,8.151551003239966064e+00,8.459551560024149097e+00]
#                    
#                    plt.plot(temp, numeroInsieme, '-o')
#                #plt.legend()
#                
#                    plt.xlabel('Temperatura ($^o$C)')
#                    plt.ylabel('Numero Cristalli')
#        #print media
#        
#        plt.savefig(numeroPesati_path+'/pesati'+"/numero_"+pippo+".png", figuresize=(8,6), dpi=80, format="png")
#        plt.show()
#        #np.savetxt('media_pesata'+' '+i,media)
#    fig=fig+1    
#       
