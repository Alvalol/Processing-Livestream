add_library('video')
add_library('peasycam')

from agent import Agent
from agentGroup import AgentGroup
global sourceMovie


desiredAgents = 1
global agentGroup

def setup():

    global sourceMovie, agentGroup
    sourceMovie = Movie(this, "movie.mp4") # livestream?
    agentGroup = AgentGroup(sourceMovie)
    PeasyCam(this,100)
    
    sourceMovie.loop()
    sourceMovie.volume(0)
    
    for i in range(desiredAgents):
        agentGroup.addAgent(Agent())

    
    size(500,500,P3D)
    smooth(8)

    
    
def draw():
    background(0)
    scale(4)
    pushMatrix()
    #translate(-400,-350,-1000)
    agentGroup.run()
#    image(sourceMovie,0,0)
    popMatrix()
    print frameRate 

def movieEvent(source):
    sourceMovie.read()


def blender():
    blendMode(SUBTRACT)
    fill(10)
    noStroke()
    rect(0,0,width*2,height*2)
    blendMode(BLEND)
                    


    