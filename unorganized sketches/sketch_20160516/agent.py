class Agent(object):
    
    def __init__(self):
        self.pos = PVector()
        self.col = color(0)
        self.xoff = 0.0

    
    def run(self):

        self.display()


        
    def display(self):
        fill(self.col,255)

    
        #self.update()
        noStroke()
        pushMatrix()
        translate(self.pos.x,self.pos.y,self.pos.z)
        box(16)
        popMatrix()



        
    def update(self):
        mapper = 0.4
        mnoise = noise(self.xoff,self.xoff)
        noiseDetail(int(mnoise)*8,int(mnoise)*16)
        self.pos.x += map(mnoise,0,1,mapper,mapper)
        self.pos.y += map(mnoise,0,1,mapper,mapper)
        self.pos.z += map(mnoise,0,1,mapper,mapper)
        self.xoff+=0.05