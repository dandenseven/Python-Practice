
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

