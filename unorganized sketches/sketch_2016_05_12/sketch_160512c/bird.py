class Bird(object):
    
    def __init__(self,x,y):
        self.acceleration = PVector(0,0)
        self.angle = random(TWO_PI)
        self.velocity = PVector(cos(self.angle),sin(self.angle))
        self.location = PVector(x, y)
        self.r = 2.0
        self.maxspeed = 1
        self.maxforce = 0.03
        self.leader = int(random(0,101))
        self.chosen = None
        self.timeOut = 0
        

## Display and run
        
    def run(self, flock):
        
        self.display()
        self.update()
        self.wrap()
        self.followLeader(flock)
        self.shapeCreator(flock)
        #self.leaderExpiration()

        
        
    def display(self):
        r = 0
        
        if self.leader > 40:
            with pushMatrix():
                rectMode(CENTER)
                fill(255,100)
                noStroke()
                rect(self.location.x,self.location.y,r,r)
        else:
                rectMode(CENTER)
                fill(255,0,0)
                #noFill()
                noStroke()
                rect(self.location.x,self.location.y,r,r)
            

    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
        
    def wrap(self):
        if self.location.x < 0:
            self.location.x = width 
        if self.location.x > width:
            self.location.x = 0
        if self.location.y > height:
            self.location.y = 0
        if self.location.y < 0:
            self.location.y = height
        
## physics stuff (?)

    def applyForce(self,force):
       self.acceleration.add(force)
       
    def followLeader(self,flock):
        for bird in flock:
            mindist = PVector.dist(self.location,bird.location)
            if (self.leader != 100 and  bird.leader == 100) and mindist < 100 and mindist > 50 :
                newdir = PVector.sub(self.location,bird.location)
                newdir.normalize()
                self.velocity.sub(newdir)
                #self.chosen = True
        
    def leaderExpiration(self):
        if self.chosen and self.timeOut == 0:
            self.timeOut +=1
        if self.timeOut >= 1000:
            self.chosen = False
        if self.leader:
            chosen = True
                
                
    def shapeCreator(self,flock):
        shapers = []
        for bird in flock:
            mindist = PVector.dist(self.location,bird.location)
            if ((mindist > 50 and mindist < 300 ) and (len(shapers) < 10)):#((self.leader != 100 and bird.leader !=100) and (mindist < 100 and mindist > 10) ) :
                shapers.append(bird.location)
        if len(shapers) > 10:
            shapers.pop(0)

        
        beginShape()         
        for birds in shapers:
            #if self.chosen:
                stroke(map(birds.x,0,width,0,255),map(birds.x,0,width,0,120),map(birds.x,0,width,50,180),255)
                #noStroke()
                #fill(map(birds.x,0,width,100,255),map(birds.y,0,width,10,40),map(birds.x,0,width,0,255),20)
                noFill()
                strokeWeight(0.1)
                curveVertex(birds.x,birds.y)
                curveVertex(self.location.x,self.location.y)
        endShape()
        

    
                      