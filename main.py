from tkinter import Tk, Canvas, Label
from pynput.keyboard import Listener
from snake import Snake
import threading
import random
import time
import os

width=800
height=608

dead = False

gui=Tk()
gui.geometry(str(width)+"x"+str(height+105))
gui.resizable(0,0)
gui.title("Snake")
score= Label(master=gui, text="0",font=("Impact", 64))
score.pack()
canvas=Canvas(master=gui,width=width,height=height,background="black")
canvas.pack()

snake=Snake(width/2,height/2,16,canvas)
food=canvas.create_oval(-16,-16,-16+snake.size,-16+snake.size,fill='red')


def onPress(key):
	global dead

	letter = str(key).replace("'","")

	if letter=='w' or letter=="Key.up":
		if snake.dir==2:
			dead=True
		snake.dir=0
	elif letter=='d' or letter=="Key.right":
		if snake.dir==3:
			dead=True
		snake.dir=1
	elif letter=='s' or letter=="Key.down":
		if snake.dir==0:
			dead=True
		snake.dir=2
	elif letter=='a' or letter=="Key.left":
		if snake.dir==1:
			dead=True
		snake.dir=3
	elif letter=='p':
		os._exit(0)

def listening():
	with Listener(on_press=onPress) as listener:
		listener.join()

def retry():
	createFood()
	snake.dir=-1
	snake.x=width/2
	snake.y=height/2
	snake.clear()
	snake.body=[]
	snake.body.append(snake.canvas.create_rectangle(snake.x,snake.y,snake.x+snake.size,snake.y+snake.size,fill='green'))
	snake.body.append(snake.canvas.create_rectangle(snake.x,snake.y,snake.x+snake.size,snake.y+snake.size,fill='green'))

def createFood():
	x=random.randint(0,width-snake.size)
	y=random.randint(0,height-snake.size)
	x-=(x%16)
	y-=(y%16)
	canvas.coords(food,x,y,x+snake.size,y+snake.size)

def main():
	global dead

	threading.Thread(target=listening).start()

	createFood()

	while 1:
		if snake.death() or dead:
			retry()
			dead=False
		if(snake.ateFood(food)):
			createFood()
		if snake.dir!=-1:
			score.config(text=str(len(snake.body)-2))
		snake.update()
		gui.update()
		time.sleep(0.035)

if __name__ == "__main__":
	main()