import random
import datetime
import time
import math

HV = math.inf

TPLL = 0
TPS = [] #Tiempo Proxima Salida
TOCIO = [] #Tiempo Ocioso
TTESTING = [] #Tiempo de duracion del Testing que varia segun prioridad.
TIEMPO = 0
SUMATORIA_TLL = 0
SUMATORIA_TPS = []
IA = 0
TIEMPO_FINAL = 0
HV = math.inf
SUMATORIA_TIEMPO_OSCIOSO = []
INICIO_TIEMPO_OSCIOSO = []

#fecha_final = INICIO_TIEMPO_DIA + TIEMPO_FINAL # Calcular la fecha final sumando la duración deseada a la fecha de inicio

BP = 0 # cantidad_tareas_baja_prioridad = 0
MP = 0 # cantidad_tareas_media_prioridad = 0
AP = 0 # cantidad_tareas_alta_prioridad = 0

vector_prioridades_por_puestos_por_puesto = []
vector_puestos_de_atencion = []
arrepentidos = 0 
contador_tareas_atendidas = 0
cantidad_de_testers = 0
cantidad_de_testers_atendiendo = 0

def llegadaTarea() :

    global BP, MP, AP, arrepentidos, contador_tareas_atendidas
    tareaAceptada = True
    
    if(AP + BP + MP) == cantidad_de_tareas_asignables:
        arrepentidos += 1
        tareaAceptada = False
         
    return tareaAceptada
    

def FDPprioridad(BP, MP, AP) :
    
    R = random.random()
    prioridad = ""

    if R <= 0.1 :
        BP += 1
        prioridad = "BP"
    elif 0.1 < R <= 0.55:
        MP += 1
        prioridad = "MP"
    else :
        AP += 1
        prioridad = "AP"
    
    return prioridad

def FDPresolucionTareas(prioridad) :
    duracion = 0
    if prioridad == "BP" :
        duracion = 1
    elif prioridad == "MP" :
        duracion = 3
    elif prioridad == "AP" :
        duracion = 7
    return duracion

def atenderTarea(tps) :
    global SUMATORIA_TIEMPO_OSCIOSO, cantidad_de_testers_atendiendo
    
    tps[buscarHV] = TIEMPO + 5
    if vector_puestos_de_atencion[buscarHV] == 0 :
        INICIO_TIEMPO_OSCIOSO = TIEMPO
        SUMATORIA_TIEMPO_OSCIOSO += TIEMPO + INICIO_TIEMPO_OSCIOSO
    cantidad_de_testers_atendiendo += 1
    
        
def buscarMenorTPS() :
    minimo_TPS = min(TPS)
    posicion_minimo_TPS = TPS.index(minimo_TPS)
    return posicion_minimo_TPS
    
def buscarHV() :
    print(TPS)
    posicion_TPS_HV = TPS.index(HV)
    return posicion_TPS_HV


#---------------------------- Programa Principal -------------------------------------------

TIEMPO_FINAL = int(input("Ingrese el número de días: "))
cantidad_de_tareas_asignables = int(input("Ingrese la cantidad maxima de tareas que se pueden asignar: "))
cantidad_de_testers = int(input("Ingresá la cantidad de testers que quieres contratar:\n -> "))
print("La cantidad de testers que has decidido contratar es %s" %cantidad_de_testers)

TPS = [HV] * cantidad_de_testers
SUMATORIA_TIEMPO_OSCIOSO = [0] * cantidad_de_testers
INICIO_TIEMPO_OSCIOSO = [0] * cantidad_de_testers
SUMATORIA_TPS = [0] * cantidad_de_testers
vector_puestos_de_atencion = [0] * cantidad_de_testers
vector_prioridades_por_puestos_por_puesto = [0] * cantidad_de_testers
cantidad_de_testers_disponibles = cantidad_de_testers
contador_tareas = 0
contador_dias_sin_tareas = 0
espera_tarea = bool

while TIEMPO < TIEMPO_FINAL :
    print("-> Entramos a la condicion 'TIEMPO < TIEMPO_FINAL'")
    posicionMenorTPS = buscarMenorTPS()
    if TPLL <= TPS[posicionMenorTPS]:
        print("-> Entramos a la condicion 'TPLL <= TPS[buscarMenorTPS()]'")
        TIEMPO = TPLL
        SUMATORIA_TLL += TPLL
        while espera_tarea :
            R = random.random()
            if R >= 0.5 :  
                print("-> Entramos a la condicion 'llegaTarea()'")
                contador_tareas += 1
                tareaAceptada = llegadaTarea()
                espera_tarea = False
    
            else :
                print("-> Entramos a la condicion 'No llega tarea e incrementa intervalo de arribo'")
                IA += 1

        espera_tarea = True
        if tareaAceptada == True :
            print("-> Entramos a la condicion 'tareaAceptada == True'")
            TPLL += TIEMPO + IA
            contador_tareas_atendidas += 1
            prioridad_llegada = FDPprioridad(BP, MP, AP)
            if(BP + MP + AP) <= cantidad_de_testers_disponibles :
                print("-> Entramos a la condicion 'if(BP + MP + AP) <= cantidad_de_testers_disponibles'")
                if HV in TPS :     
                    print("-> 'HV in TPS'")
                    posicion_disponible = buscarHV()
                    TPS[posicion_disponible] = TIEMPO + FDPresolucionTareas(prioridad_llegada)
                    vector_prioridades_por_puestos_por_puesto[posicion_disponible] = prioridad_llegada
                    SUMATORIA_TIEMPO_OSCIOSO[posicion_disponible] += TIEMPO - INICIO_TIEMPO_OSCIOSO[posicion_disponible]
            
        print("TPLL es %s y TPS es %s" %(TPLL, TPS))
        print(vector_prioridades_por_puestos_por_puesto)
        print("Se vuelve a cumplir el ciclo hasta que deje de pasar TIEMPO < TIEMPO_FINAL")
        IA = 0
    else : 
        TIEMPO = TPS[posicionMenorTPS]
        SUMATORIA_TPS += TPS[posicionMenorTPS]
        prioridad_tarea = ""
        if vector_prioridades_por_puestos_por_puesto[posicionMenorTPS] == "BP" :
            BP -= 1
            prioridad_tarea = "BP"
        elif vector_prioridades_por_puestos_por_puesto[posicionMenorTPS] == "MP" :
            MP -= 1
            prioridad_tarea = "MP"
        elif vector_prioridades_por_puestos_por_puesto[posicionMenorTPS] == "AP" :
            AP -= 1
            prioridad_tarea = "AP"
        if(BP + MP + AP) >= cantidad_de_testers_disponibles :
            TPS[posicionMenorTPS] = TIEMPO + FDPresolucionTareas(prioridad_tarea)
        else :
            TPS[posicionMenorTPS] = HV
            INICIO_TIEMPO_OSCIOSO[posicionMenorTPS] = TIEMPO
    IA = 0

print("En un lapso de %s días llegaron %s tareas, se rechazaron %s y se atendieron %s" % (TIEMPO_FINAL, contador_tareas, arrepentidos ,contador_tareas_atendidas))

print("La cantidad de tareas de Alta prioridad es: %s" %AP)
print("La cantidad de tareas de Media prioridad es: %s" %MP)
print("La cantidad de tareas de Baja prioridad es: %s" %BP)
print("El vector de las prioridades en cada puesto ha quedado: %s" %vector_prioridades_por_puestos_por_puesto)


print(TIEMPO)
#   if R <= 0.1 :
#         cantidad_tareas_baja_prioridad += 1
#         vector_prioridades_por_puestos.append("B")
#     elif 0.1 < R <= 0.55:
#         cantidad_tareas_media_prioridad += 1
#         vector_prioridades_por_puestos.append("M")
        
#     else :
#         cantidad_tareas_alta_prioridad += 1
#         vector_prioridades_por_puestos.append("A")
