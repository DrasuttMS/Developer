#Tamaños
WIDTH, HEIGHT = 1280, 720
PLAYER = 100
GRASS = 64
TREE = 64
SMALL_STONE = 28

#Animaciones
BASIC_FRAMES = 6
IDLE_DOWN = 0
IDLE_RIGHT = 1
IDLE_UP = 2
WALK_DOWN = 3
WALK_RIGHT = 4
WALK_UP = 5
FRAME_SIZE = 32
ANIMATION_DELAY = 100

#Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (105, 55, 55)

#Barras de estado
MAX_ENERGY = 100
MAX_FOOD = 100
MAX_THIRST = 100

#Colores para las barras de estado
ENERGY_COLOR = (255, 255, 0)    #Amarillo
FOOD_COLOR = (255, 165, 0)      #Naranja
THIRST_COLOR = (0, 191, 255)    #Azul claro
BAR_BACKGROUND = (100, 100, 100)#Gris oscuro

#Intervalo de tiempo
STATUS_UPDATE_INTERVAL = 1000

#Sistema dia/noche
DAY_LENGTH = 2400000 #Duracion de dia completo en milisegundos (24 segundos)
DAWN_TIME = 600000 #Amanecer a las 06:00
MORNING_TIME = 800000 #Mañana completa a las 08:00
DUSK_TIME = 1800000 #Aterdecer a las 18:00
MIDNIGTH = 2400000 #Medianoche 00:00
MAX_DARKNESS = 210 #Nivel maximo de oscudirdad (0-255)

#Colores para iluminacion
NIGHT_COLOR = (20, 20, 50) #Color azul oscuro para la noche
DAY_COLOR = (255, 255, 255) #Color Blanco para el dia
DAWN_DUSK_COLOR = (255, 193, 137) #Color anaranjado para amanecer/atardecer

#Velocidad de disminucion de estados
FOOD_DECREASE_RATE = 0.01 #Velocidad de disminucion de comida
THIRST_DECREASE_RATE = 0.02 #Velocidad de disminucion de sed
ENERGY_DECREASE_RATE = 0.005 #Velocidad de disminucion de energia en estado critico
ENERGY_INCREASE_RATE = 0.001 #Velocidad de recuperacion de energia de estado normal
MOVEMENT_ENERGY_COST = 0.001 #Eneria consumida por mivimiiento