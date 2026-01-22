fichas = ['o', 'x']

def generar_tablero(n, movimientos_jugadores):
    tablero = []
    for i in range(n):
        fila = ['_' for i in range(n)]
        for j in range(n):
            casilla_vacia = True
            for k in range(len(movimientos_jugadores)):
                movimientos_jugador = movimientos_jugadores[k]
                if i in movimientos_jugador:
                    if j in movimientos_jugador[i]:
                        fila[j] = fichas[k]
        tablero.append(fila)
    return tablero



import pytest
def test_generar_tablero():
    mov_jugador_1 = {}
    mov_jugador_2 = {}
    movimientos_jugadores = [mov_jugador_1, mov_jugador_2]
    n = 3
    t = generar_tablero(n, movimientos_jugadores)
    assert len(t) == n
    for f in t:
        assert len(f) == n
def movimiento_valido(x, y, movimientos_otro_jugador):
    # Comprueba que el movimiento esté dentro del rango y no ocupado
    if x >= n or y >= n:
        return False
    if x in movimientos_otro_jugador:
        movimientos_en_columna = movimientos_otro_jugador[x]
        if y in movimientos_en_columna:
            return False
    return True
# Asegúrate de que n esté definida para los tests
n = 3 

def test_movimiento_fila_fuera_tablero():
    movimientos_otro_jugador = {}
    x = 1  # Fila mayor que el tamaño del tablero
    y = n + 1
    # Debe devolver False porque el movimiento está fuera de los límites [cite: 439, 440]
    assert False == movimiento_valido(x, y, movimientos_otro_jugador)

def test_movimiento_fila_y_columna_fuera_tablero():
    movimientos_otro_jugador = {}
    x = n + 1
    y = n + 1
    # Debe devolver False al estar ambos fuera de rango [cite: 461]
    assert False == movimiento_valido(x, y, movimientos_otro_jugador)
def test_movimiento_incorrecto():
    movimientos_otro_jugador = {2: [3]}
    x = 2
    y = 3
    assert False == movimiento_valido(x, y, movimientos_otro_jugador)
def jugada_ganadora(movimientos_jugador):
    # Comprobamos si hay 3 fichas en una fila
    for fila in movimientos_jugador:
        movimientos_columna = movimientos_jugador[fila]
        if len(movimientos_columna) == 3:
            return True
    return False

def test_no_ganador():
    movimientos_jugador = {2:[2,3]}
    assert False == jugada_ganadora(movimientos_jugador)
def test_ganador():
    movimientos_jugador = {2:[1,2,3]}
    assert True == jugada_ganadora(movimientos_jugador)
def mostrar_tablero(tablero):
    for fila in tablero:
        for celda in fila:
            print(celda, end=' ')
        print('\n')
if __name__ == "__main__":
    n = int(input('Introduce el tamaño del tablero cuadrado: '))
    casillas_libres = n * n
    jugador_activo = 0
    movimientos_jugador_1 = {}
    movimientos_jugador_2 = {}
    movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2]

    while casillas_libres > 0:
        tablero = generar_tablero(n, movimientos_jugadores)
        mostrar_tablero(tablero)
        
        casilla_jugador = input(f"JUGADOR {jugador_activo+1}: Introduce movimiento (x,y): ")
        casilla_jugador = casilla_jugador.strip()
        
        try:
            x = int(casilla_jugador.split(',')[0]) - 1
            y = int(casilla_jugador.split(',')[1]) - 1
            
            movimientos_jugador_activo = movimientos_jugadores[jugador_activo]
            movimientos_otro_jugador = movimientos_jugadores[(jugador_activo+1)%2]

            if movimiento_valido(x, y, movimientos_otro_jugador):
                mov_col = movimientos_jugador_activo.get(x, [])
                mov_col.append(y)
                movimientos_jugador_activo[x] = mov_col

                if jugada_ganadora(movimientos_jugador_activo):
                    tablero = generar_tablero(n, movimientos_jugadores)
                    mostrar_tablero(tablero)
                    print(f"ENHORABUENA EL JUGADOR {jugador_activo+1} HA GANADO")
                    break
            else:
                # Variables de sonido según pág. 16
                frequency = 2000 
                duration = 1000 
                print('\a') # Beep
                print("Movimiento invalido. Turno para el siguiente jugador")
            
            casillas_libres = casillas_libres - 1
            jugador_activo = (jugador_activo + 1) % 2
            
        except (ValueError, IndexError):
            print("Error: Introduce el formato correcto x,y (ejemplo: 1,2)")