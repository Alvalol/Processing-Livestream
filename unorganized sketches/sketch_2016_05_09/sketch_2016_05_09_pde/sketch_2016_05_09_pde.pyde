global col1,col2,col3
col1 = random(255)
col2 = random(255)
col3 = random(255)

class Symbol():
    
    def __init__(self, xpos, ypos, rad):
        self.xpos = xpos
        self.ypos = ypos
        self.rad = rad
        self.xoff = 0.0
        self.incr = 0    
        self.incmod = 10
        self.rot = 0

            
    def display(self):
        self.xoff +=random(.01,.02)
        n = noise(self.xoff) * self.rad 

        #translate(self.xpos,self.ypos,0)
        #box(100,100,n)

        #display rect
        fill(map(self.xpos,0,width,col1,col2),self.incr/5,self.incr,10)
        rectMode(CENTER)
        strokeWeight(10)
        stroke(self.incr/2,self.incr,self.incr,20)
        stroke(map(self.xpos,0,width,col1,col2),self.incr/5,self.incr,10)
        translate(self.xpos,self.ypos,0)
        #rectmode visuals
        rect(self.xpos,self.ypos,50,-50-n)
        
        
        if(mousePressed):
            self.xoff +=0.02
        
        if self.incr > 255 or self.incr <0:
            self.incmod*=-1
        self.incr+=self.incmod            
             
                   
    def update(self): 
        pushMatrix()
        translate(width/2,height/2)
        rotateY(self.rot/20)
        rotateX(self.rot/10)
        rotateZ(self.rot/15)
#        rotateX(self.incr/100)
#        rotateZ(self.incr/100)
        self.display()
        popMatrix()
    
        rot = map(self.rot,0,100,0,PI)
        self.rot+=0.2



SymbolList = []
desiredSymbols = 5
global rot
rot = 0

def setup():
    size(600,600,P3D)
    smooth(0)
    scale(0.1)
    #PeasyCam(this,100)

    
    background(0)
    posx = 10
    posy = 0
    for i in range(desiredSymbols):

        newSymbol = Symbol(posx,posy,height)
        SymbolList.append(newSymbol)
        if posx <= width:
             #rectmode
             #posx+=2
             #box mode
             posx+=10
        
    
    
def draw():
        #background(0)
    
    for Symbol in SymbolList:
        Symbol.update()
    if(mousePressed):
        del SymbolList[:]
        saveFrame("export-####.png")
        exit()