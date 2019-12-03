import math

class Snake:
    def __init__(self,x,y,size,canvas):
        self.x=x
        self.y=y
        self.size=size
        self.canvas=canvas
        self.dir=-1
        self.snake=None
        self.body=[]
        self.createSnake()

    def createSnake(self):
        self.snake=self.canvas.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,fill='green')
        self.body.append(self.canvas.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,fill='green'))
        self.body.append(self.canvas.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,fill='green'))

    def update(self):
	
        x=self.canvas.coords(self.snake)[0]
        y=self.canvas.coords(self.snake)[1]
        x2=self.canvas.coords(self.snake)[2]
        y2=self.canvas.coords(self.snake)[3]

        if self.dir==0:
            self.y-=self.size
            self.canvas.coords(self.snake,self.x,self.y,self.x+self.size,self.y+self.size)
        elif self.dir==1:
            self.x+=self.size
            self.canvas.coords(self.snake,self.x,self.y,self.x+self.size,self.y+self.size)
        elif self.dir==2:
            self.y+=self.size
            self.canvas.coords(self.snake,self.x,self.y,self.x+self.size,self.y+self.size)
        elif self.dir==3:
            self.x-=self.size
            self.canvas.coords(self.snake,self.x,self.y,self.x+self.size,self.y+self.size)
        elif self.dir==-1:
            self.canvas.coords(self.snake,self.x,self.y,self.x+self.size,self.y+self.size)
        if len(self.body)>0:
            index=len(self.body)-1
            self.canvas.coords(self.body[index],x,y,x2,y2)
            self.body.insert(0, self.body.pop(index))

    def death(self):
        if self.x>800-self.size or self.x<0 or self.y>608-self.size or self.y<0:
            return True
        for i in range(2,len(self.body)):
            dist=math.sqrt((self.x-self.canvas.coords(self.body[i])[0])**2+(self.y-self.canvas.coords(self.body[i])[1])**2)
            if dist <15:
                return True
        return False

    def clear(self):
        for i in range(len(self.body)):
            self.canvas.delete(self.body[i])   

    def ateFood(self,food):
        dist=math.sqrt((self.x-self.canvas.coords(food)[0])**2+(self.y-self.canvas.coords(food)[1])**2)
        if dist<16:
            self.body.append(self.canvas.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,fill='green'))
            return True
        return False