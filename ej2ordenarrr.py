#import numpy as np
condiciones=[[2,1],[3,1],[4,2],[3,4],[0,2],[0,3]]

ayuda=[1,1,1,1,1]  

ayuda2=[]  

ayuda3=[]



def buscarsinsalida(x):
  
  ayuda[x]=0
  for y in range(len(condiciones)): #del 0 al 5
    
    
    if(condiciones[y][0]==x):
      
      if(ayuda[condiciones[y][1]]==1):
        
        buscarsinsalida(condiciones[y][1])
    
  ayuda2.append(x)  

for z in range(len(condiciones)-1):
  
  
  buscarsinsalida(z)
  if(len(ayuda2)>len(ayuda3)):
    ayuda3=ayuda2
  ayuda2=[]

print(ayuda3[::-1])