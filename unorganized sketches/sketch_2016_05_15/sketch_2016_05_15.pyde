##Horrible Bill Gates Sketch

from agent import Agent
from agentGroup import AgentGroup

agentGroup = AgentGroup()
desiredAgents = 400

def setup():
    global img
    size(500,500,P3D)
    img = loadImage("image.jpg")
    rotate(TWO_PI/3)
    background("#FFFCF2")
    smooth(8)
    for i in range(desiredAgents):
        agentGroup.addAgent(Agent(PVector(0,random(height))))
    
def draw():
    agentGroup.run()
    blender()
    fetchPixels()
    
    
    
    
    
def frameRateCheck():
    if frameRate < 30:
        print("!!!! FRAMERATE LOWER THAN 30!!!!" + str(frameCount) + " FPS : " +  str(frameRate))
        
        
def  blender():
      blendMode(SUBTRACT);
      fill(0)
      noStroke();
      rect(0, 0, width*2, height*2);
      blendMode(BLEND);
      
def fetchPixels():
    global img
    img.loadPixels()
    skip = 8

    
    for x in range(0,img.width,skip):
        for y in range(0,img.height,skip):
            loc = x + y * img.width
            if (x, y) in agentGroup.coordList:
                fill(brightness(img.pixels[loc]))
                noStroke()
                translate(x,y,0)
                box(8,8,100)
            