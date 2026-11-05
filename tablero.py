# tablero.py
import random
from dimensiones import TAMANO_GRID, TAMANO_CASILLA
from casilla import Casilla

class Tablero:
    def __init__(self):
        self.casillas = []
        self.casilla_vacia = None
        self.movimientos = 0
        self.crear_tablero()
        self.mezclar_tablero()

    def crear_tablero(self):
        # Crea lista del 1 al 15 y añadir el 0 al final
        numeros = list(range(1, TAMANO_GRID * TAMANO_GRID)) + [0]
        
        contador = 0
        for fila in range(TAMANO_GRID):
            for columna in range(TAMANO_GRID):
                num = numeros[contador]
                # Instanciando objetos de la clase Casilla que importamos
                nueva_casilla = Casilla(num, fila, columna)
                self.casillas.append(nueva_casilla)
                if nueva_casilla.vacia:
                    self.casilla_vacia = nueva_casilla
                contador += 1

    def obtener_casilla_en_posicion(self, fila, columna):
        for casilla in self.casillas:
            if casilla.fila == fila and casilla.columna == columna:
                return casilla
        return None

    def manejar_clic(self, x_pixel, y_pixel):
        columna_click = x_pixel // TAMANO_CASILLA
        fila_click = y_pixel // TAMANO_CASILLA

        casilla_clicada = self.obtener_casilla_en_posicion(fila_click, columna_click)
        
        if casilla_clicada and not casilla_clicada.vacia:
            distancia_fila = abs(casilla_clicada.fila - self.casilla_vacia.fila)
            distancia_columna = abs(casilla_clicada.columna - self.casilla_vacia.columna)

            if (distancia_fila == 1 and distancia_columna == 0) or (distancia_fila == 0 and distancia_columna == 1):
                self._intercambiar_posiciones(casilla_clicada)

    def manejar_teclado(self, tecla):
        import pygame
        fila_buscar = self.casilla_vacia.fila
        columna_buscar = self.casilla_vacia.columna

        if tecla == pygame.K_UP:
            fila_buscar += 1
        elif tecla == pygame.K_DOWN:
            fila_buscar -= 1
        elif tecla == pygame.K_LEFT:
            columna_buscar += 1
        elif tecla == pygame.K_RIGHT:
            columna_buscar -= 1
        else:
            return

        if 0 <= fila_buscar < TAMANO_GRID and 0 <= columna_buscar < TAMANO_GRID:
            pieza_a_mover = self.obtener_casilla_en_posicion(fila_buscar, columna_buscar)
            if pieza_a_mover:
                self._intercambiar_posiciones(pieza_a_mover)

    def _intercambiar_posiciones(self, pieza_a_mover):
        # Método auxiliar 
        temp_fila, temp_columna = pieza_a_mover.fila, pieza_a_mover.columna
        pieza_a_mover.fila = self.casilla_vacia.fila
        pieza_a_mover.columna = self.casilla_vacia.columna
        self.casilla_vacia.fila = temp_fila
        self.casilla_vacia.columna = temp_columna
        self.movimientos += 1

    def mezclar_tablero(self):
        for _ in range(100):
            movimientos_posibles = []
            for casilla in self.casillas:
                dist_f = abs(casilla.fila - self.casilla_vacia.fila)
                dist_c = abs(casilla.columna - self.casilla_vacia.columna)
                if (dist_f == 1 and dist_c == 0) or (dist_f == 0 and dist_c == 1):
                    movimientos_posibles.append(casilla)
            
            pieza_a_mover = random.choice(movimientos_posibles)
            # Intercambio rápido sin sumar al contador de movimientos del jugador
            temp_f, temp_c = pieza_a_mover.fila, pieza_a_mover.columna
            pieza_a_mover.fila = self.casilla_vacia.fila
            pieza_a_mover.columna = self.casilla_vacia.columna
            self.casilla_vacia.fila = temp_f
            self.casilla_vacia.columna = temp_c

    def verificar_victoria(self):
        for casilla in self.casillas:
            if casilla.vacia:
                if casilla.fila != TAMANO_GRID - 1 or casilla.columna != TAMANO_GRID - 1:
                    return False
            else:
                fila_correcta = (casilla.numero - 1) // TAMANO_GRID
                columna_correcta = (casilla.numero - 1) % TAMANO_GRID
                if casilla.fila != fila_correcta or casilla.columna != columna_correcta:
                    return False
        return True

    def dibujar(self, superficie, fuente):
        for casilla in self.casillas:
            casilla.dibujar(superficie, fuente)
