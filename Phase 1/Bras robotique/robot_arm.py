"""
Ce code va donc permettre de faire bouger un bras robotique avec 3 joints avec des stepper motor et une pince avec un servo quand il va recevoir un signal de la carte mere.
Il va :
- aller se placer a un lieu donne
- envoyer un signal a la carte mere qui va envoyer un autre signal a un pusher qui va pousser le sukata sur le bras
- fermer la pince
- faire passer le sukata dans le bac d'eau
- le secouer
- repeter x fois les deux dernieres etapes (x a definir par tatonnement)
- placer le sukata pour qu'il soit recupere par le systeme de sechage

Dans ce code, nous allons creer :
- une fonction qui va ouvrir et fermer la pince
- une fonction emmener le bras a un point donne avec un angle donne
- une liste d'instructions qui va faire passer le sukata dans l'eau
"""

#Set-up
#importation des librairies
import machine
import time

#Initialisation des pins
signal_in_pin = 
signal_out_pin =
motor_1_pin = 
motor_2_pin = 
motor_3_pin = 
servo_pin = 

#Initialisation des variables des positions initiales
alpha_actuel = 
theta_actuel = 
tau_actuel = 
beta_actuel = 
beta_prime_actuel = 
epsilon_actuel = 
phi_actuel = 
lambda_actuel = 
I_x_actuel = 
I_y_actuel = 
M_x_actuel = 
M_y_actuel = 

#Creation des fonctions
def spin_motor_1(n_steps, direction):


def spin_motor_2(n_steps, direction):


def spin_motor_3(n_steps, direction):


def move(M_x_but, M_y_but, phi_but):
  alpha_but = 
  theta_but = 
  tau_but = 
  beta_but = 
  beta_prime_but = 
  epsilon_but =  
  I_x_but = 
  I_y_but = 

  delta_theta = 
  delta_beta_prime = 
  delta_phi = 

  spin_motor_1()
  spin_motor_2()
  spin_motor_3()

  alpha_actuel = alpha_but
  theta_actuel = theta_but
  tau_actuel = tau_but
  beta_actuel = beta_but
  beta_prime_actuel = beta_prime_but
  epsilon_actuel = epsilon_but
  phi_actuel = phi_but
  lambda_actuel = lambda_but
  I_x_actuel = I_x_but
  I_y_actuel = I_y_but
  M_x_actuel = M_x_but
  M_y_actuel = M_y_but

def fermer_pince():


def ouvrir_pince():
  

def neutral():
  move()

def sukata_pass(n):
  for i in range(n):
    move()
    move()
    move()
    move()

def recup_sukata():
  move()
  fermer_pince()

def drop_sukata():
  move()
  ouvrir_pince()


#Loop
while True:
  
