# casilla.py
import pygame
from dimensiones import TAMANO_CASILLA, COLOR_PIEZA, COLOR_BORDE, COLOR_TEXTO

class Casilla:
    def __init__(self, numero, fila, columna):
        self.numero = numero  
        self.fila = fila      
        self.columna = columna  
        self.vacia = (numero == 0) 

    def dibujar(self, superficie, fuente):
        if self.vacia:
            return

        # coordenadas lógicas a píxeles en pantalla
        x = self.columna * TAMANO_CASILLA
        y = self.fila * TAMANO_CASILLA
        rectangulo = pygame.Rect(x, y, TAMANO_CASILLA, TAMANO_CASILLA)

        # Dibujar base azul y bordes oscuros
        pygame.draw.rect(superficie, COLOR_PIEZA, rectangulo)
        pygame.draw.rect(superficie, COLOR_BORDE, rectangulo, 4)

        # Centrar y mostrar el texto del número
        texto_superficie = fuente.render(str(self.numero), True, COLOR_TEXTO)
        texto_rect = texto_superficie.get_rect(center=rectangulo.center)
        superficie.blit(texto_superficie, texto_rect)
