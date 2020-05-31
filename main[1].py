# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:00:10 2020

@author: Sardor Mirzaev
"""
import os
os.chdir("") 
import pandas as pd
import function_0 as f0
import function_1 as f1
import function_2 as f2
 
LCR=['Unnamed: 2','Unnamed: 16'] 
FCR=['Unnamed: 3','Unnamed: 17']
#%%
############################################## 

import1= 'sample1.xlsm' # Datei auswählen
select_model=FCR        # FCR oder LCR auswählen
#LCR

###############################################

#%%
print("Loading  the required datasets...")
df=pd.read_excel(import1,'Stichtagsdaten',encoding='utf-8', index=True)
df=df.iloc[1:,:]

pd_df=pd.read_excel(import1,'Masterskala',encoding='utf-8', index=True)
pd_df2=pd_df.iloc[1:,:].reset_index()   #  Vector der PDs  

dfs=pd.DataFrame(df,columns=select_model) # Das Dataframe muss zwei Vektoren enthalten

dfs.columns=['ST1','ST2']             # Die Reihenfolge: ST1 -neue Stichtag, ST2 -alte Stichtag  
print("Loading is completed.")
#%%

### Matrixtabelle 
matrix_tabelle=f0.migmatrix(dfs,include_25th_rating=False)

### Ratings Stufe und Anzahl
counted=f0.abwechslung(dfs)

max_veschl_und_verb=f0.maximal_zahlen(dfs)  

### ROC curve
f1.plot_curve(dfs) 

### Trennschärfe gemessen (AUC, AR) 
A18,A19=f1.AUC_AR_gemessen(dfs)

### Trennschärfe Optimalmodell (AR) 
A21=f1.AR_optimal_model(dfs)    

A22=A19/A21  

### Implizite Trennschärfe (AR) 
pd_zu_stufe=pd_df2['Unnamed: 1']            # Die PD-Verteilung von Masterskala auswählen
anz_klassen=matrix_tabelle.iloc[0:25,26]    # Stichtag 2 auswählen 

A24=f1.AR_implizit(anz_klassen,pd_zu_stufe)

A25=A19/A24


### Die Anzahl der Kunden in Ratingstufe
counted=f2.anzahl_ratings(dfs)

### CT Central tendency ratio
ct_in_s1=f2.ct(dfs,matrix_tabelle.iloc[26,0:25],\
    True, pd_zu_stufe)                   # Stichtag 1 auswählen

ct_in_s2=f2.ct(dfs,matrix_tabelle.iloc[0:25, 26],\
    False, pd_zu_stufe)                 # Stichtag 2 auswählen 

print("Trennschärfe gemessen (AUC, AR) "+str( A18),str(A19),'\n')
print("Trennschärfe Optimalmodell AR) "+str( A21))
print('Quotient gemessen/opt '+str(A22),'\n')
print("Implizite Trennschärfe (AR) "+str( A24))
print('Quotient gemessen/implizit '+ str(A25),'\n')
print(counted)
print('CT in Stichtag_1 '+str(ct_in_s1),'\n','CT in Stichtag_2 ' +str(ct_in_s2))
#%%