#!/usr/bin/env python
#ECE5725 Project
#Fall 2017
#Author: Francois Mertil
#NetID: fjm83



import RPi.GPIO as GPIO
import time,sys,os,pygame
from pygame.locals import*





os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()

current_time = time.time()

#pygame.mouse.set_visible(True)
GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
cw = 1.3
ccw = 1.7
no_spin = 1.5
left_servo = GPIO.PWM(6, 46.5)  
right_servo = GPIO.PWM(5, 46.5)
left_servo.start(0)
right_servo.start(0)
left_duty_cycle=7.0
right_duty_cycle=7.0

command= " "

#command a motion
def status(c):
	global command 
	command = c
	if command == "forward":
		forward()
	elif command == "backward":
		backward()
	elif command == "left":
		left()
	elif command == "right":
		right()
	elif command == "stop":
		stop()
	elif command == "start":
		start()
	elif command == "up":
		up()
	elif command == "down":
		down()
	elif command == "quit":
		quit()
		
		
		
#start function 
def start():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(6, GPIO.OUT)
	GPIO.setup(5, GPIO.OUT)
	left_servo = GPIO.PWM(6, 46.5)
	right_servo = GPIO.PWM(5, 46.5)
	left_servo.start(0)
	right_servo.start(0)
	command="start"
	print "start: left is %s, right is %s " % (left_duty_cycle, right_duty_cycle)
	return	
	
		
#move the robot forward 
def forward():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	left_duty_cycle=6.7
	right_duty_cycle=7.3
	left_servo.ChangeFrequency(50-0.5*left_duty_cycle)
	left_servo.ChangeDutyCycle(left_duty_cycle)
	right_servo.ChangeFrequency(50-0.5*right_duty_cycle)
	right_servo.ChangeDutyCycle(right_duty_cycle)
	command ="forward"
	print "Forward: left is %s, right is %s " % (left_duty_cycle, right_duty_cycle)
	return 
    
    
    
#stop the robot 
def stop():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	left_servo.ChangeDutyCycle(0.0)
	right_servo.ChangeDutyCycle(0.0)
	command = "stop"
	print "Stop: left is %s, right is %s " % (left_duty_cycle, right_duty_cycle)
    
#move the robot backward 
def backward():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	left_duty_cycle=7.3
	right_duty_cycle=6.7
	left_servo.ChangeFrequency(50-0.5*left_duty_cycle)
	left_servo.ChangeDutyCycle(left_duty_cycle)
	right_servo.ChangeFrequency(50-0.5*right_duty_cycle)
	right_servo.ChangeDutyCycle(right_duty_cycle)
	command ="backward"
	print "Backward: left is %s, right is %s " % (right_duty_cycle, left_duty_cycle)
	return 
      

#pivot left  
def left():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	left_duty_cycle=6.7
	right_duty_cycle=6.7
	left_servo.ChangeFrequency(50-0.5*left_duty_cycle)
	left_servo.ChangeDutyCycle(left_duty_cycle)
	right_servo.ChangeFrequency(50-0.5*right_duty_cycle)
	right_servo.ChangeDutyCycle(right_duty_cycle)
	command ="left"
	print "Pivot  left: left is %s, right is %s " % (right_duty_cycle, left_duty_cycle)
	return 
       
#pivot right  
def right():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	left_duty_cycle=7.3
	right_duty_cycle=7.3
	left_servo.ChangeFrequency(50-0.5*left_duty_cycle)
	left_servo.ChangeDutyCycle(left_duty_cycle)
	right_servo.ChangeFrequency(50-0.5*right_duty_cycle)
	right_servo.ChangeDutyCycle(right_duty_cycle)
	command ="right"
	print "Pivot  right: left is %s, right is %s " % (right_duty_cycle, left_duty_cycle)
	return    


#function to quit 
def quit():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(6, GPIO.OUT)
	GPIO.setup(5, GPIO.OUT)
	left_servo = GPIO.PWM(6, 46.5)
	right_servo = GPIO.PWM(5, 46.5)
	left_servo.start(0)
	right_servo.start(0)
	command ="quit"
	print "quit: left is %s, right is %s " % (right_duty_cycle, left_duty_cycle)
	GPIO.cleanup()
	return 	

#function for speed control
def up():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	if right_duty_cycle==7.0:
		right_duty_cycle=6.9
		
	if left_duty_cycle==7.0:
		left_duty_cycle=7.1
		
	if (right_duty_cycle >7.0 and right_duty_cycle <8.0):
		right_duty_cycle +=0.1
		
	elif (right_duty_cycle <7.0 and right_duty_cycle >6.0):
		right_duty_cycle -=0.1
		
	if (left_duty_cycle >7.0 and left_duty_cycle <8.0):
		left_duty_cycle +=0.1
	elif (left_duty_cycle <7.0 and left_duty_cycle >6.0):
		left_duty_cycle -=0.1
	
	left_servo.ChangeFrequency(50-0.5*left_duty_cycle)
	left_servo.ChangeDutyCycle(left_duty_cycle)
	right_servo.ChangeFrequency(50-0.5*right_duty_cycle)
	right_servo.ChangeDutyCycle(right_duty_cycle)
	command= "up"
	print 'Up: left is %s, right is %s ' % (left_duty_cycle, right_duty_cycle)
	return 
	
def down():
	global right_duty_cycle
	global left_duty_cycle
	global left_servo
	global right_servo
	if right_duty_cycle==7.0:
		right_duty_cycle=6.9
	if left_duty_cycle==7.0:
		left_duty_cycle=7.1
		
	if (right_duty_cycle >7.0 and right_duty_cycle <8.0):
		right_duty_cycle -=0.1
	elif (right_duty_cycle <7.0 and right_duty_cycle >6.0):
		right_duty_cycle +=0.1
		
	if (left_duty_cycle >7.0 and left_duty_cycle <8.0):
		left_duty_cycle -=0.1
	elif (left_duty_cycle <7 and left_duty_cycle >6.0):
		right_duty_cycle +=0.1
	left_servo.ChangeFrequency(50-0.5*left_duty_cycle)
	left_servo.ChangeDutyCycle(left_duty_cycle)
	right_servo.ChangeFrequency(50-0.5*right_duty_cycle)
	right_servo.ChangeDutyCycle(right_duty_cycle)
	command= "down"
	print 'Down: left is %s, right is %s ' % (left_duty_cycle, right_duty_cycle)
	return  						
					


def GPIO27_callback(channel):
  print "Button 27 has been pressed meaning Left servo clockwise" 
  left_servo.ChangeFrequency(1000/(20+cw))
  left_servo.ChangeDutyCycle(100*(cw/(20+cw)))

def GPIO23_callback(channel):
  print "Button 23 has been pressed meaning Left servo stopped"
  left_servo.ChangeDutyCycle(0.0)
  

def GPIO22_callback(channel):
  print "Button 22 has been pressed meaning Left servo counter-clockwise"
  left_servo.ChangeFrequency(1000/(20+ccw))
  left_servo.ChangeDutyCycle(100*(ccw/(20+ccw)))

def GPIO26_callback(channel):
  print "Button 27 has been pressed meaning Right servo clockwise"
  right_servo.ChangeFrequency(1000/(20+cw))
  right_servo.ChangeDutyCycle(100*(cw/(20+cw)))


def GPIO19_callback(channel):
  print "Button 19  has been pressed meaning Right servo stopped"
  right_servo.ChangeDutyCycle(0.0)
    

def GPIO17_callback(channel):
  print "Button 17 has been pressed meaning Right servo counter-clockwise"
  right_servo.ChangeFrequency(1000/(20+ccw))
  right_servo.ChangeDutyCycle(100*(ccw/(20+ccw)))


# " main" part of the program
GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=GPIO26_callback, bouncetime=300)
GPIO.add_event_detect(19, GPIO.FALLING, callback=GPIO19_callback, bouncetime=300)
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)
"""
try:
	time.sleep(1200) #quit when program after run for 2 minutes

except KeyboardInterrupt:
  GPIO.cleanup() # clean up GPIO on CTRL+C exit
"""

GPIO.cleanup() # clean up GPIO on normal exit


