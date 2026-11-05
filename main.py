# main.py
import pygame
from dimensiones import ANCHO_VENTANA, ALTO_VENTANA, COLOR_FONDO
from tablero import Tablero

def main():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Rompecabezas Deslizante 15")
    reloj = pygame.time.Clock()
    
    # Fuentes
    fuente_piezas = pygame.font.SysFont("Arial", 40, bold=True)
    fuente_victoria = pygame.font.SysFont("Arial", 50, bold=True)

    # Creamos la instancia única del tablero modular
    tablero = Tablero()
    juego_terminado = False
    ejecutando = True

    while ejecutando:
        # 1. Monitoreo de 0Entadas
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            
            # Clic del Ratón
            elif evento.type == pygame.MOUSEBUTTONDOWN and not juego_terminado:
                if evento.button == 1:  
                    x_click, y_click = evento.pos
                    tablero.manejar_clic(x_click, y_click)
                    if tablero.verificar_victoria():
                        juego_terminado = True

            # Pulsación del Teclado
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r: # Reiniciar juego con 'R'
                    tablero = Tablero()
                    juego_terminado = False
                elif evento.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT] and not juego_terminado:
                    tablero.manejar_teclado(evento.key)
                    if tablero.verificar_victoria():
                        juego_terminado = True

        # 2. Ilustración del juego
        ventana.fill(COLOR_FONDO)
        tablero.dibujar(ventana, fuente_piezas)

        # Mostrar cartel si el usuario logra el objetivo
        if juego_terminado:
            cartel = fuente_victoria.render("¡Uuupa, ganaste!", True, (0, 255, 100))
            cartel_rect = cartel.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
            
            fondo_texto = pygame.Rect(0, 0, 500, 100)
            fondo_texto.center = cartel_rect.center
            pygame.draw.rect(ventana, (20, 20, 20), fondo_texto)
            
            ventana.blit(cartel, cartel_rect)

        # Actualizar título de la ventana con las estadísticas en tiempo real
        pygame.display.set_caption(f"Rompecabezas 15 | Movimientos: {tablero.movimientos}")

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
