"""
Mettre des commentaires cf robot_arm.py
Objetcif : Fournir a la carte mere l'information sur la position des sukatas et leur etat
- fonction qui seche les sukatas 
- fonction qui verifie l'etat des sukatas
- fonction informe la carte mere sur quel sukata prendre
"""

#Set-up
#Importation des librairies
from machine import Pin
import time

#Initialisation des pins
signal_pin = 
pin_colonne_1 = 
pin_colonne_2 = 
pin_colonne_3 = 
pin_colonne_4 = 
pin_ligne_1 = 
pin_ligne_2 = 
pin_ligne_3 = 
pin_ligne_4 = 
pin_info_sup =

#creation de la classe
class Armoire:
  def __init__(self, signal_pin, pin_colonne_1, pin_colonne_2, pin_colonne_3, pin_colonne_4, pin_ligne_1, pin_ligne_2, pin_ligne_3, pin_ligne_4, pin_info_sup):
      self.matrice = [[-1,-1,-1,-1],
                      [-1,-1,-1,-1],
                      [-1,-1,-1,-1],
                      [-1,-1,-1,-1]]
      self.valeur_renvoye = [0,0]
      self.temps_sechage = ("donner le temps")
      self.etat_sukata = 0
      self.signal_pin = Pin(signal_pin, Pin.IN)
      self.pin_colonne_1 = pin_colonne_1
      self.pin_colonne_2 = pin_colonne_2
      self.pin_colonne_3 = pin_colonne_3
      self.pin_colonne_4 = pin_colonne_4
      self.pin_ligne_1 = pin_ligne_1
      self.pin_ligne_2 = pin_ligne_2
      self.pin_ligne_3 = pin_ligne_3
      self.pin_ligne_4 = pin_ligne_4
  
  def allumer_pin(self, pos, val):
    if pos[0] == 0:
      self.pin_ligne_1.value(1)
    else:
      self.pin_ligne_1.value(0)

    if pos[0] == 1:
      self.pin_ligne_2.value(1)
    else:
      self.pin_ligne_2.value(0)
    
    if pos[0] == 2:
      self.pin_ligne_3.value(1)
    else:
      self.pin_ligne_3.value(0)

    if pos[0] == 3:
      self.pin_ligne_4.value(1)
    else:
      self.pin_ligne_4.value(0)

    if pos[1] == 0:
      self.pin_colonne_1.value(1)
    else:
      self.pin_colonne_1.value(0)

    if pos[1] == 1:
      self.pin_colonne_2.value(1)
    else:
      self.pin_colonne_2.value(0)

    if pos[1] == 2:
      self.pin_colonne_3.value(1)
    else:
      self.pin_colonne_3.value(0)

    if pos[1] == 3:
      self.pin_colonne_4.value(1)
    else:
      self.pin_colonne_4.value(0)

    self.pin_info_sup.value(val)

  def next_position(self):
    while True:
      self.attendre_1_seconde()
      for i in range(4):
        for j in range(4):
          if self.est_sec(i, j):
            self.etat_sukata = 0
            self.valeur_renvoye = [i,j]
            self.allumer_pin([i,j], 0)
            return None
          elif self.est_vide(i, j):
            self.etat_sukata = 1
            self.valeur_renvoye = [i,j]
            self.allumer_pin([i,j], 1)
            return None

  def attendre_1_seconde(self):
    time.sleep(1)
    for i in range(4):
      for j in range(4):
        if self.matrice[i][j] > 0:
          self.matrice[i][j] -= 1

  def est_sec(self, ligne, col):
    return self.matrice[ligne][col] == 0

  def est_vide(self, ligne, col):
    return self.matrice[ligne][col] == -1

  def run(self):
    while True:
      self.next_position()
      self.allumer_pin(self.valeur_renvoye, self.etat_sukata)
      while self.signal_pin.value() != 1:
        self.attendre_1_seconde()
      if self.etat_sukata == 1:
        self.matrice[self.valeur_renvoye[0]][self.valeur_renvoye[1]] = self.temps_sechage
      else :
        self.matrice[self.valeur_renvoye[0]][self.valeur_renvoye[1]] = -1

  def __str__(self):
    info = "matrice actuelle : {self.matrice} \netat sukata = {self.etat_sukata} \nvaleur renvoye : {self.valeur_renvoye} \n\n\n"
    info_sup = "informations supplementaire :"
    info_lignes = "\npins ligne etats actuels : \n  1 : {self.pin_ligne_1.value()} \n  2 : {self.pin_ligne_2.value()} \n  3 : {self.pin_ligne_3.value()} \n  4 : {self.pin_ligne_4.value()}"
    info_colonnes = "\n\npins colonne etats actuels : \n  1 : {self.pin_colonne_1.value()} \n  2 : {self.pin_colonne_2.value()} \n  3 : {self.pin_colonne_3.value()} \n  4 : {self.pin_colonne_4.value()}"
    all_strings = info + info_sup + info_lignes + info_colonnes
    return fall_strings

#Appel et execution du code    
armoire = Armoire(signal_pin, pin_colonne_1, pin_colonne_2, pin_colonne_3, pin_colonne_4, pin_ligne_1, pin_ligne_2, pin_ligne_3, pin_ligne_4, pin_info_sup)
armoire.run()
  
