
weight = 41.5

ground_ship = "Ground Shipping"
premium_ground  = 125.00

if weight == 2 or weight < 2:
  cost_ground = weight * 1.50 + 20.00
elif weight > 2 or weight <= 6:
  cost_ground = weight * 3.00 + 20.00 
elif weight > 6 or weight <= 10:
  cost_ground = weight * 4.00 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00

print(cost_ground)
print(premium_ground)

weight = 41.5

drone_shipping = "Drop Shipping"

if weight == 2 or weight < 2:
  cost_drop_ship = weight * 4.50 
elif weight > 2 or weight <= 6:
  cost_drop_ship = weight * 9.00 
elif weight > 6 or weight <= 10:
  cost_drop_ship = weight * 12.00 
else: 
    cost_drop_ship = weight * 14.25 

print(cost_drop_ship)



import math

pi = math.pi

def whatpimeans(alpha = 'abcdefghijklmnopqrstuvwxyz'):
    #create a dictionnary linking alphabet to 'secret encryption'
    #dico = {85:'a', 24:'b',32:'c', [...],10:'z'}
    dico = { k:v for k, v in \
        zip([85,24,32,64,11,52,91,79,78,99,62,27,74,35,14,
             16,66,81,19,39,13,33,45,49,95,10],
            alpha.upper())}
    
    #take the number PI as string and prepare it for decoding
    crypt = str(math.pi)
    crypt.replace('.','')
    code = []
        #reverse the string and group 2 by 2 to form a list
    for i in range(0, len(crypt), 2):
        code += crypt[:-1][i:i+2]
    
    #take the modified string and try to decode
    decrypt = ''
    for binom in code :
        decrypt += dico[binom]
    
    #stuck somewhere ? try to print() some of the steps
    print(decrypt)
    #hopefully...
    return decrypt

whatpimeans()
