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

pygame.mouse.set_visible(False)
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
left = GPIO.PWM(6, (1000/(20+no_spin)))  
right = GPIO.PWM(5, (1000/(20+no_spin)))
left.start(0)
right.start(0)

duty_cycle_max_spd_cw=6.10
duty_cycle_max_spd_ccw=7.83
duty_cycle_slow_spd_cw=6.89
duty_cycle_slow_spd_ccw=7.06

duty_cycle_cw=duty_cycle_slow_spd_cw
duty_cycle_ccw=duty_cycle_slow_spd_ccw

command= " "

#command a motion
def status(c):
	global command
	command = c 
	if command == "forward":
		move_forward()
	elif command == "backward":
		move_backward()
	elif command == "left":
		turn_left()
	elif command == "right":
		turn_right()
	elif command == "stop":
		stop()
	elif command == "resume":
		resume ()
		
#resume function 
def resume ():
	global duty_cycle_cw
	global duty_cycle_ccw
	GPIO.setmode(GPIO.BCM)   
	GPIO.setup(6, GPIO.OUT)
	GPIO.setup(5, GPIO.OUT)
	left = GPIO.PWM(6, (1000/(20+no_spin)))  
	right = GPIO.PWM(5, (1000/(20+no_spin)))
	left.start(0)
	right.start(0)
	print 'Resume: left is %s, right is %s ' (duty_cycle_cw, duty_cycle_ccw)
			
#move the robot forward 
def forward():
	global duty_cycle_cw
	global duty_cycle_ccw
	left.ChangeFrequency(1000/(20+ccw))
	left.ChangeDutyCycle(duty_cycle_ccw)
	right.ChangeFrequency(1000/(20+cw))
	right.ChangeDutyCycle(duty_cycle_cw)
	command ="forward"
	print 'Forward: left is %s, right is %s ' (duty_cycle_cw, duty_cycle_ccw)
	return 
    
    
    
#stop the robot 
def stop():
	global duty_cycle_cw
	global duty_cycle_ccw
	left.ChangeDutyCycle(0.0)
	right.ChangeDutyCycle(0.0)
	command = " stop"
	print 'Stop: left is %s, right is %s ' (duty_cycle_cw, duty_cycle_ccw)
	return 
    
#move the robot backward 
def backward():
	global duty_cycle_cw
	global duty_cycle_ccw
	left.ChangeFrequency(1000/(20+cw))
	left.ChangeDutyCycle(duty_cycle_cw)
	right.ChangeFrequency(1000/(20+ccw))
	right.ChangeDutyCycle(duty_cycle_ccw)
	command ="backward"
	print 'Backward: left is %s, right is %s ' (duty_cycle_cw, duty_cycle_ccw)
	return 
      

#pivot left  
def left():
	global duty_cycle_cw
	global duty_cycle_ccw
	left.ChangeFrequency(1000/(20+cw))
	left.ChangeDutyCycle(duty_cycle_cw)
	right.ChangeFrequency(1000/(20+cw))
	right.ChangeDutyCycle(duty_cycle_cw)
	command ="L"
	print 'Pivot  left: left is %s, right is %s ' (duty_cycle_cw, duty_cycle_ccw)
	return 
       
#pivot right  
def right():
	global duty_cycle_cw
	global duty_cycle_ccw
	left.ChangeFrequency(1000/(20+ccw))
	left.ChangeDutyCycle(duty_cycle_ccw)
	right.ChangeFrequency(1000/(20+ccw))
	right.ChangeDutyCycle(duty_cycle_ccw)
	command ="R"
	print 'Pivot right: left is %s, right is %s ' (duty_cycle_cw, duty_cycle_ccw)
	return    


#function to quit 
def quit():
	global duty_cycle_cw
	global duty_cycle_ccw
	left.ChangeDutyCycle(0.0)
	right.ChangeDutyCycle(0.0)
	command = " quit"
	GPIO.cleanup()
	return 	

#function for speed control
def speed_control(command):
	global duty_cycle_max_spd_cw
	global duty_cycle_max_spd_ccw
	global duty_cycle_cw
	global duty_cycle_ccw
	
	
	

	if command == "up":
		if duty_cycle_cw==6.97:
			duty_cycle_cw=6.77
		if duty_cycle_ccw==6.97:
			duty_cycle_ccw=7.17
			
		if (duty_cycle_cw >6.97 and duty_cycle_cw <7.83):
			duty_cycle_cw +=0.2
		elif (duty_cycle_cw <6.97 and duty_cycle_cw >6.10):
			duty_cycle_cw -=0.2
			
		if (duty_cycle_ccw >6.97 and duty_cycle_ccw <7.83):
			duty_cycle_ccw +=0.2
		elif (duty_cycle_ccw <6.97 and duty_cycle_ccw >6.10):
			duty_cycle_cw -=0.2
		
		left.ChangeFrequency(1000/(20+ccw))
		left.ChangeDutyCycle(duty_cycle_ccw)
		right.ChangeFrequency(1000/(20+cw))
		right.ChangeDutyCycle(duty_cycle_cw)
		print 'Up: left is %s, right is %s ' (duty_cycle_cw, duty_cycle_ccw)
		return 
		 						
	if command == "down":
		if duty_cycle_cw==6.97:
			duty_cycle_cw=7.17
		if duty_cycle_ccw==6.97:
			duty_cycle_ccw=6.77
			
		if (duty_cycle_cw >6.97 and duty_cycle_cw <7.83):
			duty_cycle_cw -=0.2
		elif (duty_cycle_cw <6.97 and duty_cycle_cw >6.10):
			duty_cycle_cw +=0.2
			
		if (duty_cycle_ccw >6.97 and duty_cycle_ccw <7.83):
			duty_cycle_ccw -=0.2
		elif (duty_cycle_ccw <6.97 and duty_cycle_ccw >6.10):
			duty_cycle_cw +=0.2
		left.ChangeFrequency(1000/(20+ccw))
		left.ChangeDutyCycle(duty_cycle_ccw)
		right.ChangeFrequency(1000/(20+cw))
		right.ChangeDutyCycle(duty_cycle_cw)
		print 'Down: left is %s, right is %s ' (duty_cycle_cw, duty_cycle_ccw)
		return  						
						


def GPIO27_callback(channel):
  print "Button 27 has been pressed meaning Left servo clockwise" 
  left.ChangeFrequency(1000/(20+cw))
  left.ChangeDutyCycle(100*(cw/(20+cw)))

def GPIO23_callback(channel):
  print "Button 23 has been pressed meaning Left servo stopped"
  left.ChangeDutyCycle(0.0)
  

def GPIO22_callback(channel):
  print "Button 22 has been pressed meaning Left servo counter-clockwise"
  left.ChangeFrequency(1000/(20+ccw))
  left.ChangeDutyCycle(100*(ccw/(20+ccw)))

def GPIO26_callback(channel):
  print "Button 27 has been pressed meaning Right servo clockwise"
  right.ChangeFrequency(1000/(20+cw))
  right.ChangeDutyCycle(100*(cw/(20+cw)))


def GPIO19_callback(channel):
  print "Button 19  has been pressed meaning Right servo stopped"
  right.ChangeDutyCycle(0.0)
    

def GPIO17_callback(channel):
  print "Button 17 has been pressed meaning Right servo counter-clockwise"
  right.ChangeFrequency(1000/(20+ccw))
  right.ChangeDutyCycle(100*(ccw/(20+ccw)))


# " main" part of the program
GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=GPIO26_callback, bouncetime=300)
GPIO.add_event_detect(19, GPIO.FALLING, callback=GPIO19_callback, bouncetime=300)
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)

try:
  time.sleep(120) #quit when program after run for 2 minutes

except KeyboardInterrupt:
  GPIO.cleanup() # clean up GPIO on CTRL+C exit


GPIO.cleanup() # clean up GPIO on normal exit



