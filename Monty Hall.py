#!/usr/bin/env python
# coding: utf-8

# In[125]:


#monty hall
import random
import numpy as np

print('Número de iterações: ')
n = input() #número de repetições
n= int(n)
troca = 0
mantem = 0

for i in range(0,n):
    listaPortas=[1,2,3]
    portaCerta = random.randrange(1,4)
    portaEscolhida= random.randrange(1,4)
    #print('portaCerta: ',portaCerta)
    #print('portaEscolhida:', portaEscolhida)
    
    pErradas = listaPortas.copy()
    pErradas.remove(portaCerta)
    #print('pErradas ',  pErradas)
    
    pSobrando = listaPortas.copy()
    pSobrando.remove(portaEscolhida)
    #print('pSobrando ',pSobrando)
    
    pElim = np.intersect1d(pErradas,pSobrando)
    pFinal= pErradas.copy()
    pFinal.remove(pElim[0])
    portaRestante = pFinal[0]
    #print('portaRestante ',portaRestante)
    
    
    if portaEscolhida==portaCerta:
        mantem=mantem + 1
    else:
        troca = troca+1
    if i%1000==0:
        print(i,'/',n)
print('Trocar ganha',troca,'vezes (',troca/n*100,'%)')
print('Manter ganha',mantem,'vezes (',mantem/n*100,'%)')



