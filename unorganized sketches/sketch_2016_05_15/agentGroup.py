class AgentGroup():
    
    def __init__(self):
        self.group = []
        self.coordList = []
        
        
    def run(self):
        self.otherAgent()
        for agent in self.group:
            agent.run()
        #print("Group size : " +str(len(self.group)))
        
        #self.cleanup - possibly?
    
        
    def addAgent(self, agent):
        self.group.append(agent)
        
        
    def otherAgent(self):
        self.coordList = []
        
        for i, agent in enumerate(self.group):
            otheragent = self.group[i-1]
            distance = floor(dist(agent.pos.x,agent.pos.y,otheragent.pos.x,otheragent.pos.y))

            if distance < 10:
                for x in (agent.pos.x,otheragent.pos.x):
                    for y in (agent.pos.y,otheragent.pos.y):
                        self.coordList.append((floor(x),floor(y)))
            
            
        

                        
                
               #stroke(0,100)
               #fill(0,100)
               #curveVertex(agent.pos.x,agent.pos.y)
               #curveVertex(otheragent.pos.x,otheragent.pos.y)
                        #line(agent.pos.x,agent.pos.y,otheragent.pos.x,otheragent.pos.y)
               #endShape()
                


            
        