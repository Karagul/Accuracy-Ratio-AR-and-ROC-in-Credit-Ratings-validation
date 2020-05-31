# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:08:19 2020

@author: U0047365
"""

def anzahl_ratings(dataframe):
    '''
    Counts the number of borrowers in each and both arrays.
    '''
    import pandas as pd
    import numpy as np
    
    if isinstance (dataframe,pd.DataFrame) is False:
        print("The  type of variable must be pd.DataFrame")
        return
        
    elif dataframe.empty==True:
        print("The  Dataframe cannot be empty")
        return
    
    dfs=dataframe
    fs2=dfs.dropna()
    ausgefall=fs2[(fs2.ST1>=22)&(fs2.ST2<=21)]    
    anz_tatz_aus=len(ausgefall)  
           
    # Anzahl ratings 
    anz_in_S1=len(dfs[dfs.ST1<=24])
    davon_lebend_S1=len(dfs[(dfs.ST1<=21)])
    davon_ausfall_S1=len(dfs[(dfs.ST1>=22)])       
           
    anz_in_S2=len(dfs[(dfs.ST2<=24)]) 
    davon_lebend_S2=len(dfs[(dfs.ST2<=21)])
    davon_ausfall_S2=len(dfs[(dfs.ST2>=22)])
    
    anz_in_beide=len(dfs[(dfs.ST1<=24)&(dfs.ST2<=24)])
    
    x=list([anz_in_S1,davon_lebend_S1,davon_ausfall_S1,\
    anz_in_beide,anz_tatz_aus])
    
    y=list([anz_in_S2,davon_lebend_S2,davon_ausfall_S2,'',''])
    
    results=pd.DataFrame(np.column_stack([x,y]),\
    columns=['Stichtag1','Stichtag2'])
    results.index=['Anzahl','davon lebend','davon ausgefallen',\
    'Anzahl Ratings in beiden Verteilungen', 'Ausfälle']
    
    return results
    
    
def ct(dataframe,alive,Stichtag_1,pd_zu_stufe):
    '''
    Calculates the Central tencency  of two given arrays.
    Variable alive is the summary list of all customers 
    categorised into rated as well as  unrated rating classes
    Boolean variable Stichtag_1 points at CT calcualtion from 
    one of the arrays.
    As **True** selected variable, the function returns to CT 
    calculation from first array.
    '''
    import pandas as pd 
    if alive is  None :
        print('The  target variable alive should contain list or series of elements')
        return
    elif pd_zu_stufe is  None:
        print('The target variable pd_zu_stufe should contain list or series of elements')
        return
    elif isinstance (dataframe,pd.DataFrame) is False:
        print("The  type of variable must be pd.DataFrame")
        return
        
    elif dataframe.empty==True:
        print("The  Dataframe cannot be empty")
        return
    else:
        dataframe=dataframe
        davon_lebend_S1=len(dataframe[(dataframe.ST1<=21)])
        davon_lebend_S2=len(dataframe[(dataframe.ST2<=21)])
        
        if Stichtag_1 is True:
            
            if davon_lebend_S1>0:
                mt=0
                for i in range(0,22):
                    mt=mt+alive[i]*pd_zu_stufe[i]
                
                mt=mt/davon_lebend_S1      
            else:
                mt=-1
                
        if Stichtag_1 is False:
            if davon_lebend_S2>0:
                mt=0
                for i in range(0,22):
                    mt=mt+alive[i]*pd_zu_stufe[i]
                
                mt=mt/davon_lebend_S2      
            else:
                mt=-1
            
        return mt*100  , "{:.2%}".format(mt)     

def main():
    ct()
    anzahl_ratings()
if __name__ =="__main__":
    main()
    
print("Completed.")