import math
an = float(input('Digite seu angulo:'))
seno = math.sin(math.radians(an))
print(f'O angulo de {an} tem o seno de: {seno:.2f}.')
cosseno = math.cos(math.radians(an))
print(f'O angulo de {an} tem o cosseno de: {cosseno:.2f}.')
tangente = math.tan(math.radians(an))
print(f'O angulo de {an} tem a tangente de: {tangente:.2f}.')
