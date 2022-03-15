#from asyncio import ThreadedChildWatcher
from statistics import mean
from time import perf_counter_ns
#from turtle import speed
import simples as sp
import mtrhead as mt
import matplotlib.pyplot as plt
import numpy as np

with open("data.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))
simples = []
thread = []
speedUp = []
ThreadsQtdd = 0
ThreadsQtddList = []
mediaThreadList = []

print('\n\nanalise de %d valores\n\n'%(len(data)))

for j in range(0, 10):
    ThreadsQtdd = ThreadsQtdd + 20
    
    print("\nUtilizando %d Threads:"%ThreadsQtdd)

    for i in range(0, 20):
        start1 = perf_counter_ns()
        primo_sp = sp.resolve_simples(data)
        finish1 = perf_counter_ns()

        start2 = perf_counter_ns()
        primo_mt = mt.resolve_trhread(data, ThreadsQtdd)
        finish2 = perf_counter_ns()

        simples.append((finish1-start1)/1000000)
        thread.append((finish2-start2)/1000000)
        speedUp.append((finish1-start1)/(finish2-start2))
    
    mediaSimples = mean(simples)
    mediaThread = mean(thread)
    mediaSpeedUp = mean(speedUp)

    ThreadsQtddList.append(ThreadsQtdd)
    mediaThreadList.append(mediaThread)    

    print('simples          > threads (%d)'%ThreadsQtdd)
    print('%f segundos   > %f segundos  : tempo execucao medio:'%(mediaSimples/1000,mediaThread/1000))
    print('%d            > %d           :numeros primos encontrados'%(primo_sp,primo_mt))
    print('Speed Up médio: %f' %(mediaSpeedUp))