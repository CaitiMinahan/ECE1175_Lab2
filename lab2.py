from sense_hat import SenseHat
import time
#subtask 1
# sense = SenseHat()
# i=1
# while i==1:
#     sense.show_message("Hello my name is Pepe")

#subtask 2
# sense = SenseHat()
# while True:
#     for event in sense.stick.get_events():
#         #print(event.direction, event.action)
#         if((event.direction == "left") and (event.action == "released")):
#             acceleration = sense.get_accelerometer_raw()
#             
#             x = acceleration['x']
#             y = acceleration['y']
#             z = acceleration['z']
#             
#             x = round(x,1)
#             y = round(y,1)
#             z = round(z, 1)
#             
#             print("x={0}, y={1}, z={2}".format(x,y,z))
#         elif((event.direction == "right") and (event.action == "released")):
#             t = sense.get_temperature()
#             t = round(t,1)
#             msg = "Temperature = {0}".format(t)
#             sense.show_message(msg, scroll_speed=0.05)
#         elif((event.direction == "down") and (event.action == "released")):
#             p = sense.get_pressure()
#             p = round(p,1)
#             msg = "Pressure = {0}".format(p)
#             sense.show_message(msg, scroll_speed=0.05)
#         elif((event.direction == "up") and (event.action == "released")):
#             h = sense.get_humidity()
#             h = round(h,1)
#             msg = "Humidity = {0}".format(h)
#             sense.show_message(msg, scroll_speed=0.05)
#         elif((event.direction == "middle") and (even
#             t.action == "released")):
#             orientation = sense.get_orientation()
#             
#             pitch = orientation['pitch']
#             roll = orientation['roll']
#             yaw = orientation['yaw']
#             
#             print("pitch={0}, roll={1}, yaw={2}".format(pitch,yaw,roll))
#subtask 3
# sense = SenseHat()
# red = (255, 0, 0)
# blue = (0, 0, 255)
# green = (0, 255, 0)
# black = (0, 0, 0)
# white = (255, 255, 255)
# yellow = (255, 255, 0)
# indigo = (75, 0, 130)
# orange = (255, 127, 0)
# 
# countXR = 0
# countXL = 0
# countYD = 0
# countYU = 0
# 
# while True:
#         acceleration = sense.get_accelerometer_raw()
#         orientation = sense.get_orientation()
#         
#         sense.clear()
#             
#         x = acceleration['x']
#         y = acceleration['y']
#         z = acceleration['z']
#             
#         x = round(x,1)
#         y = round(y,1)
#         z = round(z,1)
#         
#         pitch = orientation['pitch']
#         roll = orientation['roll']
#         yaw = orientation['yaw']
#         
#         #test for each value of the x,y,z orientation:
#         
#         #assume we only care when the board is facing upwards
#         if z>0:
#             #test for x-axis orientation
#             if(abs(x)>abs(y)):
#                 #test for x>0 (when board is tilted to the left)
#                 if x>0:
#                   countXR = 0
#                   countYD = 0
#                   countYU = 0
#                   #test for col 0
#                   if countXL==0:
#                       for i in range(8):
#                           sense.set_pixel(0, i, red)
#                       countXL = 1; #move onto the next column
#                   #test for col 1:
#                   elif countXL==1:
#                       for i in range(8):
#                           sense.set_pixel(1, i, blue)
#                       countXL = 2; #move onto the next column
#                   #test for col 2:
#                   elif countXL==2:
#                       for i in range(8):
#                           sense.set_pixel(2, i, green)
#                       countXL = 3; #move onto the next column   
#                  #test for col 3:
#                   elif countXL==3:
#                       for i in range(8):
#                           sense.set_pixel(3, i, black)
#                       countXL = 4; #move onto the next column     
#                  #test for col 4:
#                   elif countXL==4:
#                       for i in range(8):
#                           sense.set_pixel(4, i, white)
#                       countXL = 5; #move onto the next column     
#                  #test for col 5:
#                   elif countXL==5:
#                       for i in range(8):
#                           sense.set_pixel(5, i, yellow)
#                       countXL = 6; #move onto the next column     
#                  #test for col 6:
#                   elif countXL==6:
#                       for i in range(8):
#                           sense.set_pixel(6, i, indigo)
#                       countXL = 7; #move onto the next column     
#                  #test for col 7:
#                   elif countXL==7:
#                       for i in range(8):
#                           sense.set_pixel(7, i, orange)
#                       countXL = 0; #go back to beginning
#                       
#                 #test for x<0 (when the board is tilted to the right)
#                 elif x<0:
#                   countXL = 0
#                   countYD = 0
#                   countYU = 0
#                   #test for col 7
#                   if countXR==0:
#                       for i in range(8):
#                           sense.set_pixel(7, i, red)
#                       countXR = 1; #move onto the next column
#                   #test for col 6:
#                   elif countXR==1:
#                       for i in range(8):
#                           sense.set_pixel(6, i, blue)
#                       countXR = 2; #move onto the next column
#                   #test for col 5:
#                   elif countXR==2:
#                       for i in range(8):
#                           sense.set_pixel(5, i, green)
#                       countXR = 3; #move onto the next column   
#                  #test for col 4:
#                   elif countXR==3:
#                       for i in range(8):
#                           sense.set_pixel(4, i, black)
#                       countXR = 4; #move onto the next column     
#                  #test for col 3:
#                   elif countXR==4:
#                       for i in range(8):
#                           sense.set_pixel(3, i, white)
#                       countXR = 5; #move onto the next column     
#                  #test for col 2:
#                   elif countXR==5:
#                       for i in range(8):
#                           sense.set_pixel(2, i, yellow)
#                       countXR = 6; #move onto the next column     
#                  #test for col 1:
#                   elif countXR==6:
#                       for i in range(8):
#                           sense.set_pixel(1, i, indigo)
#                       countXR = 7; #move onto the next column     
#                  #test for col 0:
#                   elif countXR==7:
#                       for i in range(8):
#                           sense.set_pixel(0, i, orange)
#                       countXR = 0; #go back to beginning
#                           
#             #test for y-axis orientation
#             else:
#                 #test for y>0 (when board is tilted upwards)
#                 if y>0:
#                   countXR = 0
#                   countXL = 0
#                   countYD = 0
#                   #test for col 0
#                   if countYU==0:
#                       for i in range(8):
#                           sense.set_pixel(i, 0, red)
#                       countYU = 1; #move onto the next column
#                   #test for col 1:
#                   elif countYU==1:
#                       for i in range(8):
#                           sense.set_pixel(i, 1, blue)
#                       countYU = 2; #move onto the next column
#                   #test for col 2:
#                   elif countYU==2:
#                       for i in range(8):
#                           sense.set_pixel(i, 2, green)
#                       countYU = 3; #move onto the next column   
#                  #test for col 3:
#                   elif countYU==3:
#                       for i in range(8):
#                           sense.set_pixel(i, 3, black)
#                       countYU = 4; #move onto the next column     
#                  #test for col 4:
#                   elif countYU==4:
#                       for i in range(8):
#                           sense.set_pixel(i, 4, white)
#                       countYU = 5; #move onto the next column     
#                  #test for col 5:
#                   elif countYU==5:
#                       for i in range(8):
#                           sense.set_pixel(i, 5, yellow)
#                       countYU = 6; #move onto the next column     
#                  #test for col 6:
#                   elif countYU==6:
#                       for i in range(8):
#                           sense.set_pixel(i, 6, indigo)
#                       countYU = 7; #move onto the next column     
#                  #test for col 7:
#                   elif countYU==7:
#                       for i in range(8):
#                           sense.set_pixel(i, 7, orange)
#                       countYU = 0; #go back to beginning
#                       
#                 #test for y<0 (when the board is tilted downwards)
#                 if y<0:
#                   countXR = 0
#                   countXL = 0
#                   countYU = 0
#                   #test for col 0
#                   if countYD==0:
#                       for i in range(8):
#                           sense.set_pixel(i, 7, red)
#                       countYD = 1; #move onto the next column
#                   #test for col 1:
#                   elif countYD==1:
#                       for i in range(8):
#                           sense.set_pixel(i, 6, blue)
#                       countYD = 2; #move onto the next column
#                   #test for col 2:
#                   elif countYD==2:
#                       for i in range(8):
#                           sense.set_pixel(i, 5, green)
#                       countYD = 3; #move onto the next column   
#                  #test for col 3:
#                   elif countYD==3:
#                       for i in range(8):
#                           sense.set_pixel(i, 4, black)
#                       countYD = 4; #move onto the next column     
#                  #test for col 4:
#                   elif countYD==4:
#                       for i in range(8):
#                           sense.set_pixel(i, 3, white)
#                       countYD = 5; #move onto the next column     
#                  #test for col 5:
#                   elif countYD==5:
#                       for i in range(8):
#                           sense.set_pixel(i, 2, yellow)
#                       countYD = 6; #move onto the next column     
#                  #test for col 6:
#                   elif countYD==6:
#                       for i in range(8):
#                           sense.set_pixel(i, 1, indigo)
#                       countYD = 7; #move onto the next column     
#                  #test for col 7:
#                   elif countYD==7:
#                       for i in range(8):
#                           sense.set_pixel(i, 0, orange)
#                       countYD = 0; #go back to beginning      
# 
#                 
#         #else statement for when z<0
#         else: 
#             #remember, we don't care when the board is facing down (hence, when z is negatiev)
#             print("pi facing down with x={0}, y={1}, z={2}".format(x,y,z))
            
#subtask 4:
sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
indigo = (75, 0, 130)
orange = (255, 127, 0)
while True:
    sense.set_pixel(0, 0, red)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(0, 1, blue)
    sense.set_pixel(1, 0, blue)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(0, 2, green)
    sense.set_pixel(2, 0, green)
    sense.set_pixel(1, 1, green)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(0, 3, red)
    sense.set_pixel(2, 1, red)
    sense.set_pixel(1, 2, red)
    sense.set_pixel(3, 0, red)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(0, 4, white)
    sense.set_pixel(3, 1, white)
    sense.set_pixel(2, 2, white)
    sense.set_pixel(1, 3, white)
    sense.set_pixel(4, 0, white)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(0, 5, yellow)
    sense.set_pixel(4, 1, yellow)
    sense.set_pixel(3, 2, yellow)
    sense.set_pixel(2, 3, yellow)
    sense.set_pixel(1, 4, yellow)
    sense.set_pixel(5, 0, yellow)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(0, 6, indigo)
    sense.set_pixel(1, 5, indigo)
    sense.set_pixel(2, 4, indigo)
    sense.set_pixel(3, 3, indigo)
    sense.set_pixel(4, 2, indigo)
    sense.set_pixel(5, 1, indigo)
    sense.set_pixel(6, 0, indigo)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(0, 7, orange)
    sense.set_pixel(1, 6, orange)
    sense.set_pixel(2, 5, orange)
    sense.set_pixel(3, 4, orange)
    sense.set_pixel(4, 3, orange)
    sense.set_pixel(5, 2, orange)
    sense.set_pixel(6, 1, orange)
    sense.set_pixel(7, 0, orange)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(1, 7, indigo)
    sense.set_pixel(2, 6, indigo)
    sense.set_pixel(3, 5, indigo)
    sense.set_pixel(4, 4, indigo)
    sense.set_pixel(5, 3, indigo)
    sense.set_pixel(6, 2, indigo)
    sense.set_pixel(7, 1, indigo)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(2, 7, yellow)
    sense.set_pixel(3, 6, yellow)
    sense.set_pixel(4, 5, yellow)
    sense.set_pixel(5, 4, yellow)
    sense.set_pixel(6, 3, yellow)
    sense.set_pixel(7, 2, yellow)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(3, 7, white)
    sense.set_pixel(4, 6, white)
    sense.set_pixel(5, 5, white)
    sense.set_pixel(6, 4, white)
    sense.set_pixel(7, 3, white)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(4, 7, red)
    sense.set_pixel(5, 6, red)
    sense.set_pixel(6, 5, red)
    sense.set_pixel(7, 4, red)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(5, 7, green)
    sense.set_pixel(6, 6, green)
    sense.set_pixel(7, 5, green)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(6, 7, blue)
    sense.set_pixel(7, 6, blue)
    time.sleep(1)
    sense.clear()
    sense.set_pixel(7, 7, red)
    time.sleep(1)
    sense.clear()