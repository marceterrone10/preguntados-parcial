import json
import pygame
from datos import lista
from biblioteca_funciones import *
from config import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Preguntados")

# Variables/banderas
running = True
sonido_on = True
mostrar_contenedor = False
pantalla = 'Inicio'
contador_pregunta = 0
intentos = 2
puntaje = 0
respuestas_incorrectas = []

# Variables para almacenar el nombre de usuario
nombre_usuario = ''
input_activo = False
puntajes = []
lista_puntajes = []
pasada = True
nombre_archivo = 'pygame/preguntados/puntajes.json'

# Funciones
def render_preguntas(index_pregunta: int):
    ''' 
    Renderiza las preguntas a medida que avanza el juego, por medio de un contador que sirve como index de la lista de preguntas. Si la respuesta es incorrecta se fija en la lista_incorrecta y si es asi dibuja un rectangulo del tamanio del contenedor de la respuesta del mismo color del fondo para simular que se oculta dicha respuesta incorrecta.
    Args:
    index_pregunta:int, contador que sirve para avanzar el programa a medida que el usuario acierta o no las respuestas.
    
    '''
    pregunta = lista[index_pregunta]
    texto_question = font.render(pregunta['pregunta'], True, (0, 0, 0))
    respuesta_a = font_unmute.render('a )' + pregunta['a'], True, (0, 0, 0))
    respuesta_b = font_unmute.render('b )' + pregunta['b'], True, (0, 0, 0))
    respuesta_c = font_unmute.render('c )' + pregunta['c'], True, (0, 0, 0))
    screen.blit(texto_question, (60, 360))

    if 'a' not in respuestas_incorrectas: #verifica que la respuesta no este en la lista de incorrectas
        screen.blit(respuesta_a, (60, 550)) #si es asi muestra el texto de dicha respuesta
    else:
        pygame.draw.rect(screen, (0, 0, 255), contenedor_respuesta_a) #si se encuentra en la lista de incorrectas dibuja un rectangulo del color del fondo en el surface de la respuesta para hacer efecto de ocultarla
    if 'b' not in respuestas_incorrectas:
        screen.blit(respuesta_b, (450, 550))
    else:
        pygame.draw.rect(screen, (0, 0, 255), contenedor_respuesta_b)
    if 'c' not in respuestas_incorrectas:
        screen.blit(respuesta_c, (880, 550))
    else:
        pygame.draw.rect(screen, (0, 0, 255), contenedor_respuesta_c)

def render_puntajes(lista: list):
    '''
    Renderiza los tres mejores puntajes y sus contenedores con sus respectivos nombres y puntos. A medida que la lista se va llenando de datos toma dichos puntajes y los vuelca en los contenedores.
    Args:
    lista de puntajes ordenada descendientemente.
    '''
    contenedor_puntajes_uno = pygame.Rect(50, 200, 1180, 100)
    contenedor_puntajes_dos = pygame.Rect(50, 350, 1180, 100)
    contenedor_puntajes_tres = pygame.Rect(50, 500, 1180, 100)
    pygame.draw.rect(screen, (255, 255, 255), contenedor_puntajes_uno)
    pygame.draw.rect(screen, (255, 255, 255), contenedor_puntajes_dos)
    pygame.draw.rect(screen, (255, 255, 255), contenedor_puntajes_tres)
    #empieza condicion que si el largo de la lista es mayor a X cantidad se muestra el 1ero, 2do, 3er valor de la lista descendiente
    #asi quedando los tres mejores puntajes
    if len(lista) > 0:
        puntaje_1 = font_puntajes.render(f'1) {lista[0]["nombre"]}: {lista[0]["puntos"]} puntos', True, (0, 0, 0))
        screen.blit(puntaje_1, (60, 220)) #renderizo en pantalla el puntaje uno 
    if len(lista) > 1:
        puntaje_2 = font_puntajes.render(f'2) {lista[1]["nombre"]}: {lista[1]["puntos"]} puntos', True, (0, 0, 0))
        screen.blit(puntaje_2, (60, 370))
    if len(lista) > 2:
        puntaje_3 = font_puntajes.render(f'3) {lista[2]["nombre"]}: {lista[2]["puntos"]} puntos', True, (0, 0, 0))
        screen.blit(puntaje_3, (60, 520))

# Ejecución del programa
while running:
    for event in pygame.event.get():  # Iteración para click
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pantalla == 'Inicio':
                if rect_boton_salir.collidepoint(event.pos):  # Botón salir
                    running = False
                elif rect_boton_jugar.collidepoint(event.pos):  # Botón jugar
                    pantalla = 'preguntas'  # Cambio bandera de pantalla a preguntas
                elif rect_boton_puntajes.collidepoint(event.pos):  # Botón sala puntajes
                    pantalla = 'sala_puntajes'  # Cambio bandera a pantalla de sala de puntajes
                    ordenar_lista_por_parametro(lista_puntajes, 'DESC', 'puntos') #automaticamente se ordena de la lista descendiente para que muestre los tres con mas puntajes

            if pantalla == 'preguntas':  # Pantalla preguntas - ejecución de juego
                if rect_boton_pregunta.collidepoint(event.pos):  # Botón pregunta
                    intentos = 2
                    mostrar_contenedor = True  # Cambio estado de mostrar_contenedor
                    respuestas_incorrectas = []  # Reiniciar respuestas incorrectas

                if mostrar_contenedor:
                    if contenedor_respuesta_a.collidepoint(event.pos):
                        if lista[contador_pregunta]['correcta'] == 'a': #entra en la condicion si la respuesta es la correcta
                            contador_pregunta += 1 #suma contador lo que significa que pasa a la siguiente pregunta por medio del index de la lista
                            puntaje += 10 #sumar puntaje
                            mostrar_contenedor = False #oculto contenedor de preguntas y respuestas por medio de la bandera
                            sonido_level_up.play()
                        elif 'a' not in respuestas_incorrectas:
                            intentos -= 1
                            respuestas_incorrectas.append('a')#si la respuesta es incorrecta se agrega a la lista
                            sonido_error.play()
                    elif contenedor_respuesta_b.collidepoint(event.pos):
                        if lista[contador_pregunta]['correcta'] == 'b':
                            contador_pregunta += 1
                            puntaje += 10
                            mostrar_contenedor = False
                            sonido_level_up.play()
                        elif 'b' not in respuestas_incorrectas:
                            intentos -= 1
                            respuestas_incorrectas.append('b')
                            sonido_error.play()
                    elif contenedor_respuesta_c.collidepoint(event.pos):
                        if lista[contador_pregunta]['correcta'] == 'c':
                            contador_pregunta += 1
                            puntaje += 10
                            mostrar_contenedor = False
                            sonido_level_up.play()
                        elif 'c' not in respuestas_incorrectas:
                            intentos -= 1
                            respuestas_incorrectas.append('c')
                            sonido_error.play()
                    if intentos == 0: #si intentos llega a 0 se ejecuta la condicion
                        contador_pregunta += 1 #pasa a la siguiente pregunta
                        mostrar_contenedor = False #se oculta el contenedor de pregs y respuestas
                        respuestas_incorrectas = [] #se reinicia la lista de incorrectas

                if rect_boton_reiniciar.collidepoint(event.pos): #al precionar reiniciar se reinicia los scores, intentos, listas incorrectas y el contador de pregs
                    contador_pregunta = 0
                    puntaje = 0
                    intentos = 2
                    respuestas_incorrectas = []

                if contador_pregunta >= len(lista):
                    pantalla = 'pantalla_final'
                    input_activo = True #activa bandera de input para ingresar nombre


            if pantalla == 'sala_puntajes':
                if rect_boton_salir_puntaje.collidepoint(event.pos):
                    pantalla = 'Inicio'

            if rect_boton_sonido.collidepoint(event.pos):  # boton mutear/desmutear soundtrack
                sonido_on = mutear_desmutear_soundtrack(sonido_on)

        if event.type == pygame.KEYDOWN:
            if pantalla == 'pantalla_final' and input_activo:
                if event.key == pygame.K_RETURN:
                    # Almaceno el nombre
                    input_activo = False
                    pantalla = 'Inicio'
                    puntajes.append({'nombre': nombre_usuario, 'puntos': puntaje})
                    extraer_json(nombre_archivo, pasada, puntajes)
                    lista_puntajes = importar_json(nombre_archivo)

                elif event.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                else:
                    nombre_usuario += event.unicode

    # renderizar en pantalla
    if pantalla == 'Inicio':
        screen.blit(fondo_inicio, (0, 0))
        screen.blit(logo_preguntados, (550, 20))
        pygame.draw.rect(screen, (color_celeste), rect_boton_jugar, border_radius=10)
        screen.blit(texto_jugar, (580, 280))
        pygame.draw.rect(screen, (color_amarillo), rect_boton_puntajes, border_radius=10)
        screen.blit(texto_puntajes, (580, 390))
        pygame.draw.rect(screen, (color_rojo), rect_boton_salir, border_radius=10)
        screen.blit(texto_salir, (600, 500))
    elif pantalla == 'preguntas':
        screen.fill((0, 0, 255))
        screen.blit(logo_preguntados, (100, 20))
        pygame.draw.rect(screen, (color_amarillo), rect_boton_pregunta, border_radius=10)
        screen.blit(texto_pregunta, (540, 60))
        pygame.draw.rect(screen, (color_amarillo), rect_boton_reiniciar, border_radius=10)
        screen.blit(texto_reiniciar, (540, 240))
        texto_puntos = font.render(f'+{puntaje} puntos', True, (0, 0, 0))
        texto_intentos = font.render(f'{intentos} intentos', True, (0, 0, 0))
        screen.blit(texto_intentos, (1070, 260))
        screen.blit(texto_puntos, (1070, 138))
        
        if mostrar_contenedor:
            pygame.draw.rect(screen, (255, 255, 255), contenedor_preguntas)
            pygame.draw.rect(screen, (255, 255, 255), contenedor_respuesta_a)
            pygame.draw.rect(screen, (255, 255, 255), contenedor_respuesta_b)
            pygame.draw.rect(screen, (255, 255, 255), contenedor_respuesta_c)
            render_preguntas(contador_pregunta)
    elif pantalla == 'pantalla_final':
        screen.fill((139, 0, 0))
        pygame.draw.rect(screen, color_celeste, pygame.Rect(400, 300, 480, 70))
        text_surface = font_input.render(nombre_usuario, True, (0, 0, 0))
        screen.blit(text_surface, (410, 310))
        screen.blit(texto_guardar_puntaje, (410, 100))

    elif pantalla == 'sala_puntajes':
        screen.fill((139, 0, 0))
        pygame.draw.rect(screen, (0, 0, 0), rect_boton_salir_puntaje)
        screen.blit(texto_salir_puntaje, (1168, 120))
        screen.blit(texto_sala_puntajes, (420,50))
        render_puntajes(lista_puntajes)

    # alternar estado de boton de soundtrack dependiendo del estado de la bandera
    if sonido_on:
        pygame.draw.rect(screen, (color_verde), rect_boton_sonido)
        screen.blit(texto_mute, (1168, 36))
    else:
        pygame.draw.rect(screen, (color_rojo), rect_boton_sonido)
        screen.blit(texto_unmute, (1168, 36))

    pygame.display.flip()

pygame.quit()
