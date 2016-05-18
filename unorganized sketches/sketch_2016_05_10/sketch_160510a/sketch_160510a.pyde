# Rotating canvas, traces shapes in a 3D rotating environment

class Symbol():
    global positions
    positions = []
    
    def __init__(self,pos):
        self.pos = pos 
        self.xoff = 0.0
        
    def display(self):
        beginShape()
        stroke(255,10)
        strokeWeight(4)
        noFill()
        #fill(10,map(len(positions),0,100,100,20),map(len(positions),0,100,10,120),10)
        
        self.xoff +=0.01
        n = noise(self.xoff) * 300
        
        for l in positions :
            curveVertex(l.x,l.y,l.z)
            offset = PVector.random3D()
            offset.mult(0.5)
            l.add(offset)

        endShape()
    
        if len(positions) > 10:
            positions.pop(0)#int(random(len(positions)-1)))

        
        if(frameCount % 5 == 0):
            v1 = PVector.random3D().mult(200)
            
            println(frameCount)

    

            positions.append(v1)
        

        


rot = 0
offset = PVector(0,0,random(-0.5,0.5))
symbolcollection = []
desiredsymbols = 1


def setup():

    size(800,800,P3D)
    #smooth(8)
    background(5)

      
    
    for i in range(desiredsymbols):
        i = Symbol(PVector(width/2,height/2,0))
        symbolcollection.append(i) 




def draw():
    scale(0.5)
    global rot

    rot+=0.01
    
    #background(5)

  
    pushMatrix()
    translate(width/2,height/2)
    rotateY(rot)
    rotateX(rot)
    #rotateZ(rot)
    for Symbol in symbolcollection:

         #translate(Symbol.pos.x,Symbol.pos.y,Symbol.pos.z)
         Symbol.display()
    sphereDetail(int(random(3,4)))
    noFill()
    strokeWeight(1)
    sphere(300)  
    popMatrix()
    if(frameCount % 500 == 0):
        background(0)


        