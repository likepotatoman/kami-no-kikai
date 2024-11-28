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
limit_switch_1_in_pin =  #limit switch au niveau du prep papier
limit_switch_2_in_pin =  #limit switch au niveau du bras robotique

#Creation des fonctions
def aller_robot():
  while limit_switch_2_in_pin == False:
    #tourner le motor
  signal_out_pin.value(1)
  time.sleep(100)
  signal_out_pin.value(0)

def aller_papier():
  while limit_switch_2_in_pin == False:
    #tourner le motor dans le sens inverse
  signal_out_pin.value(1)
  time.sleep(100)
  signal_out_pin.value(0)

#Loop
while True:
  while signal_in_pin.value() == 0:
    time.sleep(50)
  aller_robot()
  while signal_in_pin.value() == 0:
    time.sleep(50)
  aller_papier()
  
  
