##Problema de pokemon competitivo vamos a crear un Gestor de equipo 
import json

pokemon1 = {"Nombre":"Milotic", "Habilidad": "Gran encanto", "Nivel": 50}
pokemon2 = {"Nombre": "Incineroar", "Habilidad": "Intimidacion", "Nivel": 50}
pokemon3 = {"Nombre":"Gengar", "Habilidad": "Cuerpo  maldito", "Nivel": 50}
pokemon4 = {"Nombre":"Aerodactyl", "Habilidad": "Nerviosismo", "Nivel": 50}
pokemon5 = {"Nombre":"Sinitcha", "Habilidad": "Hospitalidad", "Nivel": 50}
pokemon6 = {"Nombre":"Clefable", "Habilidad": "Guardia magica", "Nivel": 50}
pokemones = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]

## hacemos un archivo json para leer los pokemons guardados 
#OCUPAMOS TRY POR SI AL MOMMENTO DE INTENTAR LEER (CARGAR) ARCHIVO O POKEMON Y NO HAYA NIONGUNO HAGA UNA LISTA VACIA 
#ocupamos una funcion para despues ejecutar todo esto solo llamando a cargar_datos y para que el codigo
def cargar_datos():
    try:
        #abrimos el archivo pokemon.json con with y open le decimos que lo queremos lear con r y lo apodamos archivo 
        with open ("pokemon.json", "r")as archivo:
            return json.load(archivo) #usamosjson.load para que lea el archivo que es como apodamos a pokemon.json
    except FileNotFoundError :
        return []
#ahora hacemos la funcion de el guardado de datos con w 
def guardar_datos(lista):
    with open ("pokemon.json", "w") as archivo:
        json.dump(lista, archivo , indent= 4)## usamos json dump para que lista que es guardar datos en archivo que es pokemon.json y el indent= 4  regla de oro par que se vea ,as limpio en la terminal 
guardar_datos(pokemones)## guardamos la lista pokemones en el archivo pokemon.json
#Hacmos la funcion menu con todas la opciones disponibles de mi conocimiento
#definmimos que guardar datos ahora es mipc para despues poder agregar pokemons a mipc (pokemon.json)
def menu ():
    mipc = cargar_datos()
    #hago un while true para crear un bucle infinito hasta detenerlo manualmente con un break 
    while True:
        print("\n ----EQUIPO POKEMON---")        
        print("1.-Ver mi pc")        
        print("2.-Agregar Pokemon al equipo")        
        print("3.-Buscar Pokemon")        
        print("4.-Salir")        
        #pedims al usuario que ingrese una opcion del menu 
        opcion = input("Elige una opcion: ")

        #hacemos un if para cada opcion empezando con la de salir para cortar el bucle
        if opcion == "1":
            print("\n ---- MiPC----")
            #uso for para recorrer la lista de pokemon.json
            for inv in mipc:
                print(f"\n-{inv['Nombre']}: {inv['Nivel']}")
        elif opcion == "2":
            nom = input("Ingrese el nombre de el pokemon que quiere ingresar: ")
            hab = input("Ingrese la habilidad de el pokemon que quiere ingresar: ")
            niv = input("Ingresa el nivel de el pokemon que quieres ingresar: ")

            nuevo_pokemon = {"Nombre": nom , "Habilidad": hab, "Nivel": niv}
            mipc.append(nuevo_pokemon)
            guardar_datos(mipc)
            print("\n ----Pokemon Guardado con exito---- ")
        elif opcion == "3":
            ##para el buscador defino busqueda para pedirselo al cliente con u input y un lower para evitar problemas por mayusculas
            busqueda = input("Ingrese un Pokemon: ").lower()
            encontrado = False #definimos a encontrado como false por que aun no ha enocntrado nada
            
            ## buscamos el pokemonm con un for 
            for pok in mipc:#decimos que pok es el indice osea que de momento en este sting mipc pasa a ser pok al menos en lo que se ejecuta el for
                if busqueda in pok ['Nombre'].lower(): #despues le preguntamos si la variable busqueda (pokemon ingresado) esta en pok (mipc)
                    #buscamos con el input ingresado en archivo co metodo diccionario buscando por nombre (milotic, gengar, etc)
                    print(f"\ Encontrado")
                    print(f"Pokemon: {pok['Nombre']}")
                    encontrado = True # le decimos al pc que si este if es verdad encontrado es igual a true lo que hace que no tenga que buscar mas
                    break #paramos el while infinito   
                if not encontrado: 
                    print("No se ha encontrado el Pokemon")

menu()










            
            
