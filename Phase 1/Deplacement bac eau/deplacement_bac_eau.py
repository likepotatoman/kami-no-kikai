"""
Mettre des commentaires cf robot_arm.py
Objetcif : Déplacer un bac d'eau de 60kg sur une longueur d'1m
Dimensions : 50cm (longueur), 35cm (largeur), 45cm (hauteur)
- fonction qui emmene d'un point A à un point B
- fonction inverse qui emmene d'un point B à un point B
"""

#Set-up
#Importation des librairies
import machine
import time

#Initialisation des pins
signal_in_pin = 
signal_out_pin = 

#Creation des fonctions
def aller_robot():


def aller_papier():



#Loop
while True:
  while signal_in_pin.value() == 0:
    time.sleep(50)
  aller_robot()
  while signal_in_pin.value() == 0:
    time.sleep(50)
  aller_papier()
  
  
