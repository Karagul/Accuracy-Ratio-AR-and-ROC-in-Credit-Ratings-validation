# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:39:50 2020

@author: U0047365
"""

def migmatrix(dataframe,include_25th_class):
    import pandas as pd
    
    if isinstance (dataframe,pd.DataFrame) is False:
        print("The  type of variable must be pd.DataFrame")
        return
        
    elif dataframe.empty==True:
        print("The  Dataframe cannot be empty")
        return
        
    elif len(dataframe.shape) !=2:
        print("Dataframe length mismatch: Expected axis takes only 2 elements/columns")
        return
        
    else:
        dataframe.columns=['ST1','ST2']
        result2=dataframe.groupby('ST2').ST1.value_counts\
        (dropna=False).unstack()
        result3=dataframe.groupby('ST1').ST2.value_counts\
        (dropna=False).unstack()
        result2['unrated']=result2.iloc[0:,0]
        result3['unrated']=result3.iloc[0:,0]
        
        if include_25th_class is True:
            
            s1=pd.DataFrame(columns=range(0,26),index=range(0,26))
            for i in s1.index:
                for s in result2.index:
                    try:
                        if i== s:
                            s1.loc[i] = result2.loc[s,:]
                           
                        elif i != s:
                            s1.loc[i]=s1.loc[i,:]
                            
                        else:     
                            continue
                    except IndexError:
                        break
                
            s1['unrated']=result2['unrated']                 
            s1=s1.append(result3['unrated']) 
            
            # sum 'Stichtag2','Stichtag1'excluding unrated ratings,
            #change here  26 to 27 to get sum with unrated ratings                
            
            s1['Stichtag2']=s1.iloc[0:26].sum(axis=1)
            s1.loc["Stichtag1"]=s1.iloc[0:26,0:26].sum(axis=0)

    
            s1=s1.fillna(0)     
        elif include_25th_class is False : 
            
            s1=pd.DataFrame(columns=range(0,25),index=range(0,25))
            for i in s1.index:
                for s in result2.index:
                    try:
                        if i== s:
                            s1.loc[i] = result2.loc[s,:]
                           
                        elif i != s:
                            s1.loc[i]=s1.loc[i,:]
                            
                        else:     
                            continue
                    except IndexError:
                        break
                
            s1['unrated']=result2['unrated']                 
            s1=s1.append(result3['unrated'])                
            s1['Stichtag2']=s1.iloc[0:26].sum(axis=1)
            s1.loc["Stichtag1"]=s1.iloc[0:26,0:26].sum(axis=0)
    
            s1=s1.fillna('')
        else:
            pass
        print("-- Die Migrationsmatrix wurde erfolgreich erstellt --")
        
        return s1
        
def abwechslung(dataframe,include_5_notch):
 
    import pandas as pd 
    count00 = 0    
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count77 = 0
    
    dataframe.columns=['ST1','ST2']
    for idx, key in dataframe.dropna().iterrows(): 
        
        a= key['ST2'] - key['ST1']  
        
        if include_5_notch is True:

 
            if a is not None and a in range(-22,22):
                if a <=-5:
                    count00 = count00+1
                elif a == -4:
                    count0= count0+1    
                elif a == -3:
                    count1= count1+1
                elif a ==-2:
                    count2 = count2+1
                elif a ==-1:
                    count3 = count3+1
                elif a ==0:
                    count = count+1
                elif a ==1:     
                    count4 = count4+1
                elif a ==2:
                    count5 = count5+1
                elif a==3:
                    count6=count6+1
                elif a==4:
                    count7=count7+1
                elif a>=5:
                    count77=count77+1
                 
                else:
                    pass
            else:
                pass
        
            qs1=pd.DataFrame([count00,count0,count1,count2,count3,count,\
                            count4,count5,count6,count7,count77],columns=['Anzahl'])
            qs1.index=[\
            'Verschlechterung um mind. 5 Klassen','Verschlechterung um mind. 4 Klassen',\
            'Verschlechterung um mind. 3 Klassen','Verschlechterung um mind. 2 Klassen',\
            'Verschlechterung um mind. 1 Klasse','Gleichheit', \
            'Verbesserung um 1 Klasse','Verbesserung um 2 Klassen',\
            'Verbesserung um 3 Klassen','Verbesserung um 4 Klassen','Verbesserung um 5 Klassen']
        
        elif include_5_notch is False:
            
            if a is not None and a in range(-22,22):
                if a <=-4:
                    count0= count0+1    
                elif a == -3:
                    count1= count1+1
                elif a ==-2:
                    count2 = count2+1
                elif a ==-1:
                    count3 = count3+1
                elif a ==0:
                    count = count+1
                elif a ==1:     
                    count4 = count4+1
                elif a ==2:
                    count5 = count5+1
                elif a==3:
                    count6=count6+1
                elif a>=4:
                    count7=count7+1
                 
                else:
                    pass
            else:
                pass
            qs1=pd.DataFrame([count00,count0,count1,count2,count3,count,\
                            count4,count5,count6,count7,count77],columns=['Anzahl'])
            qs1.index=[\
            'Verschlechterung um mind. 5 Klassen','Verschlechterung um mind. 4 Klassen',\
            'Verschlechterung um mind. 3 Klassen','Verschlechterung um mind. 2 Klassen',\
            'Verschlechterung um mind. 1 Klasse','Gleichheit', \
            'Verbesserung um 1 Klasse','Verbesserung um 2 Klassen',\
            'Verbesserung um 3 Klassen','Verbesserung um 4 Klassen','Verbesserung um 5 Klassen']
        else:
            pass
    return qs1

def maximal_zahlen(dataframe):
    import pandas as pd
    a={}
    dfss=dataframe.dropna()
    
    for idx, key in dfss.iterrows():  
        
        a[idx]= key['ST2'] - key['ST1'] 
        
    aa=sorted(a.values())
    
    maxschlecht=aa[0]*(-1)  
    maxverbess=aa[-1]  
    
    qqs1=pd.DataFrame([maxschlecht, maxverbess], columns=['Anzahl'])     
    qqs1.index=['Maximale Verschlechterung','Maximale Verbesserung']
    
    return qqs1
    
def main():
    migmatrix()
    maximal_zahlen()
    abwechslung()
if __name__=="__main__":
    main()
print("Completed.")