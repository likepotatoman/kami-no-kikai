"""
Cette carte va simplement garder en memoire la situation de chaque composant du systeme.
Elle va utiliser ses digital pins pour indiquer un drapeau vert ou rouge pour l'action de chaque composant.
Ceci peut et doit etre modifie par tout les membres du groupe en fonction de ses besoins en flag, attention, n'utiliser par plusieur fois le meme pin.

Liste des connections : 
  CM --> Bras robotique : 
    Position du sukata (numbre de colonnes + nombre de lignes)
    sukata ouvert (1)
    sukata sec (1)
    START (1)
  Bras robotique --> CM :
    Fini (1)

  CM --> Prep. papier : 
    START (1)
    Allumer shredder + mixer (1)
  Prep. papier --> CM :
    Papier (1)

  CM --> Station Sechage : 
    START (1)
    Fini (1)
  Station Sechage --> CM :
    Position sukata (numbre de colonnes + nombre de lignes)
    Sukata ouvert (1)
    Sukata sec (1)
"""

#Set-up
import machine
import time

#initialisation des pins
pin_in_bras_robotique = machine.Pin( , machine.Pin.IN)
pin_out_bras_robotique_presence_sukata = machine.Pin( , machine.Pin.OUT)
pin_out_bras_robotique_place_libre = machine.Pin( , machine.Pin.OUT)


while True:
  
