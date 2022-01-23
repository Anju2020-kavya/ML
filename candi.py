import pandas as pd
import numpy as np
data=pd.read_csv('candi.csv')
concept=np.array(data)[:,:-1]
print("the concept is:",concept)
target=np.array(data)[:,-1]
print("label concept as:",target)
print("\n")
def learn(concept,target):
    specific_h=concept[0].copy()
    generic_h=[['?' for i in range (len(specific_h))] for i in range (len(specific_h))]
    for i,h,in enumerate(concept):
        if target[i]=='yes':
            for j in range (len(specific_h)):
                if h[j]!=specific_h[j]:
                    specific_h[j]='?'
                    generic_h[j][j]='?'
        elif target[i]=='no':
            for j in range (len(specific_h)):
                if h[j]!=specific_h[j]:
                    generic_h[j][j]=specific_h[j]
                else:
                    generic_h[j][j]='?'
    indices=[i for i,val in enumerate(generic_h) if val==['?' for i in range(len(specific_h))]]
    for i in indices:
        generic_h.remove(['?' for i in range (len(specific_h))])
    return generic_h,specific_h
s_final,g_final=learn(concept,target)
print("s_final:",s_final)
print("g_final:",g_final)