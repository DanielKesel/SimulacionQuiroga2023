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
IA = 0
TIEMPO_FINAL = 0
HV = math.inf
SUMATORIA_TIEMPO_OSCIOSO = 0
INICIO_TIEMPO_OSCIOSO = 0

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

    global BP, MP, AP
    
    R = random.random()

    if R <= 0.1 :
        BP += 1
        
    elif 0.1 < R <= 0.55:
        MP += 1
       
    else :
        AP += 1

def atenderTarea(tps) :
    global SUMATORIA_TIEMPO_OSCIOSO, cantidad_de_testers_atendiendo
    
    tps[buscarHV] = TIEMPO + 5
    if vector_puestos_de_atencion[buscarHV] == 0 :
        INICIO_TIEMPO_OSCIOSO = TIEMPO
        SUMATORIA_TIEMPO_OSCIOSO += TIEMPO + INICIO_TIEMPO_OSCIOSO
    cantidad_de_testers_atendiendo += 1
    
        
def buscarMenorTPS() :
    posicion_minimo_TPS = TPS.index(min(TPS))
    return posicion_minimo_TPS
    
def buscarHV() :
    posicion_TPS_HV = TPS.index(HV)
    return posicion_TPS_HV


#---------------------------- Programa Principal -------------------------------------------

TIEMPO_FINAL = int(input("Ingrese el número de días: "))
cantidad_de_tareas_asignables = int(input("Ingrese la cantidad maxima de tareas que se pueden asignar: "))
cantidad_de_testers = int(input("Ingresá la cantidad de testers que quieres contratar:\n -> "))
print("La cantidad de testers que has decidido contratar es %s" %cantidad_de_testers)
TPS = [HV] * cantidad_de_testers
vector_puestos_de_atencion = [0] * cantidad_de_testers

print("tamaño de lista ", TPS)
contador_tareas = 0
contador_dias_sin_tareas = 0
espera_tarea = bool
while TIEMPO < TIEMPO_FINAL :
    
    if TPLL <= TPS[buscarMenorTPS()]:
        TIEMPO = TPLL
        print("1 ",TIEMPO)
        SUMATORIA_TLL += TPLL
        
        while espera_tarea :
            R = random.random()
            if R >= 0.5 :  
    
                llegadaTarea()
                contador_tareas += 1
                espera_tarea = False
    
            else :
                IA += 1

        espera_tarea = True
        TPLL = TIEMPO + IA
        
        if(AP + BP + MP) == cantidad_de_tareas_asignables:
            arrepentidos += 1
        else :
            (AP + BP + MP)
            atenderTarea(TPS) 
    print("2 ", TIEMPO)
        

print("En un lapso de %s días llegaron %s tareas" % (TIEMPO_FINAL, contador_tareas))



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
