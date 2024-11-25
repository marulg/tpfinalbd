# Clase para representar una receta individual
class Receta:
    def __init__(self, nombre, ingredientes, es_vegano, tiempoc):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.es_vegano = es_vegano
        self.tiempoc = tiempoc

# Clase para gestionar una colección de recetas
class Recetas:
    def __init__(self):
        self.lista_recetas = [
            Receta("Vitel Toné",["Peceto","Vino Blanco","Puerro","Zanahoria","Apio","Cebolla","Ajo","Perejil","Sal","Laurel","Pimienta",],False,180),
            Receta("Ensalada César", ["lechuga", "pollo", "pan", "queso parmesano", "aderezo César"], False, 50),
            Receta("Guacamole", ["aguacate", "tomate", "cebolla", "limón", "cilantro", "sal"], True, 80),
            Receta("Spaghetti a la boloñesa", ["spaghetti", "carne", "tomate", "aceite", "sal", "pimienta"], False, 45)
        ]
    def buscar_recetas_por_ingredientes(self, ingredientes_buscados):
        # convertimos la lista de ingredientes buscados a un conjunto para facilitar la comparación
        ingredientes_buscados_set = set(ingredientes_buscados)

        # Inicializamos una lista vacía para las recetas que coinciden
        recetas_con_ingrediente = []

        # recorremos cada receta en la lista de recetas
        for receta in self.lista_recetas:
            # verificamos si todos los ingredientes de la receta están dentro de los ingredientes que el usuario ha ingresado
            if set(receta.ingredientes).issubset(ingredientes_buscados_set):
                recetas_con_ingrediente.append(receta)

        # Si hay recetas que coinciden, las mostramos
        if recetas_con_ingrediente:
            print(f"\nRecetas disponibles para los ingredientes ingresados:")
            for receta in recetas_con_ingrediente:
                tipo = "Vegano" if receta.es_vegano else "No vegano"
                print(f" - {receta.nombre} ({tipo})  ({receta.tiempoc} minutos)")  
        else:
            print(f"\nNo se encontraron recetas con todos los ingredientes requeridos dentro de los ingredientes.")

# Crear instancia de la clase Recetas
coleccion_recetas = Recetas()

# Solicitar ingredientes uno por uno
ingredientes_buscados = []

while True:
    ingrediente = input("Escribe un ingrediente para buscar recetas (o escribe 'No' para terminar): ").strip().lower()
    
    if ingrediente == "no":
        break
    if ingrediente:
        ingredientes_buscados.append(ingrediente)
    else:
        print("Por favor, ingresa un ingrediente válido.")

# Buscar recetas por los ingredientes ingresados
coleccion_recetas.buscar_recetas_por_ingredientes(ingredientes_buscados)
