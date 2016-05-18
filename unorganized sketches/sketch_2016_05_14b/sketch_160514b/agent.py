class Agent(object):
    
    def __init__(self, pos):

        self.pos = pos
        self.xoff = random(1000)
        self.noiseValue = noise(self.xoff,self.xoff)
        self.angle = random(TWO_PI)
        self.speed = PVector(cos(self.angle),sin(self.angle),tan(self.angle))
        self.outside = False

        
        
    def run(self):
        self.display()
        self.move()
        self.wrap()
        
    def display(self):
        strokeWeight(map(self.speed.y,-1,1,.1,1))
        #noStroke()
        stroke(255,map(self.speed.x,-1,1,50,150))
        pushMatrix()
        translate(self.pos.x,self.pos.y,self.pos.z)
        rotate(sin(self.xoff))
        #noFill()
        noFill()
        box(40)
        popMatrix()
        
    def move(self):
        self.xoff +=0.02
        self.noiseValue = noise(-self.xoff,self.xoff)
        self.angle = map((TWO_PI * self.noiseValue),0,4,-0.5,0.5)  * TWO_PI / 10
        self.speed = PVector(cos(self.angle),sin(self.angle),cos(self.angle)*10)
        self.pos.add(self.speed)

        
    
    
    def wrap(self):
        if(self.pos.x > width  or self.pos.x < 0):
            self.outside = True
        elif(self.pos.y > height or self.pos.y < 0):
            self.outside = True
            
        if(self.outside):
            self.pos = PVector(random(width),random(height),0)
            self.outside = False
        
        
        