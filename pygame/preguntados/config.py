import pygame

pygame.init()

# Botones
rect_boton_jugar = pygame.Rect(490, 250, 290, 70)
rect_boton_puntajes = pygame.Rect(490, 360, 290, 70)
rect_boton_salir = pygame.Rect(490, 470, 290, 70)
rect_boton_sonido = pygame.Rect(1150, 20, 100, 50)
rect_boton_pregunta = pygame.Rect(450, 20, 390, 100)
rect_boton_reiniciar = pygame.Rect(450, 200, 390, 100)
rect_boton_salir_puntaje = pygame.Rect(1150, 100, 100, 50)

# Contenedores de preguntas/respuestas
contenedor_preguntas = pygame.Rect(50, 350, 1180, 150)
contenedor_respuesta_a = pygame.Rect(50, 550, 300, 100)
contenedor_respuesta_b = pygame.Rect(450, 550, 300, 100)
contenedor_respuesta_c = pygame.Rect(880, 550, 300, 100)

# Textos/fonts
font = pygame.font.SysFont('Arial Narrow', 50)
font_puntajes = pygame.font.SysFont('Arial Narrow', 40)
font_unmute = pygame.font.SysFont('Arial Narrow', 30)
font_preguntas = pygame.font.SysFont('Arial Narrow', 60)
font_input = pygame.font.SysFont('Arial Narrow', 50)
font_guardar_puntaje = pygame.font.SysFont('Arial Narrow', 60)

texto_pregunta = font_preguntas.render('Pregunta', True, (255, 255, 255))
texto_reiniciar = font_preguntas.render('Reiniciar', True, (255, 255, 255))
texto_jugar = font.render('Jugar', True, (255, 255, 255))
texto_puntajes = font_puntajes.render('Ver puntajes', True, (255, 255, 255))
texto_salir = font.render('Salir', True, (255, 255, 255))
texto_mute = font_puntajes.render('Mute', True, (255, 255, 255))
texto_unmute = font_unmute.render('Unmute', True, (255, 255, 255))
texto_salir_puntaje = font_puntajes.render('Salir', True, (255, 255, 255))
texto_guardar_puntaje = font_guardar_puntaje.render('Ingrese su nombre:', True, (255,255,255))
texto_sala_puntajes = font_guardar_puntaje.render('Top 3 mejores puntajes!', True, (255,255,255))


# Colores
color_rojo = 255, 0, 0
color_amarillo = 255, 179, 0
color_celeste = 135, 206, 235
color_verde = 0, 255, 0

# Logos/fondos
logo_preguntados = pygame.image.load('pygame/preguntados/logo_preguntados.png')
logo_preguntados = pygame.transform.scale(logo_preguntados, (150, 150))
fondo_inicio = pygame.image.load('pygame/preguntados/maxresdefault.jpg')

# Sonidos
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('pygame/preguntados/soundtrack_fondo.mp3')  # soundtrack
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.05)
sonido_level_up = pygame.mixer.Sound('pygame/preguntados/level-passed-142971.mp3')  # sonido de acierto de pregunta
sonido_level_up.set_volume(0.1)
sonido_error = pygame.mixer.Sound('pygame/preguntados/error-126627.mp3') # sonido error pregunta
sonido_error.set_volume(0.4)

