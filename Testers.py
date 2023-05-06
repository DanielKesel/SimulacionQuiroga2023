import random
import datetime
import time

TPLL = [] #Tiempo Proxima Llegada
TPS = [] #Tiempo Proxima Salida
TOCIO = [] #Tiempo Ocioso
TTESTING = [] #Tiempo de duracion del Testing que varia segun prioridad.
INICIO_TIEMPO_DIA = datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0) # Crear objeto datetime para representar la hora de inicio
FIN_TIEMPO_DIA = INICIO_TIEMPO_DIA + datetime.timedelta(hours=9) # Sumar 9 horas para calcular la hora de finalización
SUMATORIA_TIEMPOS_DIAS = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
TIEMPO_FINAL = datetime.timedelta(days=int(input("Ingrese el número de días: ")))
fecha_final = INICIO_TIEMPO_DIA + TIEMPO_FINAL # Calcular la fecha final sumando la duración deseada a la fecha de inicio

cantidad_tareas_baja_prioridad = 0
cantidad_tareas_media_prioridad = 0
cantidad_tareas_alta_prioridad = 0
vector_tareas = []

def llegadaTarea() :

    global cantidad_tareas_baja_prioridad, cantidad_tareas_media_prioridad, cantidad_tareas_alta_prioridad

    R = random.random()

    if R <= 0.1 :
        cantidad_tareas_baja_prioridad += 1
        vector_tareas.append("B")
    elif 0.1 < R <= 0.55:
        cantidad_tareas_media_prioridad += 1
        vector_tareas.append("M")
        
    else :
        cantidad_tareas_alta_prioridad += 1
        vector_tareas.append("A")


cantidad_de_testers = int(input("Ingresá la cantidad de testers que quieres contratar:\n -> "))
print("La cantidad de testers que has decidido contratar es %s" %cantidad_de_testers)

contador_tareas = 0

while SUMATORIA_TIEMPOS_DIAS < fecha_final :
    
    R = random.random()
    if R >= 0.5 :  
        
        llegadaTarea()
        contador_tareas += 1
    SUMATORIA_TIEMPOS_DIAS += datetime.timedelta(hours=8)

print("En un lapso de %s días llegaron %s tareas" % (TIEMPO_FINAL.days, contador_tareas))




print("La cantidad de tareas de Alta prioridad es: %s" %cantidad_tareas_alta_prioridad)
print("La cantidad de tareas de Media prioridad es: %s" %cantidad_tareas_media_prioridad)
print("La cantidad de tareas de Baja prioridad es: %s" %cantidad_tareas_baja_prioridad)
print("El vector de las prioridades en cada puesto ha quedado: %s" %vector_tareas)
