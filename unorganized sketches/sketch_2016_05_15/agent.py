class Agent(object):
    
    def __init__(self,pos):
        self.pos = pos
        self.xoff = random(0,100)
        self.vel = PVector(8,0)
        self.outside = False
        self.modY = 0
        
    def run(self): 
        #self.display()
        self.update()
        self.wrap()
        
    def display(self):
        s = 2
        with pushMatrix():
            stroke(0,100)
            strokeWeight(1)
            point(self.pos.x,self.pos.y)
        
    def update(self):
        
        self.modY = map(noise(-self.xoff,self.xoff),0,1,-0.5,0.5)
    
        self.pos.add(self.vel)
        self.pos.y += self.modY
        self.xoff += 0.05
        
    
    def wrap(self):
        if(self.pos.x > width  or self.pos.x < 0):
            self.outside = True
        elif(self.pos.y > height or self.pos.y < 0):
            self.outside = True
            
        if(self.outside):
            self.pos = PVector(0,random(height),0)
            self.outside = False
            
            
        