#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random


# In[20]:


def crearMapaLaberinto(numeroFilas, numeroColumnas, numeroParedes, numeroEspacios, numeroJugador):
    #crear mapa lleno de paredes
    mapaLaberinto = []
    numeroParedesGeneradas = 0
    for fila in range(0, numeroFilas):
        filaMapaLaberinto = []
        for columna in range(0, numeroColumnas):
#             if (random.randrange(2) == 1 and numeroParedesGeneradas < numeroParedes):
#                 filaMapaLaberinto.append('#')
#                 numeroParedesGeneradas += 1
#             else:
#                 filaMapaLaberinto.append('')
            filaMapaLaberinto.append('#')
        mapaLaberinto.append(filaMapaLaberinto)
#Se ubica un punto de inicio aleartorio y a partir del punto se generan espacios
    numeroEspaciosGenerados = 0
    filaPosicionActual = random.randrange(numeroFilas)
    columnaPosicionActual = random.randrange(numeroColumnas)
    mapaLaberinto[filaPosicionActual][columnaPosicionActual] = ''
    numeroEspaciosGenerados += 1
#Se ubica al jugador en un punto aleatorio
    jugadorPosicionFila = random.randrange(numeroFilas)
    jugadorPosicionColumna = random.randrange(numeroColumnas)
    mapaLaberinto[filaPosicionActual][columnaPosicionActual] = 'o'
    
    while numeroEspaciosGenerados < numeroEspacios:
        direccion = random.randrange(4)
        if direccion == 0 and filaPosicionActual > 0:
            filaPosicionActual -=1
        elif direccion == 1 and filaPosicionActual < numeroFilas -1:
            filaPosicionActual += 1
        elif direccion == 2 and columnaPosicionActual > 0:
            columnaPosicionActual -= 1
        else:
            if columnaPosicionActual <numeroColumnas -1:
                columnaPosicionActual += 1
                
        if mapaLaberinto[filaPosicionActual][columnaPosicionActual] == '#':
            mapaLaberinto[filaPosicionActual][columnaPosicionActual] = ''
            numeroEspaciosGenerados += 1
            
    return mapaLaberinto


# In[21]:


numeroFilas = int(input('Introduzca el número de filas del laberinto: '))
numeroColumnas = int(input('Introduzca el número de columnas del laberinto: '))
numeroParedes = int(input('Introduzca el número de paredes del laberinto: '))
numeroEspacios = numeroFilas * numeroColumnas - numeroParedes
numeroJugador= int(input('Introduzca el numero de jugadores: '))


# In[22]:


laberinto = crearMapaLaberinto(numeroFilas, numeroColumnas, numeroParedes, numeroEspacios, numeroJugador)

for filaMapaLaberinto in laberinto:
    print(filaMapaLaberinto)

