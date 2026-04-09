"""
Nous allons apprendre à utiliser les variables.
Connaître leur utilité et aussi les différents types de variables
"""

# Définition de variables

age = 29
name = "Konan Koffi N'guessan Bernard"
job = 'Cil Engineer / Surveyor'

print(f"Je suis {name} et j'ai {age} ans.\nEnfin je travaille en tant qu'un {job}.")

# Calcul du périmètre et de l'ai d'un cercle

roof = 3.5
PI = 3.1415

perimeter = 2 * PI * roof
circle_area = PI * roof * roof

print(f"Un cercle de rayon {roof} cm a pour:\n\tPérimètre: {perimeter}cm\n\tAire: {circle_area}cm2")

# Reassigner une variable
chat = "Michou"
print(f"Chat avant: {chat}\n")

chat = "Bunny"
print(f"Chat après: {chat}\n")

# Casting ou Conversion de type
num = "10"
num = int(num) # Transformer un chaine valide en nombre entier

calculus = str(num * 20)

print("Num x 20 = " + calculus)
