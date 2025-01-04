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
import math
import _thread

#Initialisation des pins
signal_in_pin = 
signal_out_pin =
vacuum_signal =
shredder_signal = 
motor_1_pin_dir = 
motor_1_pin_pul = 
motor_2_pin_dir = 
motor_2_pin_pul = 
motor_3_pin_dir = 
motor_3_pin_pul = 
servo_pin = 

#Initialisation des variables des positions initiales
motor_1_fini = False
motor_2_fini = False
motor_3_fini = False
motor_4_fini = False
motor_5_fini = False
position_rail = 
sukata_position = [0,0]
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
def sign(x): #Attention il faut bien configurer les moteurs tels que quand dir == HIGH, ils tournent dans le sens anti-horraire / trigonometrique
    if x > 0:
        return 1
    elif x < 0:
        return 0
    else:
        return 1


def spin_motor_1(n_steps, direction, speed): #motor at O
  global motor_1_fini
  motor_1_pin_dir.value(direction)
  for i in range(n_steps):
    motor_1_pin_pul.value(HIGH)
    time.sleep(speed)
    motor_1_pin_pul.value(LOW)
    time.sleep(speed)
  motor_1_fini = True
    

def spin_motor_2(n_steps, direction, speed): #motor at I
  global motor_2_fini
  motor_2_pin_dir.value(direction)
  for i in range(n_steps):
    motor_2_pin_pul.value(HIGH)
    time.sleep(speed)
    motor_2_pin_pul.value(LOW)
    time.sleep(speed)
  motor_2_fini = True

def spin_motor_3(n_steps, direction, speed): #motor at M
  global motor_3_fini
  motor_3_pin_dir.value(direction)
  for i in range(n_steps):
    motor_3_pin_pul.value(HIGH)
    time.sleep(speed)
    motor_3_pin_pul.value(LOW)
    time.sleep(speed)
  motor_3_fini = True

def spin_motor_4(n_steps, direction): #motor for rail
  global motor_4_fini
  motor_4_pin_dir.value(direction)
  for i in range(n_steps):
    motor_4_pin_pul.value(HIGH)
    time.sleep(0.5) #a changer si besoin
    motor_4_pin_pul.value(LOW)
    time.sleep(0.5) #a changer si besoin
  motor_4_fini = True

def spin_motor_5(n_steps, direction): #motor on rotating platform
  global motor_5_fini
  motor_5_pin_dir.value(direction)
  for i in range(n_steps):
    motor_5_pin_pul.value(HIGH)
    time.sleep(0.5) #a changer si besoin
    motor_5_pin_pul.value(LOW)
    time.sleep(0.5) #a changer si besoin
  motor_5_fini = True

def turn_on_vacuum():
  vacuum_signal.value(HIGH)
  time.sleep(1)
  vacuum_signal.value(LOW)

def turn_off_vacuum():
  vacuum_signal.value(HIGH)
  time.sleep(1)
  vacuum_signal.value(LOW)

def turn_on_shredder_mixer():
  shredder_signal.value(HIGH)
  time.sleep(1)
  shredder_signal.value(LOW)
  
def turn_off_shredder_mixer():
  shredder_signal.value(HIGH)
  time.sleep(1)
  shredder_signal.value(LOW)  

def move(M_x_but, M_y_but, phi_but):
  global alpha_actuel, theta_actuel, tau_actuel, beta_actuel, beta_prime_actuel, epsilon_actuel, phi_actuel, lambda_actuel, I_x_actuel, I_y_actuel, M_x_actuel, M_y_actuel, motor_1_fini, motor_2_fini, motor_3_fini
  #calculs d'angles intermediaires
  alpha_but = 
  theta_but = 
  tau_but = 
  beta_but = 
  beta_prime_but = 
  epsilon_but =  
  I_x_but = 
  I_y_but = 

  #calcul d'angles final
  delta_theta = 
  delta_beta_prime = 
  delta_phi = 

  #calcul de pas associes
  motor_1_steps = 
  motor_2_steps = 
  motro_3_steps = 
  
  #Calculs vitesses de chaque moteur
  motor_1_speed = 
  motor_2_speed =
  motor_3_speed =
  
  motor_1_fini = False
  motor_2_fini = False
  motor_3_fini = False
  
  _thread.start_new_thread(spin_motor_1, (abs(moteur_1_steps), sign(moteur_1_steps), motor_1_speed))
  _thread.start_new_thread(spin_motor_2, (abs(moteur_2_steps), sign(moteur_2_steps), motor_2_speed))
  _thread.start_new_thread(spin_motor_3, (abs(moteur_3_steps), sign(moteur_3_steps), motor_3_speed))

  while motor_1_fini == False or motor_2_fini == False or motor_3_fini == False:
    time.sleep(1)
  
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

def close_claw():


def open_claw():
  

def neutral():
  move()

def sukata_pass(n):
  for i in range(n):
    move()
    move()
    move()
    move()

def lower_claw():
  while #limit swtch off :
    goal_y = M_y_actuel - #valeur arbitraire
    move(M_x_actuel, goal_y, 0)
  
def raise_claw():
  move(M_x_actuel, M_y_actuel - #valeur arbitraire, 0)

def recup_sukata():
  move()
  lower_claw()
  close_claw()
  raise_claw()
  neutral()

def drop_sukata():
  move()
  open_claw()
  neutral()

def recup_mixer():
  move()
  lower_claw()
  close_claw()
  raise_claw()
  neutral()

def drop_mixer():
  move()
  open_claw()
  neutral()

def recup_vacuum():
  move()
  lower_claw()
  close_claw()
  raise_claw()
  neutral()

def drop_vacuum():
  move()
  open_claw()
  neutral()

def recup_paper():
  move()
  move()
  turn_on_vacuum() 
  move()
  neutral()

def drop_paper():
  move()
  turn_off_vacuum()
  neutral()

def negative_rail_move():
  while #limit swtch on : 
    spin_motor_4( , #neg)

def positive_rail_move():
  while #limit swtch on : 
    spin_motor_4( , #pos)

def rail_move(goal_position):
  global position
  while goal_position != position : 
    if goal_position > position:
      positive_rail_move()
    else : 
      negative_rail_move():

def rotate_quarter_left():
  spin_motor_5(#arbitraire, 1)

def rotate_quarter_right():
  spin_motor_5(#arbitraire, 0)


def pass_cycle():
  rail_move(#position du  vacuum)
  recup_vacuum()
  rail_move(#position du papier)
  recup_paper()
  rail_move(#position du shredder)
  turn_on_shredder_mixer()
  drop_paper()
  rail_move(#position du vacuum)
  drop_vacuum()
  rail_move(#position du mixer)
  recup_mixer()
  
  
  

  
#Loop
while True:
  
