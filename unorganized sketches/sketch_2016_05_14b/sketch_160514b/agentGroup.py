class AgentGroup(object):
    
    def __init__(self):
        self.agentCollection = []
        
    def run(self):
        for b in self.agentCollection:
            b.run()

            
    def addAgent(self,b):
        self.agentCollection.append(b)
    