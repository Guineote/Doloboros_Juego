import time
import os
import pygame
import sys
import keyboard
from tkinter import *
from PIL import Image, ImageTk
class Doloboros:
    def __init__(self):
        pygame.init()
        self.flag = True    #Banndera para controlar algunos ciclos dentro del codigo
        self.duracion = 2.5
        self.intervalo = 0.5
        self.repeticioes = int(self.duracion/self.intervalo)
        self.speed = 0.01
        self.items_erebos = []

    def clear_screen(self): #Esta funcion ayuda a limpiar lo que este en consola
        os.system('cls' if os.name == 'nt' else 'clear')

   
    def text_blinking(self, text):  #Esta funcion toma como parametro un texto y simulara una animacion de parpadeo
        self.text = text
        for _ in range (self.repeticioes):
            print("\033[1;37;40m" + self.text + "\033[0m", end="", flush=True)
            time.sleep(self.intervalo)
            self.clear_screen()
            time.sleep(self.intervalo)
        
    def print_paused(self, text):   #Imprime el texto de manera pausada, como si fuera una maquina de escribir
        self.text = text
        for caracter in self.text:
            sys.stdout.write(caracter)
            sys.stdout.flush()
            time.sleep(self.speed)
    
    def Erebos_History(self):   #Ventana que ayuda a conocer un poco de contexto sobre el personaje
       self.clear_screen()
       self.Erebos_window = Tk()
       self.Erebos_window.title("E R E B O S")
       self.Erebos_window.resizable(True, True)
       #self.Erebos_window.geometry("400x400")
       self.Erebos_window.iconbitmap("Doloboros_f1.ico")
       self.Erebos_window.config(bg = "black")
       self.label = Label(self.Erebos_window, text = "Erebos, un hombre nacido en condiciones desfavorables que debido a las circunstancias es forzado a")
       self.label.pack()
       self.label1 = Label (self.Erebos_window, text = "dedicarse a una profesion que atenta contra la vida humana, pero su vida puede dar")
       self.label1.pack()
       self.lbl2 = Label (self.Erebos_window, text = ("Un giro totalmente repentino. Algunas decisiones pueden tener repercusiones importantes"))
       self.Erebos_window.mainloop()
             
        
    def inventory_erebos(self, ruta):   #Pantalla que permite ver en una ventana el inventario de tu personaje y la barra de salud mental
        self.inventory_ero = Tk()
        self.inventory_ero.title ("Inventario")
        self.inventory_ero.resizable(False, False) #Hace que no se puede redimensionar la ventana
        self.inventory_ero.geometry("600x600")  #Establece el anchoo y alto de la ventana
        self.inventory_ero.iconbitmap("Doloboros_f1.ico")   #carga un icono para la ventana
        self.label = Label(self.inventory_ero, text = "Inventario")
        self.label.pack()
        self.list_inventory = Listbox(self.inventory_ero)
        for item in self.items_erebos:
            self.list_inventory.insert(END, item)
        self.list_inventory.pack()
        imagen = Image.open(ruta)  #Tomara una ruta para de imagen oara ponerla dentro de la ventana, generalmente las imagenes de la barra de salud mental
        imagen = ImageTk.PhotoImage(imagen)
        self.label_imagen = Label(self.inventory_ero, image = imagen)
        self.label_imagen.imagen = imagen
        self.label_imagen.pack() #Controla la posicion de la imagen dentro de la ventana
        self.inventory_ero.mainloop()

    def set_new_item(self, item):   #Ayuda a controlar los items que se agregan al inventario
        self.items_erebos.append(item)  #Append new item
        print(f"Item '{item}' agregado al inventario")

    def delete_item(self, item):  #Ayuda a borrar items del inventario
        if item in self.items_erebos:
            self.items_erebos.remove(item)
            print(f"Item '{item}' eliminado del inventario")
        else:
            print(f"El item '{item}' no esta en el inventario")
            
                
    def start_screen(self): #Pantalla de inicio co el nombre del juego y las instrucciones para iniciar
        self.clear_screen()
        print("\tLoading ", end = "")
        for _ in range(5):
            time.sleep(0.05)
            print("▪", end = "", flush = True)
        screen = """ 
        +=======================================================================================================+
        |████████▄|||▄██████▄|||▄█||||||||▄██████▄||▀█████████▄|||▄██████▄|||||▄████████||▄██████▄|||||▄████████|
        |███|||▀███|███||||███|███|||||||███||||███|||███||||███|███||||███|||███||||███|███||||███|||███||||███|
        |███||||███|███||||███|███|||||||███||||███|||███||||███|███||||███|||███||||███|███||||███|||███||||█▀||
        |███||||███|███||||███|███|||||||███||||███||▄███▄▄▄██▀||███||||███||▄███▄▄▄▄██▀|███||||███|||███||||||||
        |███||||███|███||||███|███|||||||███||||███|▀▀███▀▀▀██▄||███||||███|▀▀███▀▀▀▀▀|||███||||███|▀███████████|
        |███||||███|███||||███|███|||||||███||||███|||███||||██▄|███||||███|▀███████████|███||||███||||||||||███|
        |███|||▄███|███||||███|███▌||||▄|███||||███|||███||||███|███||||███|||███||||███|███||||███||||▄█||||███|
        |████████▀|||▀██████▀||█████▄▄██||▀██████▀||▄█████████▀|||▀██████▀||||███||||███||▀██████▀|||▄████████▀||
        |||||||||||||||||||||||▀||||||||||||||||||||||||||||||||||||||||||||||███||||███|||||||||||||||||||||||||
        +=======================================================================================================+
        """ #ASCII hecho para el nombre del juego
        print(screen)
        self.intro_sound = pygame.mixer.Sound ("Silent_Hill.mp3")   #Libreria que ayuda a crear un objeto de Pygame y tomar un archivo de audio 
        self.intro_sound.play() #Reproduce archivo de audio
        while self.flag:
            s = input("Bienvenido, ingresa 's' para iniciar: ").lower()
            if (s == 's'):
                name = input("Ingresa tu nombre: ")
                print("Hola, " + name + ", beinvenid@ a Doloboros")
                print("Para comenzar presiona cualquier tecla")
                self.key = keyboard.read_event(suppress = True).name
                time.sleep(2)
                self.flag = False
            else:
                print("Opcion invalida, igresa s para iniciar")
        
        self.flag = True    
        while self.flag:    
            print("Se abrira una ventana emergente con contexto sobre tu personaje")
            print("Presiona cualquier tecla")
            self.key = keyboard.read_event(suppress = True).name
            self.Erebos_History()
            print("¿Deseas comenzar?")
            self.aux = input("Ingresa 's' o 'n'\n").lower()
            if self.aux == 's':
                print("Comezando historia de Erebos Moreau...")
                print("\tLoading ", end = "")
                for _ in range(5):
                    time.sleep(0.5)
                    print("▪", end = "", flush = True)
                self.flag = False
                self.Erebos_Moreau()
                break
            else:
                print("Opcion invalida")
                self.clear_screen()

    def Erebos_Moreau(self):
        self.mental_health = 0
        self.murders = 0
        self.lives_forgive = 0
        self.ch = ""
        self.intro_sound.stop()
        self.clear_screen()
        self.flag_b = True
        self.gun = True
        self.bulllets = 6
        self.amu = 0
        intro = ("""
        Los Moreau, no se sabe realmente mucho de ellos, solo que la madre dejo a su unico hijo, Erebos, 
        abandonado en un pobre mercado, moribundo y a su suerte, Erebos crecio sin padres, solo comerciantes 
        embusteros que le enseñarian a subsistir\n""")
        self.print_paused(intro)
        self.clear_screen()
        print("Instrucciones:\nPresiona cualquier letra para continuar en los dialogos.\n")
        self.key = keyboard.read_event(suppress = True).name
        #audio de fondo
        self.text_blinking("1772")
        self.print_paused("Te encuentras en Francia viviendo entre comerciantes, no tienes un hogar, duermes en donde puedas y en donde se te permita.\n")
        self.print_paused("Comerciante: Erebos acompañame a ir por un cargamento\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos niño: Claro!\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos niño: Estas robando? A tu propio proveedor?\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Comerciante: Es lo que es y lo necesito mas que el, toma algo tu tambien\n")
        while self.flag_b:
            self.ch = input("'t' tomar, 'n' no\n").lower()
            if self.ch == 't':
                self.print_paused("Comerciante: Buena decision niño\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Comerciante: Sabes, aqui el que no ve por si mismo no sobrevive, debes ver por tu supervivencia y tomar lo que te pertenece por ley natural\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos niño: Seguro, lo tendre muy en cuenta señor, gracias!")
                self.key = keyboard.read_event(suppress = True).name
                self.flag_b = False
                break
            elif self.ch == 'n':
                self.print_paused("Comerciante: No duraras mucho aqui mocoso\n")
                self.key = keyboard.read_event(suppress = True).name
                self.clear_screen()
                self.print_paused("Erebos niño: Lo siento, es solo que no sabia que hacer\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Comerciante: Y ellos ni siquieran saben de ti, alla afuera podriamos morir y a nadie le importaria, por eso debemos ver por nostros mismos\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Vives donde vives, eres lo que eres y somos lo que somos, espero que esto te enseñe, porque yo no te alimentare si no me alimento primero yo\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos niño: Nonono, disculpe enserio, si regresamos ttratare de-\n")
                self.print_paused("Comerciante: No trataras nada!!, si quieres comida ganatela o tomala.")
                self.key = keyboard.read_event(suppress = True).name
                self.flag_b = False
                break
            else:
                print("Ingresa una opcion valida")
        
        self.clear_screen()
        self.text_blinking("1781")
        self.print_paused("A los 19 años empiezas a relacionarte con personas que se ganan la vida de forma poco etica. En esta etapa no tienes mas opcion que ser cobrador\n") 
        self.print_paused("Comerciante: Necesito que vayan a cobrar algunas libras francesas\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Descuide jefe, yo ire\n")
        self.key = keyboard.read_event(suppress = True).name
        self.clear_screen()
        print("Debes cobrar 1000 libras")
        self.print_paused("Erebos: No hay a donde correr, es mejor que saldes tu deuda\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Campesino: Por favor, es todo lo que tengo, tomelo\n")
        self.flag_b = True
        while self.flag_b == True:
            self.ch = input("¿Aceptar 500 libras?\n 's ' \t 'n'\n").lower()
            if self.ch == 's':
                self.print_paused("Erebos: Debe pagar la semana entrante lo que falta, vere como puedo ayudarlo por el momento\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Campesino: Gracias joven, prometo que pagare solo deme mas tiempo\n")
                self.key = keyboard.read_event(suppress=True).name
                self.clear_screen()
                self.print_paused("Erebos: Lo siento jefe, el campesino solo tenia 500 libras\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Comerciante: No te pago por tener por compasion, te pago por conseguirme mi dinero\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos: El campesio no tenia nada mas, me lo dio todo\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Comerciante: Por supuesto, eso dicen todos, un par de golpes y hubieras regresado con mis 1000 libras, pero ahora tu me debes a mi\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Necesito que vayas a hacer otro trabajo, esta ves mas te vale regresar con mi dinero")
                self.key = keyboard.read_event(suppress = True).name
                self.flag_b = False
            
            elif self.ch == 'n':
                self.print_paused("Erebos: Usted sabe que eso solo cubre la mitad\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Campesino: Es todo lo que tengo, por favor\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos: Miente\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Campesino: Se lo suplico, por favor\n")
                punch = True
                self.hits = 0
                while punch:
                    self.ch = input("'g' golpear\n").lower()
                    if self.ch == 'g':
                        self.ou = pygame.mixer.Sound("Punch.mp3")
                        self.ou.play()    
                        self.hits += 1
                        if self.hits == 2:
                            self.print_paused("Campesino: Detengase, aqui esta lo demas, era para pagar la medicina de mi hija\n")
                            self.key = keyboard.read_event(suppress = True).name
                            self.print_paused("Erebos: Lo lamento, pero si no era a usted será a mi\n")
                            self.flag_b = False
                            self.key = keyboard.read_event(suppress = True).name
                            break
                    else:
                        print("Debes golpearlo")
                
        self.clear_screen()
        self.print_paused("Comerciante: Aqui esta el joven del que le hable Baron Ro\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Tu quien eres muchacho?\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Soy Erebos señor, en que le puedo ayudar?\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Me han dicho que tienes habilidades que podrian servirme\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Espero serle de ayuda, mientras la paga sea buena, no tengo muchas libras\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Si trabajas para mi, las libras seran lo ultimo de tus preocupaciones.\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Ven conmigo\n")
        self.key = keyboard.read_event(suppress = True).name
        self.clear_screen()
        self.print_paused("Baron Ro: Toma esto\n")
        self.flag_b = True
        while self.flag_b:
            self.ch = input("Aceptar el arma\n's'\t'n'\n").lower()
            if self.ch == 's':
                self.print_paused("Baron Ro: No debería de ser complicado, espero que no tengas que descargarla\n")
                self.key = keyboard.read_event(suppress = True).name
                self.set_new_item("arma")
                self.text_blinking("Arma añadida al inventario")
                self.inventory_erebos("Mental_Health_Bar_S1.png")
                self.gun = True
                self.flag_b = False
                #self.inventory_erebos("Mental_Health_Bar_S1.png")
            elif self.ch == 'n':
                self.print_paused("Espero que no tengas que necesitarla pacifista\n")
                self.key = keyboard.read_event(suppress = True).name
                self.gun = False
                aux = 1
                self.flag_b = False
            else:
                print("Opcion invalida\n")
                
        self.print_paused("Baron Ro: Tu objetivo es un hombre de la nobleza que gusta de venir al mercado con ustedes de ves en cuando\n")
        self.print_paused("Dale un susto, a menos que consideres necesario algo mas\n")
        self.key = keyboard.read_event(suppress = True).name
        self.clear_screen()
        self.print_paused("Mercado central de Francia\n")
        #sonido aqui
        self.print_paused("Erebos: Hola, estoy buscando a un hombre llamado Charles\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Vendedor: Aqui hay muchas personas, deberas ser mas especifico\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Me dieron esta descripcion, es de estatura media, perteneciente a la nobleza, puede que venga con mas hombres\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Vendedor: He visto a alguien con mas hombres que parecian de la nobleza, se fueron por alla\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Gracias\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Ahi estas, podria generar una distraccion y apartarlo\n")
        self.key = keyboard.read_event(suppress = True).name
        self.flag_b = True
        while self.flag_b:
            self.ch = input("Hacer\n'd' distraccion\n").lower()
            if self.ch == 'd':
                self.distract = pygame.mixer.Sound("Distract.mp3")
                self.distract.play()
                self.print_paused("Dispersado entre la multitud logras separar a Charles\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos: Charles, usted le debe libras a Baron Ro\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Charles: Libras? Baron Ro deberia de agradecerme, solo yo se su pequeño secreto y he sido muy prudente al respecto\n")
                self.print_paused("Charles: No es dinero por lo que te han mandado chico, son documentos\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos: Usted sabe que no estaria aqui solo por documentos\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Charles: La cuestion es que el dinero ya no lo tengo\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos: Bueno, parece que tendremos que solucionarlo de otra forma\n")
                if self.gun == True:
                    self.print_paused("Charles: Si vas por ese camino, sera dificil dar vuelta atras \n")
                    self.sgun = pygame.mixer.Sound("Shot.mp3")
                    self.sgun.play()
                    self.key = keyboard.read_event(suppress = True).name
                    self.print_paused("Has encontrado en su chaleco unos documentos\n")
                    self.murders += 1
                    self.amu = self.bulllets - 1
                    self.key = keyboard.read_event(suppress = True).name
                    self.flag_b == True
                
                elif aux == 1:
                    self.print_paused("Erebos: Necesito que me pague y me de todo lo que le corresponda al Baron Ro\n")
                    self.key = keyboard.read_event(suppress = True).name
                    self.print_paused("Charles: Ya te he dicho que no tengo nada para el\n")
                    self.key = keyboard.read_event(suppress = True).name
                    self.print_paused("Erebos: Ya lo veremos\n")
                    punch = True
                    self.hits = 0
                    while punch:
                        self.ch = input("'g' golpear\n").lower()
                        if self.ch == 'g':
                            self.ou = pygame.mixer.Sound("Punch.mp3")
                            self.ou.play()    
                            self.hits += 1
                        if self.hits == 6:
                            self.print_paused("Erebos: Ha tenido suficiente?\n")
                            self.key = keyboard.read_event(suppress = True).name
                            self.print_paused("Charles: No sabes lo que haces, esta nacion esta en peligro por ese hombre\n")
                            self.key = keyboard.read_event(suppress = True).name
                            break
            while self.flag_b:
                self.print_paused("Leer carta\n")
                self.ch = input("'s' 'n'").lower()
                if self.ch == 's':
                    print("No tenemos mucho tiempo, el Baron Ro es alguien que actua desde la corte, no se aun quien pero lo podemos descubrir,\n")
                    print("No es alguien de fiar, ha traicionado incluso a sus empleados mas cercanos, temo por mi vida, por favor espero atiendan mi peticion\n")
                    print("de arrestarle a la brevedad.")
                    self.key = keyboard.read_event(suppress = True).name
                    self.flag_b = False
                    break
                elif self.ch == 'n':
                    self.flag_b = False
                    break
                            
            self.print_paused("Baron Ro: ¿Que ha pasado chico\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: He encontrado estos documentos en el chaleco del señor Charles, creo que planeaba algo en contra suya.\n")
            letter = """
                        ...
                      /`   `\
                     /       \
                    |\~~~~~~~/|
                    | \=====/ |
                    | /`...'\ |
                    |/_______\|
                            """
            self.print_paused(letter)
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Baron Ro: Estos documentos seran de gran utilidad chico, te ganaste un lugar\n")
            self.key = keyboard.read_event(suppress = True).name
            self.clear_screen()
            self.print_paused("A partir de ahora tendras una barra de salud mental, esta ira descendiendo o aumentando dependiendo de tus buenas o malas acciones\n")
            self.key = keyboard.read_event(suppress = True).name

                    
                
            self.print_paused("Tiempo despues, en 1783 conoces a una mujer que se convertiria en tu esposa.\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("No les va mal ya que llevas un par de años trabajado para el Baron Ro, por lo que no les faltan las libras.\n")
            self.key = keyboard.read_event(suppress = True).name
            self.text_blinking("1784")
            self.print_paused("Nace tu hija\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Esta niña es mi felicidad entera, va a crecer en unn mundo muy diferente al que yo creci\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Marie:Durante cuanto tiempo Erebos? \n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: A que te refieres querida, todo en orden?\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Marie: No lo se, he estado pensando...\n")
            self.print_paused("No se cuanto tiempo debas seguir con tu vocacion...\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Lo se Marie, pero eso es lo unico que pondra un buen techo sobre nosotros y nuestra hija\n")
            self.print_paused("Jamas en mi vida regresaria al mercado y mi hija ni mi esposa merecen eso\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Marie: Hay otras formas de ganarse la vida, Erebos. No podemos seguir así.\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Pero, Marie, ¿cómo alimentaremos a nuestra hija?\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Marie: Podemos encontrar otras formas, Erebos. No podemos vivir en la sombra de la violencia para siempre.\n")
            self.key = keyboard.read_event(suppress = True).name   
            self.print_paused("Erebos: Lo pensare, pero en un futuro cercano es lo unico que tenemos.\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Presiona cualquier tecla para Continuar...\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.clear_screen()
            self.text_blinking("1788")
            self.print_paused("Diciembre de 1788\n")
            self.print_paused("Baron Ro: Hey Erebos, disculpa incomodarte con tu bella familia, pero hay un trabajo que requiere tu atencion\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Claro Baron, descuide, en que le sirvo?\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.flag_b = True
            while self.flag_b:
                self.print_paused("Baron Ro: Necesito de tus habilidaades nuevamente, tu objetivo sera una mujer, tienes problema con eso?\n")
                self.ch = input("'S'    'N'\n").lower()
                if self.ch == 's':
                    self.print_paused("\nBaron Ro: Pues lo lmento, pero sabes que asi es este trabajo\n")
                    self.key = keyboard.read_event(suppress = True).name 
                    self.flag_b = False
                    break
                elif self.ch == 'n' :
                    self.print_paused("Baron Ro: Excelente, esto entonces no te molestara\n")
                    self.key = keyboard.read_event(suppress = True).name 
                    self.flag_b = False
                    break
                else:
                    print("Ingresa algo valido\n")
            
            self.print_paused("Baron Ro: Tu siguiente objetivo sera Antonieta Monteur\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Algo de informacion que deba saber?\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Baron Ro: Si, le gusta mucho las cosas dulces, tartas, pasteles, galletas, es realmente algo glotona, tal ves puedas lograr algo con eso\n")      
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Marie: Querido, voy a sali a hacer las compras, vuelvo mas tarde\n")
            self.print_paused("Hija de Erebos: Adios papi\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Claro cariño, suerte, adios pequeña te amo\n")   
            self.key = keyboard.read_event(suppress = True).name    
            self.print_paused("Baron Ro: Despues de que te hayas encargado buscame, tengo una oferta para ti\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Claro Baron, yo tambien quisiera hablar con usted sobre algo importante...\n")   
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Baron Ro: Nos veremos entonces\n")
            self.key = keyboard.read_event(suppress = True).name   
            self.clear_screen()
            self.print_paused("Informacion: Se cree que la señora Antonieta ira a una pasteleria a recoger un pedido, entra y completa la mision\n")
            self.key = keyboard.read_event(suppress = True).name     
            self.print_paused("Erebos: Ese pastel encaja con la descripcion de la orden de Antonieta\n")    
            self.key = keyboard.read_event(suppress = True).name     
            self.print_paused("Erebos: O tambien podria ser aquel...\nMaldicion\n")
            self.print_paused("Erebos: No tendre tiempo de evenarlos todos\n")
            self.key = keyboard.read_event(suppress = True).name 
            
            self.flag_b = True
            while self.flag_b:
                self.print_paused("Envenar los primeros 3\n")
                self.ch = input("'e' para envenenar\n").lower()
                if self.ch == 'e':
                    print("Envenenando ", end = "")
                    for _ in range(5):
                        time.sleep(0.5)
                        print("▪", end = "", flush = True)
                    self.flag_b = False
                else:
                    print("Invalido")   
            
            self.print_paused(" Pasteles envenenados\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Pastelero: Hola, puedo ayudarle en algo?\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Amm nop, creo que me he equivocado, podria decirme donde esta el bar?\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Pastelero: Esta a 3 cuadras de aqui\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Gracias, disculpe estos 3 pasteles de aqui ya estan vendidos?\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Pastelero: Si caballero, 2 le pertenecen a la señora Antonieta y el otro fue apartado hace 1 hora\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Ya veo, se ven deliciosos, muchas gracias, hasta pronto\n")
            self.key = keyboard.read_event(suppress = True).name 
            
            self.clear_screen()
            self.print_paused("Despacho del Baron Ro:\n")
            self.print_paused("Baron Ro: Sabia que serias rapido, pero no tanto, tiene menos de 3 horas que nos vimos\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: He tenido que apresurarme Baron, sabe que no me gusta tardar mas de lo necesario\n")
            self.key = keyboard.read_event(suppress = True).name           
            self.print_paused("Baron Ro: Bueno, me alegra tener a alguien tan eficaz a mi disposicion, has pasado buenos años desde que te conoci en aquel mercado sucio no?\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Si, han sido buenos años, como usted me lo prometio, las libras han sido lo ultimo de mis preocupaciones, pero...\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Baron Ro: Pero?, no habra pero cuando controle esta nacion\n")
            self.print_paused("Baron Ro: Es para eso que queria verte, tengo una lista de nombres mas grande de lo habitual, y necesito que me ayudes a... Darles nuestro mensaje\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Lo lamento Baron Ro, le agradezco por estos años que ha estado dandome medios para subsistir, pero...\n")
            self.print_paused("Baron Ro: Pero???\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Pero necesito que mi hija crezca en un entorno alejado de la violencia, no puedo ser su ejemplo a seguir si seguira los pasos de un asesino.\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Baron Ro: Con que si...\nTe atreves a rechazarme\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: No para nada Baron, es solo que debo ser mejor persona para mi hija\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Baron Ro: Tu hija podria crecer sin que le falte nnada, podrias ser uno de los hombres mas ricos de esta nacion\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Erebos: Agradezco la oferta Baron, pero Marie y yo tenemos planeado empezar un negocio propio con algunos ahorros\nEsa sera mi nueva vocacion, padre y probablemente repostero\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Baron Ro: Te arrepentiras muchacho, y cuando lo hagas, no te prometo que te estare esperando...\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Una vez caida la noche, regresas a casa\n")
            self.print_paused("Erebos: Marie, he regresado\n")
            self.print_paused("...\n")
            self.print_paused("Erebos(asustado): Marie?\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.print_paused("Tu esposa e hija estan en el suelo, hay un desastre y apenas respiran, buscando pistas en tu alrededor puedes notar algo sobre la mesa\n")
            self.key = keyboard.read_event(suppress = True).name 
            self.nono = pygame.mixer.Sound ("Nonono.mp3")   #Libreria que ayuda a crear un objeto de Pygame y tomar un archivo de audio 
            self.nono.play() #Reproduce archivo de audio
            cake = """
             _______________________________      __________________________
            /                               \    /                          \   
            | Is missing a piece             |     Just waiting to be eaten! |
            \_________________________     /     |   _______________________/
                          \   /_______\ /
               __....----''\./         | ````  '''''''''''
          _-'''             o          o            ````````-_
        .'                 \T/        /A\             
        |`-_              _/ \_       / \                  _-'|
        |   ```--....____                     ____....--'''   |
        |                `````-----------'''''                |
        |-__                                               __-|
        |   ~~~--________                     ________--~~~   |
        |                ~~~~~-----------~~~~~                |
        |-__                                               __-|
        |   ~~~--________                     ________--~~~   |
        |                ~~~~~-----------~~~~~                |
         `-_                                               _-'
            ```--....____                     ____....--'''
                         `````-----------'''''              

            """                                                    
        print(cake)
        self.print_paused("Erebos (en panico): NOOOO, AYUDA POR FAVOR!\n")
        self.key = keyboard.read_event(suppress = True).name 
        self.print_paused("Erebos: Van a estar bien lo prometo\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Hospital de Francia:\n")
        self.print_paused("Doctora: Ingirieron un quimico muy peligroso, estaran estables, pero vivas\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Se recuperaran Doctora? \n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Doctora: Tardar unos meses, la cantidad de veneno en ese pastel era la suficiente como para matarlas, por suerte no comieron mucho\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Doctora: Pero sera algo costoso señor Erebos, la situacio de su esposa y su hija es critica\n")
        self.print_paused("Doctora: En especial la de su hija, tiene tan solo 5 años\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: No importa, cueste lo que cueste\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: M****a, debo volver a trabajar con Baron Ro, de otra forma no podre manteerlas vivas.")
        self.clear_screen()
        self.print_paused("Despacho de Baron Ro. Enero de 1789\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Miren quien ha vuelto\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Baron usted no entiende, mi familia, mi espoa y mi hija...\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Deja de lloriquear, yo tambien soy padre y esposo, las esposas engañan y los hijos decepcionan\n")
        self.print_paused("Baron Ro: Asi que levantate y dime por que estas aqui, renunciaste, recuerdas?\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Lo se señor, pero necesito dinero, no pasaran de 3 meses con lo que tengo ahorrado, es muy costoso\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Este no es un banco y yo ya no soy tu jefe\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Usted gana, hare lo que sea con tal de obtener ese dinero...\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Esto te costara, ya habia mandado a alguien mas a completar tu lista\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Costar? Pero no tengo mas libras, todo lo que tengo es para mi esposa e hija\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Tomalo como un prestamo, por la cortesia de dejarte volver y en disculpa por haberte largado\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Cuanto me costara?\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: No estoy hablando de dinero, negociemos terminos\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Tu termina esta lista por mi, terminando y cuando logremos derrumbar a los revolucionarios, deberas hacer otra lista para mi\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Esta bien... Pero este sera el ultimo trabajo, despues de esto quiero reunciar, sin conscecuencias\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Baron Ro: Me parece que tenemos un trato entonces\n")
        self.print_paused("Presiona una tecla para continuar")
        self.key = keyboard.read_event(suppress = True).name
        self.clear_screen()
        self.print_paused("Casa de Erebos.\n")
        self.print_paused("Elige 1 item para llevar contigo\n")
        print("1.Cuchillo\2.Veneno\n3. Ir sin items")
        self.flag_b = True
        while self.flag_b:
            self.ch = int(input("Ingresa un numero"))
            if self.ch == 1:
                self.set_new_item("Cuchillo")
                self.print_paused("Presiona una tecla para continuar")
                self.key = keyboard.read_event(suppress = True).name
                self.flag_b = False
                break
            elif self.ch == 2:
                self.set_new_item("Veneno")
                self.print_paused("Presiona una tecla para continuar")
                self.key = keyboard.read_event(suppress = True).name
                self.flag_b = False
                break
            elif self.ch == 3:
                self.inventory_erebos("Mental_Health_Bar_S1.png")
                self.flag_b = False
                break
            else:
                print("Debe ser un item valido\n")
        
        
        
        #Primer asesinato
        self.clear_screen()
        self.text_blinking("Febrero. 1789\n")
        self.print_paused("Informacion: Tu primera victima sera Jean Dubois")
        self.decision = input("'a' asesinar a Jean Dubois, 'p' perdonar").lower()
        self.flag_b = True
        while self.flag_b:    
            if self.decision == 'a':
                self.print_paused("Erebos: Adiós, Jean Dubois\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha disminuido\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            elif self.decision == 'p':
                self.print_paused("Erebos: Te perdono, Jean Dubois\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha aumentado\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            else:
                self.print_paused("Decisión no válida...\n")
            
        
        
        
        #Segunda victima
        self.clear_screen()
        self.text_blinking("Marzo. 1789\n")
        self.print_paused("Informacion: Tu siguiente objetivo sera Isabelle Dupont")
        self.decision = input("'a' asesinar a Isabelle Dupont, 'p' perdonar").lower()
        self.flag_b = True
        while self.flag_b:    
            if self.decision == 'a':
                self.print_paused("Erebos: Adiós, Isabelle Dupont\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha disminuido\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            elif self.decision == 'p':
                self.print_paused("Erebos: Te perdono, Isabelle Dupont\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha aumentado\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            else:
                self.print_paused("Decisión no válida...\n")
        
        
        #Tercea victima
        self.clear_screen()
        self.text_blinking("Abril. 1789\n")
        self.print_paused("Informacion: Tu siguiente victima sera Claire Martin")
        self.decision = input("'a' asesinar a Claire Martin, 'p' perdonar").lower()
        self.flag_b = True
        while self.flag_b:    
            if self.decision == 'a':
                self.print_paused("Erebos: Adiós, Claire Martin\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha disminuido\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            elif self.decision == 'p':
                self.print_paused("Erebos: Te perdono, Claire Martin\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha aumentado\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            else:
                self.print_paused("Decisión no válida...\n")
        
        
        
        #Cuarta victima
        self.clear_screen()
        self.text_blinking("Mayo. 1789\n")
        self.print_paused("Informacion: Tu siguiente victima sera Francois Leclerc")
        self.decision = input("'a' asesinar a Francois Leclerc, 'p' perdonar").lower()
        self.flag_b = True
        while self.flag_b:    
            if self.decision == 'a':
                self.print_paused("Erebos: Adiós, Francois Leclerc\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha disminuido\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            elif self.decision == 'p':
                self.print_paused("Erebos: Te perdono, Francois Leclerc\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha aumentado\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            else:
                self.print_paused("Decisión no válida...\n")        
        
        
        
        #Quinta victima
        self.clear_screen()
        self.text_blinking("Junio. 1789\n")
        self.print_paused("Informacion: Tu siguiente victima sera Samir Eiffel")
        self.decision = input("'a' asesinar a Samir Eiffel, 'p' perdonar").lower()
        self.flag_b = True
        while self.flag_b:    
            if self.decision == 'a':
                self.print_paused("Erebos: Adiós, Samir Eiffel\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha disminuido\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            elif self.decision == 'p':
                self.print_paused("Erebos: Te perdono, Samir Eiffel\n")
                self.murders += 1
                self.print_paused("Tu salud mental ha aumentado\n")
                self.key = keyboard.read_event(suppress = True).name
                break
            else:
                self.print_paused("Decisión no válida...\n")  
        
        #Sexta victima
        self.clear_screen()
        self.text_blinking("Julio. 1789\n")
        self.print_paused("Informacion: Tu siguiente victima sera Adler ----")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Lo puedes encontrar en un bar llamado artisant")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Artisant, por lo que veo en esta lista, Adler viene mucho aqui. Entremos\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Adler: Me da una copa mas por favor cantinero\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Esta ocupada esta silla?\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Adler: Si\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Adler: Por un desconocido que se quiere sentar a un lado mio\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos se sienta junto a Adler\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos: Veo que lo esta pasando bien, que toma?\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Adler: Te importa mucho? Metete en tus asuntos\n")
        self.key = keyboard.read_event(suppress = True).name
        self.print_paused("Erebos:(No tengo tiempo que perder con este payaso, deberia encargarme aqui y ahora o esperar?)")
        self.ch = input("'p' pelear, 'c' charlar").lower
        if self.ch == 'p':
            self.print_paused("Erebos: Te acabas de meter en los mios amigo\n")
            self.key = keyboard.read_event(suppress = True).name
            punch = True
            self.hits = 0
            while punch:
                        self.ch = input("'g' golpear\n").lower()
                        if self.ch == 'g':
                            self.ou = pygame.mixer.Sound("Punch.mp3")
                            self.ou.play()    
                            self.hits += 1
                        if self.hits == 10:
                            self.print_paused("Erebos: Has tenido suficiente payaso?\n")
                            self.key = keyboard.read_event(suppress = True).name
                            self.print_paused("Adler: Que te pasa maniatico????\n")
                            self.key = keyboard.read_event(suppress = True).name
                            self.print_paused("Erebos lanza a Adler a la calle\n")
                            self.key = keyboard.read_event(suppress = True).name
                            self.print_paused("Adler: Espera hermano detente yo que te he hecho?\n")
                            self.key = keyboard.read_event(suppress = True).name
                            self.print_paused("Erebos Disociado: Que me has hecho??, te cruzaste conmigo")
                            self.key = keyboard.read_event(suppress = True).name
                            self.ou = pygame.mixer.Sound("Punch.mp3")
                            self.ou.play()
                            self.print_paused("Erebos: Tu nombre estaba en la lista equivocada, asi que acabemos esto\n")
                            self.key = keyboard.read_event(suppress = True).name
                            self.print_paused("Adler: Espera!\n")
                            self.key = keyboard.read_event(suppress = True).name
                            self.print_paused("Erebos lanza a Adler a un barranco \n")
                            self.murders += 1 
                            self.kill_a = True
                            break
        elif self.ch == 'c':
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: No hay necesidad de ser agresivos, solo queria charlar\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: Charlar, justo como mi padre cada que no me quiero involucrar en sus negocios\n")
            self.print_paused("Adler:(Imitando) Adler debes encargarte, Adler nunca llegaras a ser como yo, Adler no te involucres en mis asuntos\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Debe ser complicado, yo nunca tuve un padre, pero tengo una hija\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: Estas mejor asi, creeme\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Algunas copas juntos despues...\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Jajaja, ha sido una buena charla\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: Eres un tipazo hermao, oJalA nunKa te vayAz\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Solo ire a fumarme un cigarrillo afuera, me acompañas?\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: Claro, claro k zyy\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Sabes, debe ser muy dificil ser hijo de alguien importante, todos te ponen en estandares que no tienes por que llenar, no somos nuestros padres\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: A veces, la sociedad nos obliga a ser de una forma, pero debemos imponernos con nuestra escencia y gritar quienes somos\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: No somos quienes nos imponen que debemos ser, somos lo que elegimos ser, guste a quien guste\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler:(Grita) ADLER ROHAN SEÑORES\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Rohan?")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: Si, mi padre es Edouard Rohan\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Tu padre, m-m-m-me ha mandado a matarte\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: QUE!\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Esto o tiene sentido, por que haria eso?\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler Rohan: No tego idea, se suponia que debia atacar al hospital o a mi, o al menos eso esuchce de uno de sus trabajadores.\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Hospital???\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: Si, conoces a alguien ahi?\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Mi esposa y mi hija, estan en grabe peligro.\n")
            self.print_paused("Debo irme, gracias Adler\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Adler: Corre, tal ves aun las salves, no sabes como lo siento\n")
            self.lives_forgive += 1
        else:
            print("Ingresa una opcion valida\n")
            
        if self.lives_forgive > self.murders:
            if self.kill_a == True:
                self.print_paused("Erebos: ALTO BARON ROHAN!!\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Baron Ro: Muy tarde, si yo caigo con todos estos revolucionarios, tu caeras conmigo\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos: No, por favor, mi hija tan solo tiene 5 y mi esposa no te ha hecho nada, tomame a mi\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Baron Ro:Esto no hubiera pasado si hubieras cumplido mi lista\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Gracias a que has salvado mas personas, tu salud mental no esta tan degradada, sin embargo matar a Adler te ha impedido llehgar antes.\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erobos: Me han quitado lo que mas amo, todo me lo arrebataron, yo hare lo mismo con el\n")
                self.key = keyboard.read_event(suppress = True).name
                guillotina = """
                      __.--.____________.--.__
      (       _.------._       ).
       '._.--'    ||    '--._.'  )
        | |================| || (
        | ||               | ||  )
        | ||              _| || (
        | ||          _.-' | ||  )
        | ||      _.-'     | || (
        | ||  _.-'         | ||  )
        | |.-'             | || (
        | ||               | ||  )
        | ||               | || (
        | ||               | ||  )
        | ||               | || (
        | ||               | ||  )
        | ||               | || (
        | .---.            | ||  )
        | |   |            | || (
        | |   |            | ||  )
        | |  .'            | || (
        | | '              | ||  )
        | |  '.            | || (
        | |   |            | ||  )
        | |O__|  .))).     | || (
        | ||    ( O O )    | ||
        | ||===._ (_) _.===| ||
        | ||     '-.-'     | ||
        | ||               | ||
        | ||               | ||
        | ||    ______     | ||
        | ||   /      \    | ||
      __| ||  (\______/)   | ||_____
     /__| ||___) |''| (____| ||____/
    /___|_|/  (________)   |_|/___/
   /_____________________________/
                """
            
                self.print_paused("Tras perder a tu esposa y tu hija, te encargas de que Edouard Rohan tambien sea castigado")
                print(guillotina)
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Felicidades, has terminado el juego, sin embargo este no es el final bueno\n")
                time.sleep(5)
                self.clear_screen()
                self.text_blinking("Desarrollado por: Arturo Reza y Jared Lopez")
            else:
                self.print_paused("Hospital\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Baron Ro: Muy tarde, si yo caigo con todos estos revolucionarios y nobles tontos caeran conmigo\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos: No, por favor, mi hija tan solo tiene 5 y mi esposa no te ha hecho nada, tomame a mi\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Baron Ro:Esto no hubiera pasado si hubieras cumplido mi lista\n")
                self.key = keyboard.read_event(suppress = True).name
                self.sgun = pygame.mixer.Sound("Shot.mp3")
                self.sgun.play()
                self.print_paused("Has herido en el pecho a Edouard Rohan\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Erebos: Vamonos Marie, trae a la niña!!\n")
                self.key = keyboard.read_event(suppress = True).name
                self.print_paused("Marie: Debemos huir de aqui, los revolucionarios se han levantado\n")
                self.key = keyboard.read_event(suppress = True).name
                self.f2b = pygame.mixer.Sound("MetroB.mp3")
                self.f2b.play()
                self.print_paused("Felicidades, has logrado terminar el juego con el mejor final posible, Gracias por jugar!")
                time.sleep(5)
                self.text_blinking("Desarrollado por: Arturo Reza y Jared Lopez")                
            
        else:
            self.print_paused("No has conseguido llegar a tiempo, debido al elevado numero de muertes que has hecho, y al degradado estado de salud mental que tienes\n")
            self.print_paused("Has desbloqueado el peor final posible\n")
            self.key = keyboard.read_event(suppress = True).name
            self.print_paused("Erebos: Ya no vale la pena vivir, todo lo que hice, no significo nada...\n")
            print("...\n")
            print("...\n")
            print("...\n")
            print("...\n")
            self.print_paused("Presiona una tecla para terminar: \n")
            self.key = keyboard.read_event(suppress = True).name
            self.sgun = pygame.mixer.Sound("Shot.mp3")
            self.sgun.play()
            self.print_paused("Han llevado a tu hija y a tu esposa a la guillotina, tu salud mental esta en el nivel mas bajo.")
            self.text_blinking("Gracias por jugar, intenta nuevamente para llegar a otro final :)")
            self.clear_screen()
            time.sleep(5)
            self.text_blinking("Desarrollado por: Arturo Reza y Jared Lopez")
            
New_Game = Doloboros()
New_Game.start_screen()
