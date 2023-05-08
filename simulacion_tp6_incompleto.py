import random

# VARIABLES DE CONTROL
CANTIDAD_DE_TAREAS_ASIGNABLES = 2 #int(input("Ingrese la cantidad maxima de tareas que se pueden asignar: "))
CANTIDAD_DE_TESTERS = 1 #int(input("Ingresá la cantidad de testers que quieres contratar:\n -> "))

# VARIABLES DE ESTADO
BP = 0
MP = 0 
AP = 0

# CONDICIONES INICIALES
TIEMPO = 0
TIEMPO_FINAL = 300
HV = 2147483646
TPLL = 0
TPS = [HV] * CANTIDAD_DE_TESTERS
TOCIO = [] #Tiempo Ocioso
SUMATORIA_TPLL = 0
SUMATORIA_TPS = [0] * CANTIDAD_DE_TESTERS
SUMATORIA_TIEMPO_OSCIOSO = [0] * CANTIDAD_DE_TESTERS
INICIO_TIEMPO_OSCIOSO = [0] * CANTIDAD_DE_TESTERS
VECTOR_PRIORIDADES = [0] * CANTIDAD_DE_TESTERS
ARREPENTIDOS = 0 
CONTADOR_DE_TAREAS = 0
    
def generarIA() :
    return random.randint(1,7)

def generarTAAP() :
    return random.randint(4,5)

def generatTAMP() :
    return random.randint(3,5)

def generarTABP() :
    return random.randint(1,2)
           
def buscarMenorTPS() :
    minimo_TPS = min(TPS)
    posicion_minimo_TPS = TPS.index(minimo_TPS)
    return posicion_minimo_TPS
    
def buscarHV() :
    posicion_TPS_HV = TPS.index(HV)
    return posicion_TPS_HV

def llegada() :
    global AP,MP,BP, ARREPENTIDOS, TIEMPO, TPLL, CONTADOR_DE_TAREAS, SUMATORIA_TPLL, SUMATORIA_TIEMPO_OSCIOSO, INICIO_TIEMPO_OSCIOSO
    TIEMPO = TPLL
    SUMATORIA_TPLL += TPLL
    TPLL = TIEMPO + generarIA()

    if BP+MP+AP == CANTIDAD_DE_TAREAS_ASIGNABLES :
        ARREPENTIDOS += 1
    else:
        CONTADOR_DE_TAREAS += 1
        R = random.random()
        if R < 0.27 :
            AP += 1
            if BP+MP+AP <= CANTIDAD_DE_TESTERS :
                puestoLibre = buscarHV()
                SUMATORIA_TIEMPO_OSCIOSO[puestoLibre] += (TIEMPO - INICIO_TIEMPO_OSCIOSO[puestoLibre])
                TPS[puestoLibre] = TIEMPO + generarTAAP()
                VECTOR_PRIORIDADES[puestoLibre] = "AP"
        elif R < 0.58 :
            MP += 1
            if BP+MP+AP <= CANTIDAD_DE_TESTERS :
                puestoLibre = buscarHV()
                SUMATORIA_TIEMPO_OSCIOSO[puestoLibre] += (TIEMPO - INICIO_TIEMPO_OSCIOSO[puestoLibre])
                TPS[puestoLibre] = TIEMPO + generatTAMP()
                VECTOR_PRIORIDADES[puestoLibre] = "MP"
        else :
            BP += 1
            if BP+MP+AP <= CANTIDAD_DE_TESTERS :
                puestoLibre = buscarHV()
                SUMATORIA_TIEMPO_OSCIOSO[puestoLibre] += (TIEMPO - INICIO_TIEMPO_OSCIOSO[puestoLibre])
                TPS[puestoLibre] = TIEMPO + generarTABP()
                VECTOR_PRIORIDADES[puestoLibre] = "BP"

def salida(menorTPS) :
    global AP,MP,BP
    TIEMPO = TPS[menorTPS]
    SUMATORIA_TPS[menorTPS] += TPS[menorTPS]

    if VECTOR_PRIORIDADES[menorTPS] == "AP" :
        AP -=1
    elif VECTOR_PRIORIDADES[menorTPS] == "MP" :
        MP -=1
    elif VECTOR_PRIORIDADES[menorTPS] == "BP" :
        BP -=1
            
    if AP+MP+BP>= CANTIDAD_DE_TESTERS :
        if AP > 0 and AP > VECTOR_PRIORIDADES.count("AP"):
            VECTOR_PRIORIDADES[menorTPS] = "AP"
            TPS[menorTPS] = TIEMPO + generarTAAP()
        elif MP > 0 and MP > VECTOR_PRIORIDADES.count("MP"):
            VECTOR_PRIORIDADES[menorTPS] = "MP"
            TPS[menorTPS] = TIEMPO + generatTAMP()
        elif BP > 0 and BP > VECTOR_PRIORIDADES.count("BP"):
            VECTOR_PRIORIDADES[menorTPS] = "BP" 
            TPS[menorTPS] = TIEMPO + generarTABP()
    else :
        TPS[menorTPS] = HV
        VECTOR_PRIORIDADES[menorTPS] = "0"
        INICIO_TIEMPO_OSCIOSO[menorTPS] = TIEMPO
        
#---------------------------- Programa Principal -------------------------------------------

while TIEMPO < TIEMPO_FINAL :
    menorTPS = buscarMenorTPS()
    if TPLL <= TPS[menorTPS]:
        llegada()
    else :
        salida(menorTPS)

TPLL = HV
while AP+MP+BP>0 :
    menorTPS = buscarMenorTPS()
    if TPLL <= TPS[menorTPS]:
        llegada()
    else :
        salida(menorTPS)

# CALCULO DE RESULTADOS

PTO = [0] * CANTIDAD_DE_TESTERS
for i in range(CANTIDAD_DE_TESTERS):
    PTO[i] = SUMATORIA_TIEMPO_OSCIOSO[i]*100/TIEMPO

PPS = ((sum(SUMATORIA_TPS) - SUMATORIA_TPLL)/CONTADOR_DE_TAREAS)

PTA = ARREPENTIDOS *100 / CONTADOR_DE_TAREAS

print("En un lapso de %s días llegaron %s tareas, se rechazaron %s" % (TIEMPO_FINAL, CONTADOR_DE_TAREAS, ARREPENTIDOS))
print("La cantidad de tareas de Alta prioridad es: %s" %AP)
print("La cantidad de tareas de Media prioridad es: %s" %MP)
print("La cantidad de tareas de Baja prioridad es: %s" %BP)

print("dias osciosos: %s" %SUMATORIA_TIEMPO_OSCIOSO[0])

for i in range(CANTIDAD_DE_TESTERS):
    print("PTO del integrante %s por mes es del %s" % (i, PTO[i]))

print("Promedio de permanencia en el sistema: %s" %PPS)

print("Porcentaje de tareas asignadas a otros equipos: %s" %PTA)
#semanas laborales y meses con distintos numeros de dias