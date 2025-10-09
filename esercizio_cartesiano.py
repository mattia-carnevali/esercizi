#dato un insieme di 20 punti su un piano cartesiano, random compresi nell'intervallo 0,10 calcolare
#il punto con ascissa massima e il punto con coordinata minima

import random

x = []
y = []

for i in range (0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))
    
punti_cartesiano = []
for i in range (0,20):
    punto = (random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)