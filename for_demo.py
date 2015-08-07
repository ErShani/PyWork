"""
for j in range(31,50):
    if j >= 31 and j <= 35:
          print("Sunny Day")
    elif j>=36 and j<=40:
          print("Warm Day")
    else:
          print("High Tempreture")
    
"""

temp = eval(input("Enter Tempreture: "))
if temp>30 and temp<35:
        print("Sunny Day")
elif temp>35 and temp<40:
        print("Warm Day")
elif temp>40 and temp<50:
        print("High Tempreture")
elif temp>50:
        print("Ghare Vaya Jaav Nakar Bali jase tamari.....   Chaamdi")
        
