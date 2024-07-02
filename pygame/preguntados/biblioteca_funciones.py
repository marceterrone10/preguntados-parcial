from datos import lista
import json
import pygame


def extraer_json(nombre_archivo:str, pasada:bool, puntajes:list):
    """
    Dependiendo la pasada y su valor en booleano, crea el archivo y vuelca los datos del puntaje y nombre, si ya paso una vez se torna en False y la proxima vez solo actualiza los datos sin necesidad de crear otra vez el archivo.

    Args:
    nombre del archivo/ruta en str
    pasada: inicialmente en True
    puntajes: lista de puntajes y nombres
    """
    if pasada == True:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(puntajes, archivo, indent=4)
            pasada = False
    elif pasada == False:
        with open(nombre_archivo, 'r') as archivo:
            puntajes = json.load(archivo)

def importar_json(nombre_archivo:str):
    """
    Importa los datos de puntajes.json para utilizarlos luego en la pantalla puntajes
    args:
    nombre del archivo/ruta del archivo en str

    return:
    retorna la lista con los datos de los puntajes y nombres para manipularla en el archivo
    """
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def ordenar_lista_por_parametro(lista: list, criterio:str, parametro:str):
    """
    Ordena la lista recibida por parametro con el criterio "ASC" o "DESC" tambien recibido por parametro.

    args:
    lista: lista de juegos
    criterio: str con criterio ASC o DESC
    parametros: que se desea ordenar

    return:
    retorna la lista ordenada
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (criterio == "ASC" and lista[i][parametro] > lista[j][parametro]) or (criterio == "DESC" and lista[i][parametro] < lista[j][parametro]):
                    # Swap
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                    
    return lista

def mutear_desmutear_soundtrack(sonido_on:bool):
    """
    Activa o desactiva el sountrack del juego
    Args:
    booleano que funciona como bandera para activar o desactivar la musica

    Return:
    Retorna el nuevo estado de la musica, si es False se baja el volumen a 0 simulando apagarla y si es True continua
    
    """
    sonido_on = not sonido_on
    if sonido_on:
        pygame.mixer.music.set_volume(0.05)
    else:
        pygame.mixer.music.set_volume(0)
    return sonido_on




