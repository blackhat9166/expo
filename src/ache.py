import math

wv = float(input("sidways compopnent "))
wh = float(input("upsidedown component "))
v0 = float(input("muzzle velocity of the gun "))
angle = float(input("input the given inclination ang "))
u_angle = 0
g = 9.80665
R = float(input("given range of the target "))
while (u_angle < 80):

    
  
  v = float(v0*math.cos(math.radians(u_angle)))
  vv = float(v0*math.sin(math.radians(u_angle)))
  av = float(0.5*g*(math.sin(math.radians(angle))))
  a = float(0.5*g*(math.cos(math.radians(angle))))
  t =0
  dspl_v = 0
  if angle >= 0:
    d = (v*v)-(4*av*R)
    if d <= 0:
     print("bullet cant reach")
    else: 
      d = math.sqrt(d)
      t = (v-d)/(2*av)
      dspl_v = (vv*t)-(a*t*t)
  else:
    if (v != 0):
     d =  (v*v)+4*a*R
     d = math.sqrt(d)
     t = (-v+d)/(2*a)
     dspl_v = (vv*t)+(av*t*t)
    else:
     print("bullet cant reach")

  if angle >=0:
   yh = v - av*t
   yv = vv - av*t
  kill = math.sqrt(yh*yh + yv*yv)
  print(dspl_v)
  bull = -int(dspl_v)
  print(f"bullet reach at {t}")
  print(f"bullet speed at which target hit by {kill}")
  u_angle +=1



    
   