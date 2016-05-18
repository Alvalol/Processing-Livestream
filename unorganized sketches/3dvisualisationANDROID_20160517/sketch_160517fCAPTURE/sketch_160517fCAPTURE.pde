import ketai.camera.*;
import processing.video.*;

int desiredAgents = 1;
AgentGroup agentGroup;
KetaiCamera sourceMovie;
//KetaiCamera cam;


void setup() 
{
   size(480,800,P3D);
   frameRate(24);
   orientation(PORTRAIT);
  //Camera KetaiCamera(PApplet pParent, int _width, int _height, int _framesPerSecond)
   sourceMovie = new KetaiCamera(this, 480, 800, 24);
  //debug
   sourceMovie.start();
  
  
 
  
  //sourceMovie = //new Movie(this, "movie.mp4");
  //sourceMovie.loop();
  
  agentGroup = new AgentGroup(sourceMovie);

  
  for(int x = 0; x < desiredAgents; x++)
  {
    Agent agent = new Agent();
    agentGroup.addAgent(agent);

  }


}

void draw()
{
  background(0);
  pushMatrix();
  agentGroup.run();
  popMatrix();


}

void onCameraPreviewEvent()
{
 sourceMovie.read(); 
}
/*
void movieEvent(Movie m)
{
     m.read(); 
}*/

void blender()
{
    blendMode(SUBTRACT);
    fill(10);
    noStroke();
    rect(0,0,width*2,height*2);
    blendMode(BLEND);
}     
               