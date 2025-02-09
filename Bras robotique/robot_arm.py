#IL RESTE LE PHI/SIGMA A VERIFIER, CODE INCOMPLET


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
import time
from machine import Pin, PWM
import math

#Initialisation des pins
armoire_col_1 = Pin(, Pin.IN)
armoire_col_2 = Pin(, Pin.IN)
armoire_col_3 = Pin(, Pin.IN)
armoire_col_4 = Pin(, Pin.IN)
armoire_lin_1 = Pin(, Pin.IN)
armoire_lin_2 = Pin(, Pin.IN)
armoire_lin_3 = Pin(, Pin.IN)
armoire_etat = Pin(, Pin.IN)
prep_station_signal = Pin(, Pin.OUT)
motor_1_pin_dir = Pin(, Pin.OUT)
motor_1_pin_pul = Pin(, Pin.OUT)
motor_1_gear_ratio = 
motor_2_pin_dir = Pin(, Pin.OUT)
motor_2_pin_pul = Pin(, Pin.OUT)
motor_2_gear_ratio = 
motor_3_pin_dir = Pin(, Pin.OUT)
motor_3_pin_pul = Pin(, Pin.OUT)
motor_3_gear_ratio = 
motor_4_pin_dir = Pin(, Pin.OUT)
motor_4_pin_pul = Pin(, Pin.OUT)
motor_4_gear_ratio = 
motor_5_pin_dir = Pin(, Pin.OUT)
motor_5_pin_pul = Pin(, Pin.OUT)
motor_5_gear_ratio = 
servo_PWM_pin = Pin(, Pin.OUT)
position_limit_switch_input_pin =
claw_limit_switch_input_pin =

#creation des classes et objets
class Motor:
    def __init__(self, motor_pin_dir, motor_pin_pul, gear_ratio):
        self.pin_dir = motor_pin_dir
        self.pin_pul = motor_pin_pul
        self.gear_ratio = gear_ratio
        self. fastest_step_time = 500 #in micro-seconds
        
    def spin(self, n_steps, direction):
        self.pin_dir.value(direction)
        for i in range(n_steps):
            self.pin_pul.value(1)
            time.sleep_us(self.fastest_step_time)
            self.pin_pul.value(0)
            time.sleep_us(self.fastest_step_time)

    def determine_steps(self, angle):
        return round((angle / 360) * self.gear_ratio * 200)
        

shoulder = Motor(motor_1_pin_dir, motor_1_pin_pul, motor_1_gear_ratio)
elbow = Motor(motor_2_pin_dir, motor_2_pin_pul, motor_2_gear_ratio)
wrist = Motor(motor_3_pin_dir, motor_3_pin_pul, motor_3_gear_ratio)
body = Motor(motor_4_pin_dir, motor_4_pin_pul, motor_4_gear_ratio)
legs = Motor(motor_5_pin_dir, motor_5_pin_pul, motor_5_gear_ratio)


class Limit_Switch:
    def __init__(self, input_pin):
        self.input_pin = input_pin
    
    def state(self):
        return self.input_pin.value()

position_limit_switch = Limit_Switch(position_limit_switch_input_pin)
claw_limit_switch = Limit_Switch(claw_limit_switch_input_pin)


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

    def release(self):
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
        self.sigma = 0
        self.M_x = 0
        self.M_y = -100
        self.position_type = 0

    def move(self, M_x_but, M_y_but, phi_but, position_type = 0):

        #handling edge-cases
        if M_x_but == 0 and M_y_but == 0 :
            shoulder.spin(shoulder.determine_steps(self.tau), 1)
            elbow.spin(elbow.determine_steps(self.beta_prime + 180), 1)
            wrist.spin(wrist.determine_steps(self.sigma), 1)
            wrist.spin(abs(wrist.determine_steps(optimize_angle(phi_but))), sign(wrist.determine_steps(optimize_angle(phi_but))))
            
            self.tau = 0
            self.beta_prime = 180
            self.sigma = phi_but 
            self.M_x = M_x_but
            self.M_y = M_y_but
            self.position_type = position_type
        
        else : 
            #On definit certaines droites et segments utiles pour des calculs futurs, B(0, -100)
            OM = math.sqrt(M_x_but**2 + M_y_but**2)
            BM = math.sqrt(M_x_but**2 + (M_y_but + 100)**2)
            BO = 100
            print(f"OM : {OM}")
            print(f"BM : {BM}")
            
            #On cherche alpha, l'angle relatif que le moteur doit prendre par rapport a la droite OM
            if position_type == 0:
                alpha_but = math.degrees( math.acos((self.arm_1_length**2 +  OM**2 - self.arm_2_length**2) / (2 * self.arm_2_length * OM)) )
            else:
                alpha_but = math.degrees( - math.acos((self.arm_1_length**2 +  OM**2 - self.arm_2_length**2) / (2 * self.arm_2_length * OM)) )
            

            print(f"alpha but : {alpha_but}")
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
            
            print(f"theta but : {theta_but}")
            
            #On en deduit tau, l'angle que doit prendre le moteur 1 : shoulder
            tau_but = theta_but + alpha_but
            print(f"tau but : {tau_but}")
            
            #On cherche beta, normalement nous pouvons trouver facilement mais je generalise pour des bras de longueur differentes
            beta_but = math.degrees( math.acos((self.arm_1_length**2+ self.arm_2_length**2 - OM**2 ) / (2 * self.arm_2_length * self.arm_1_length)) )
            print(f"beta but : {beta_but}")
            #On peut donc determiner beta_prime, l'angle que doit prendre le moteur 2 : elbow
            if position_type == 0:
                beta_prime_but = -(180 - beta_but)
            else : 
                beta_prime_but = 180 - beta_but
            
            print(f"beta prime but : {beta_prime_but}")
            #On calcule les coordonnees de I
            I_x_but = math.cos(math.radians(tau_but - 90)) * 50
            I_y_but = math.sin(math.radians(tau_but - 90)) * 50
            print(f"I x but : {I_x_but}")
            print(f"I y but : {I_y_but}")
            
            #On determine epsilone decoulant de cette nouvelle configuration
            delta_x_IM = M_x_but - I_x_but
            delta_y_IM = M_y_but - I_y_but
            print(f"delta x IM : {delta_x_IM}")
            print(f"delta y IM : {delta_y_IM}")
            
            if delta_x_IM > 0:
                if delta_y_IM > 0:
                    #M above to the right
                    epsilon = 90 + math.degrees(math.atan(delta_y_IM / delta_x_IM))
                else :
                    #M below to the right
                    epsilon = 90 - math.degrees(math.atan(delta_y_IM / delta_x_IM))
            else : 
                if delta_y_IM > 0:
                    #M above to the left
                    epsilon = 270 - math.degrees(math.atan(delta_y_IM / delta_x_IM))
                else : 
                    #Mbelow to the left
                    epsilon = 270 + math.degrees(math.atan(delta_y_IM / delta_x_IM))
            print(f"epsilon : {epsilon}")
            
            #calcul d'angles final
            delta_tau = optimize_angle(tau_but - self.tau)
            delta_beta_prime = optimize_angle(beta_prime_but - self.beta_prime)
            delta_phi =  optimize_angle(phi_but - (epsilon + self.sigma))
            print(f"delta tau : {delta_tau}")
            print(f"delta beta prime : {delta_beta_prime}")
            print(f"delta phi : {delta_phi}")
            
            #Calculs vitesses de chaque moteur
            shoulder.spin(abs(shoulder.determine_steps(delta_tau)), sign(shoulder.determine_steps(delta_tau)))
            elbow.spin(abs(elbow.determine_steps(delta_beta_prime)), sign(elbow.determine_steps(delta_beta_prime)))
            wrist.spin(abs(wrist.determine_steps(delta_phi)), sign(wrist.determine_steps(delta_phi))) 
            
            self.tau = tau_but
            self.beta_prime = beta_prime_but
            self.sigma = phi_but - epsilon
            self.M_x = M_x_but
            self.M_y = M_y_but
            self.position_type = position_type
            
            print("\n\n")
        
    def negative_rail_move(self):
        while position_limit_switch.state() == 1: 
            await legs.spin(1, 0, legs.fastest_step_time)
            
        while position_limit_switch.state() == 0: 
            await legs.spin(1, 0, legs.fastest_step_time)

    def positive_rail_move(self):
        while position_limit_switch.state() == 1: 
            await legs.spin(1, 1, legs.fastest_step_time)
            
        while position_limit_switch.state() == 0: 
            await legs.spin(1, 1, legs.fastest_step_time)
    

    def rail_move(self, goal_position):
        while goal_position != self.rail_position: 
            if goal_position > self.rail_position:
                positive_rail_move()
                self.rail_position += 1
            else : 
                negative_rail_move()
                self.rail_position -= 1

    def rotate_quarter_left(self):
        await body.spin(body.determine_steps(90), 0, 5)

    def rotate_quarter_right(self):
        await body.spin(body.determine_steps(90), 0, 5)
        
    def lower_claw(self):
      while claw_limit_switch.state() == 0 :
        move(self.M_x, self.M_y - 0.1, 0)
      
    def raise_claw(self):
      move(self.M_x, self.M_y + 5, 0)

robot = Robot()


#Creation des fonctions
def optimize_angle(angle):
    if abs(angle % 360) < abs((angle % 360) - 360):
        return angle % 360
    return angle % 360 - 360

def sign(x): #Attention il faut bien configurer les moteurs tels que quand dir == 1, ils tournent dans le sens anti-horraire / trigonometrique
    if x > 0:
        return 0
    elif x < 0:
        return 1
    else:
        return 0

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

def drop_mixer(self):
  move()
  move()
  claw.release()
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
