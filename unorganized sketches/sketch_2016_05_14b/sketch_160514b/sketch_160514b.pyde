from agent import Agent
from agentGroup import AgentGroup

add_library('peasycam')
agentGroup = AgentGroup()
agentMaximum = 200


agent = Agent(PVector(0,0,0))

def setup():
    background(0)
    size(500,500,P3D)
    smooth(8)
    PeasyCam(this,100)
    for i in range(agentMaximum):
        agentGroup.addAgent(Agent(PVector(random(width),random(height))))
    
    
    
def draw():
    background(0)
    agentGroup.run()
    print len(agentGroup.agentCollection)


         
        
    