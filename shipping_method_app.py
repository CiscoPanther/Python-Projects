"""
Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal's Shippers.
Sal's Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren't charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
"""
def ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <=6:
   price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
   price_per_pound = 4.75

  return 20 + (price_per_pound * weight)
#Testing the function
print(ground_shipping(8.4))

premium_ground = 125.00

def drone_shipping(weight):
  if weight <= 2:
  	price_per_pound = 4.50
  elif weight <= 6:
   	price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
   price_per_pound = 14.25

  return (price_per_pound * weight)


#Testing the drone shipping cost
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = premium_ground
  drone = drone_shipping(weight)

  if ground < premium and ground < drone:
    method = "Standard ground"
    cost = ground

  elif premium < ground and premium < drone:
    method = "Premium"
    cost = premium
  else:
    method = "Drone!"
    cost = drone

  print("The shipping method that is the cheapest is %s and the cost is $%.2f"
       % (method, cost)
       )
#Testing the function
item_weight = input("Enter the weight of the item: ")
item_weight = float(item_weight)
print(cheapest_shipping(item_weight))

