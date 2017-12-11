# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import loader
from .models import *
from servo1 import *


import subprocess
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template import context 
import pygame, time
pygame.mixer.init()
#import psutil
# Create your views here
#setup= True


def index(request):
	template=loader.get_template('main_app/index.html')
	#print "message is %s" %(message)
	context={}
	return HttpResponse(template.render(context, request))
	
#PROCNAME= 'video.py'
#subprocess.Popen("sudo python main_app/video.py", shell=True)

def motor (request):
	#global setup_0
	
	
	#
	#return HttpResponse('<h1>Bonjour</h1>')
	template=loader.get_template('main_app/motor.html')
	print "?????"
	#posts = Post.objects.filter(title__contains='Django').order_by('title')
	
	while True:
		message = ''
		print "here"
		if 'command' in request.GET and request.GET['command']:
			command = request.GET['command']
			
			if command == 'forward':
				print "======in forward======"
				message = "get button forward"
				status('forward')
			
			if command == 'backward':
				print "======in backward======" 
				message = "get button backward"
				status('backward')
				
			if command == 'stop': 
				print "======in stop======"
				message = "get button stop"
				status('stop')
				
			if command == 'quit': 
				print "======in quit======"
				message = "get button quit"
				status('quit')
			
			if command == 'start': 
				print "======start======"
				message = "get button start"
				status('start')
			
			if command == 'up': 
				print "======in up======"
				message = "get button speed up"
				status('up')
			
			if command == 'down': 
				print "======in down======"
				message = "get button speed down"
				status('down')
			
			if command == 'left':
				message = "get button left"
				status('left')
				
			if command == 'right': 
				message = "get button right"
				status('right')
		
			if command == 'record':
				camera.record()
			
			if command == 'stop_record':
				camera.stop()
			
			
		
			
				
		#subprocess.Popen("sudo python main_app/servo1.py", shell=True)
		
		context={'message':message}
		
		print "message is %s" %(message)
		return HttpResponse(template.render(context, request))
		


def voice(request):
	template=loader.get_template('main_app/voice.html')
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		s=pygame.mixer.Sound('/home/pi/finalproject'+uploaded_file_url)
		s.play(loops=1)
		time.sleep(3)
		return render(request, 'main_app/voice.html', {
			'uploaded_file_url': uploaded_file_url
		})
		
        #return render(request, 'main_app/temperature')
	context ={}
	return HttpResponse(template.render(context, request))
			


