from bird import Bird
from flock import Flock

flock = Flock()
desiredBirds = 20

def setup():
    size(500,500,P2D)
    noSmooth()
    #smooth()
    background(0)
    for i in range(desiredBirds):
        flock.addBird(Bird(random(width),random(height)))
        
    
def draw():
    #background(0)
    blender()
    flock.run()
 #   print(str(frameRate) + "FPS")

    
 

def mouseClicked():
        flock.addBird(Bird(mouseX,mouseY))
        
def keyPressed():
        m = Bird(mouseX,mouseY)
        m.leader = 100
        flock.addBird(m)
        
        
    
def blender():
      blendMode(SUBTRACT);
      fill(6);
      noStroke();
      rect(0, 0, width*2, height*2);
      blendMode(BLEND);