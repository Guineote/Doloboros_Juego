import time
import os
import pygame
import sys

from tkinter import *
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
def show_opt(options, selected):
        time.sleep(1.5)
        #clear_screen()
        
        for i, opcion in enumerate(options, start = 1):
            if i == selected:
                print(f"\033[1;37;40m{i}. {opcion}\033[0m")  # Resaltar la opción seleccionada
            else:
                print(f"{i}. {opcion}")

def confirm_opt():
    print("¿Estas seguro que deseas elegir este personaje?")
    aux = input("Ingresa 's' o 'n'\n")
    if aux == 's':
        print("Comezando historia de Fenrir Vortex...")
        print("\tLoading ", end = "")
        for _ in range(5):
            time.sleep(0.5)
            print("▪", end = "", flush = True)
    if aux == 'n':
            pass
   
    
def start_screen():
        print("\tLoading ", end = "")
        for _ in range(5):
            time.sleep(0.5)
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
        """
        print(screen)
        a=0
        while a == 0:
            s = input("Bienvenido, ingresa 's' para iniciar: ")
            if (s == 's'):
                name = input("Ingresa tu nombre: ")
                print("Hola, " + name + ", beinvenid@ a Doloboros")
                print("Para empezar deberas escoger una historia la cuál seguir. Tus opciones son:\n")
                a = 1
            else:
                print("Opcion invalida, igresa s para iniciar")
    
def Fenrir_History():
        clear_screen()
        
        
def Erebos_History():
        clear_screen()
        
def inventory():
    pass

def set_new_item():
    pass

def delete_item():
    pass

def Fenrir_Chapter():
    mental_health = 0
    murders = 0
    lives_forgive = 0

def Erobos_Chapter():
    mental_health = 0
    murders = 0
    lives_forgive = 0



start_screen()
characters = ["Fenrir Vortex", "Erebos Perilse"]
selection = 1
choice = False
while choice == False:
    show_opt(characters, selection)
    try:
        selected = int(input("\nIngresa el número de la opción deseada: "))
        if 1 <= selected <= len(characters):
            selection = selected
    except ValueError:
        print("Opcion invalida")
    #selected = int(input("\nIgresa el número de personaje que elegiras: "))
    if selection == 1:
        print("Fenrir Vortex:\n")
        Fenrir_History()
        
    if selection == 2:
        print("Erebos Perilse:\n")
        Erebos_History()
        