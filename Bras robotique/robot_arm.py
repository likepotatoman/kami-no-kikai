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
import asyncio
from machine import Pin
import math

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
motor_4_pin_dir = 
motor_4_pin_pul = 
motor_5_pin_dir = 
motor_5_pin_pul = 
servo_PWM_pin = 

#creation des classes et objets
class Motor:
    def __init__(self, motor_pin_dir, motor_pin_pul, gear_ratio):
        self.angle = 0
        self.pin_dir = motor_pin_din
        self.pin_pul = motor_pin_pul
        self.gear_ratio = gear_ratio
        self. fastest_step_time = 
        self.full_spin_time = self.gear_ratio * 200 * self.fastest_step_time
        
    async def spin(self, n_steps, direction, total_time):
        self.pin_dir.value(direction)
        one_step = total_time / n_steps
        for i in range(n_steps):
            self.pin_pul.value(1)
            await asyncio.sleep(one_step / 2)
            self.pin_pul.value(0)
            await asyncio.sleep(one_step / 2)

    def determine_time(self, steps):
        return round(abs(steps) * self.fastest_step_time)

    def determine_steps(self, angle):
        return round((angle / 360) * self.gear_ratio * 200)
        

shoulder = Motor(motor_1_pin_dir, motor_1_pin_pul, motor_1_gear_ratio)
elbow = Motor(motor_2_pin_dir, motor_2_pin_pul, motor_2_gear_ratio)
wrist = Motor(motor_3_pin_dir, motor_3_pin_pul, motor_3_gear_ratio)
body = Motor(motor_4_pin_dir, motor_4_pin_pul, motor_4_gear_ratio)
legs = Motor(motor_5_pin_dir, motor_5_pin_pul, motor_5_gear_ratio)


class Servo:
    def __init__(self, PWM_pin, min_PW, max_PW): #PW are in ms
        self.PWM_pin = PWM(PWM_pin)
        self.PWM_pin.freq(50)
        self.max_DC = 65535 * (max_PW / 20) #DC stands for duty cycle
        self.min_DC = 65535 * (min_PW / 20)
        self.delta_DC = self.max_DC - self.min_DC

    def move(self, angle):
        percentage = angle / 180
        duty_cycle = self.delta_DC * percentage + self.min_DC
        self.PWM_pin.duty_u16(round(duty_cycle))

    def open(self):
        self.move(0)

    def close(self):
        self.move(180)

claw = Servo(servo_PWM_pin)

class Robot:
    def __init__(self):
        self.arm_1_length = 50
        self.arm_2_length = 50
        self.position_rail = 0
        self.tau = 0
        self.beta_prime = 0
        self.lambda = 0

    def move(self, M_x_but, M_y_but, phi_but, position_type = 0):
        #calculs d'angles intermediaires
        
        #On definit certaines droites et segments utiles pour des calculs futurs, B(0, -100)
        OM = math.sqrt(M_x_but**2 + M_y_but**2)
        BM = math.sqrt(M_x_but**2 + (M_y_but + 100)**2)
        BO = 100 
        
        #On cherche alpha, l'angle relatif que le moteur doit prendre par rapport a la droite OM
        if position_type == 0:
            alpha_but = math.degrees( math.acos((self.arm_1_length**2 +  OM**2 - self.arm_2_length**2) / (2 * self.arm_2_length * OM)) )
        else:
            alpha_but = math.degrees( - math.acos((self.arm_1_length**2 +  OM**2 - self.arm_2_length**2) / (2 * self.arm_2_length * OM)) )
        
        #On cherche theta, l'angle entre la verticale et la semi-doite [OM) dans le sens trigonometrique
        if M_x_but > 0:
            theta_but = math.degrees( math.acos((OM**2 + BO**2 - BM**2) / (2 * BO * OM)) ) 
        elif M_x_but < 0:
            theta_but = math.degrees( 2 * math.pi - math.acos((OM**2 + BO**2 - BM**2) / (2 * BO * OM)) )
        else:
            if M_y_but > 0:
                theta_but = 180
            else : 
                theta_but = 0
        
        #On en deduit tau, l'angle que doit prendre le moteur 1 : shoulder
        tau_but = theta_but + alpha_but
        
        #On cherche beta, normalement nous pouvons trouver facilement mais je generalise pour des bras de longueur differentes
        beta_but = math.degrees( math.acos((self.arm_1_length**2+ self.arm_2_length**2 - OM**2 ) / (2 * self.arm_2_length * self.arm_1_length)) )

        #On peut donc determiner beta_prime, l'angle que doit prendre le moteur 2 : elbow
        if position_type == 0:
            beta_prime_but = -(180 - beta_but)
        else : 
            beta_prime_but = 180 - beta_but

        #On calcule les coordonnees de I
        I_x_but = math.cos(math.radians(tau_but - 90)) * 50
        I_y_but = math.sin(math.radians(tau_but - 90)) * 50
     
        #On determine epsilone decoulant de cette nouvelle configuration
        delta_x_IM = M_x_but - I_x_but
        delta_y_IM = M_y_but - I_y_but
        if delta_x_IM > 0:
            if delta_y_IM > 0:
                #M above to the right
                epsilon_but = 
            else :
                #M below to the right
                epsilon_but = 
        else : 
            if delta_y_IM > 0:
                #M above to the left
                epsilon_but = 
            else : 
                #Mbelow to the left
                epsilon_but = 
        
        #calcul d'angles final
        delta_tau = optimize_angle(tau_but - self.tau)
        delta_beta_prime = optimize_angle(beta_prime_but - self.beta_prime)
        delta_phi =  optimize_angle(phi_but - (epsilon + self.lambda))
        
        #Calculs vitesses de chaque moteur
        delta_time = max([shoulder.determine_time(shoulder.determine_steps(delta_tau)), elbow.determine_time(elbow.determine_steps(delta_beta_prime)), wrist.determine_time(wrist.determine_steps(delta_phi))])

        async def simultanious_spin(delta_tau, delta_beta_prime, delta_phi, delta_time):
           task1 = asyncio.create_task(shoulder.spin(abs(shoulder.determine_steps(delta_tau), sign(shoulder.determine_steps(delta_tau)), delta_time))
           task2 = asyncio.create_task(elbow.spin(abs(elbow.determine_steps(delta_beta_prime)), sign(elbow.determine_steps(delta_beta_prime)), delta_time))
           task3 = asyncio.create_task(elbow.spin(abs(wrist.determine_steps(delta_phi)), sign(wrist.determine_steps(delta_phi)), delta_time))
           await task1
           await task2
           await task3

        asyncio.run(simultanious_spin(delta_tau, delta_beta_prime, delta_phi, delta_time))
        
        self.tau = tau_but
        self.beta_prime = beta_prime_but
        self.lambda = lambda_but

#Creation des fonctions
def optimize_angle(angle):
    if abs(angle % 360) < abs((angle % 360) - 360):
        return angle % 360
    return angle % 360 - 360

def sign(x): #Attention il faut bien configurer les moteurs tels que quand dir == HIGH, ils tournent dans le sens anti-horraire / trigonometrique
    if x > 0:
        return 1
    elif x < 0:
        return 0
    else:
        return 1

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
  
