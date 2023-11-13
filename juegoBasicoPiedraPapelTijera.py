# El jugador elige una opción en forma de número
# La opción elegida (variable resultado) va ser devuelta como entero cuando se llame a la función
def jugador():
    resultado = input('¿Qué opcion eliges? (1:Piedra, 2:Papel, 3:Tijera) ')
    return int(resultado)

## Función que ejecuta el ordenador para elegir de forma aleatoria
# Creo una lista con las opciones disponibles
# Selecciono una de forma aleatoria y la guardo en la variable
# Cuando se llame a esta función devolverá la elección al azar
# https://www.w3schools.com/python/module_random.asp
import random

def ordenador():
    opciones = ['Piedra','Papel','Tijera']
    opcion = random.choice(opciones)
    return(opcion)

# La variable ganador se inicializa en nulo (None) por si se ejecuta else se muestre el error y siga quedando vacia para continuar el juego
# Si jugador gana se muestra mensaje Has ganado esta tirada
# Si ordenador gana se muestra este mensaje He ganado esta vez
# Si hay empate se muestra mensaje Hemos empatado
# 1 = PIEDRA - 2 = PAPEL - 3 = TIJERA

def compara(jugador, ordenador):
    ganador = None
    
    if (jugador == 1 and ordenador == 'Tijera'): ganador = 'jugador'
    elif(jugador == 1 and ordenador == 'Papel'): ganador = 'ordenador'
    elif(jugador == 1 and ordenador == 'Piedra'): ganador = 'empate'
    elif(jugador == 2 and ordenador == 'Piedra'): ganador = 'jugador'
    elif(jugador  == 2 and ordenador == 'Papel'): ganador = 'empate'
    elif(jugador == 2 and ordenador == 'Tijera'): ganador = 'ordenador'
    elif(jugador == 3 and ordenador == 'Piedra'): ganador = 'ordenador'
    elif(jugador  == 3 and ordenador == 'Papel'): ganador = 'jugador'
    elif(jugador == 3 and ordenador == 'Tijera'): ganador = 'empate'
    else: print('Ha habido un error')
    return(ganador)

# Pregunto el nombre al jugador
# Explicar reglas del juego
# Inicializo las variables que van a contener los puntos de ambos a 0
nombre_jugador = input('¿Cual es tu nombre?')
print('Hola %s. Vamos a jugar a PIEDRA-PAPEL-TIJERAS. A 10 tiradas. El que consigas mas puntos gana.'%nombre_jugador)
puntos_j = 0
puntos_o = 0

# Para ejecutar las 10 tiradas uso un bucle for con un rango de 10 - range()
# Recibo las tiradas de jugador y ordenador en tirada_jugador y tirada_ordenador
# Paso los valores a la funcion compara() para que me devuelva un ganador
for n in range(10):
    tirada_jugador = jugador()
    tirada_ordenador = ordenador()
    ganador = compara(tirada_jugador, tirada_ordenador)
    
# Comparaciones y eleccion del ganador
# Si el ganador es jugador muestro los valores de la tirada, muestro que el ganador es el jugador y sumo 1 a la variable (puntos_j) que almacena los puntos del jugador
# Mismo procedimiento para la tirada ganadora de ordenador
# Para el empate igual. Si no se cumplen ninguna de las anteriores muestro un Error
    if ganador == 'jugador':
        print('\n Yo he sacado %s'%tirada_ordenador)
        print('\n ¡¡¡Enhorabuena!!! Tu eres el ganador de esta tirada')
        puntos_j =+ 1
    elif ganador == 'ordenador':
        print('\n Mi tirada es %s'%tirada_ordenador)
        print('\n Esta vez he ganado yo ¡¡¡Jajaja!!!')
    elif ganador == 'empate':
        print('\n Ahora he sacado %s'%tirada_ordenador)
        print('\n ¡Vaya! Has tenido suerte. Hemos empatado, volvamos a jugar ')
    else: print('Ha ocurrido un error')
        
# Muestra de resultados
# Si los puntos del jugador son mas que los de ordenador, creo una variable para almacenarlos (puntos_finales)
# Igual para ordenador
# Si hay empate de puntos, muestro el aviso y los puntos conseguidos por ambos
if puntos_j > puntos_o:
    puntos_finales = puntos_j
    print('\n La partida ha acabado')
    print('\n ¡¡¡Eres el ganador con {} puntos!!!'.format(puntos_finales))
elif puntos_j < puntos_o:
    puntos_finales = puntos_o
    print('\n ¡¡¡He ganado!!! He conseguido {} puntos. Verguenza para ti :D'.format(puntos_finales))
else:
    print('Ha habido un empate de puntos, tu con {} y yo con {}'.format(puntos_j, puntos_o))