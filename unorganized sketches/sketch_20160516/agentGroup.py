class AgentGroup():
    
    def __init__(self,sourceMovie):
        self.group = []
        self.pixelcollection = []
        self.sourceMovie = sourceMovie
        
        
    def run(self):
        for agent in self.group:
            agent.run()  

        #self.fetchPixels(self.sourceMovie)
        self.setAgentPos()
    
        
    def addAgent(self, agent):
        self.group.append(agent)

        
    def setAgentPos(self):
        pixelcollection = self.fetchPixels(self.sourceMovie)
        self.pixelcollection = []

        beginShape()
        for agent in self.group:   
            for PVcoords in pixelcollection:
                agent.pos = PVcoords[0]
                agent.col = PVcoords[1]
                agent.run()
        endShape()
              
    def fetchPixels(self, sourceMovie):
        global desiredAgents
        sourceMovie.loadPixels()
        skip = 16
        minBright = 0
        maxBright = 255
        minDepth = 0
        maxDepth = 400


         
         # changed to make it more interesting?
        for x in range(0,sourceMovie.width,skip):
            for y in range(0,sourceMovie.height,skip):
                loc = x + y * sourceMovie.width
                if (brightness(sourceMovie.pixels[loc]) > 1):
                    newpos = PVector(x,y,map(brightness(sourceMovie.pixels[loc]),minBright,maxBright, minDepth,maxDepth))
                    newcol = color(sourceMovie.pixels[loc])
                    self.pixelcollection.append([newpos,newcol])
        return self.pixelcollection



                   

            
        

                        
            
                


            
        