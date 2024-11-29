"""
Cette carte va simplement garder en memoire la situation de chaque composant du systeme.
Elle va utiliser ses digital pins pour indiquer un drapeau vert ou rouge pour l'action de chaque composant.
Ceci peut et doit etre modifie par tout les membres du groupe en fonction de ses besoins en flag, attention, n'utiliser par plusieur fois le meme pin.
"""

#Set-up
import machine
import time

#initialisation des pins
pin_in_bras_robotique = machine.Pin( , machine.Pin.IN)
pin_out_bras_robotique_presence_sukata = machine.Pin( , machine.Pin.OUT)
pin_out_bras_robotique_place_libre = machine.Pin( , machine.Pin.OUT)


while True:
  
