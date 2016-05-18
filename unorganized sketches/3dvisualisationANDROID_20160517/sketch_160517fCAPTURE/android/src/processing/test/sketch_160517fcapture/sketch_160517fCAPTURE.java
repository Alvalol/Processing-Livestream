package processing.test.sketch_160517fcapture;

import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import ketai.camera.*; 
import processing.video.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class sketch_160517fCAPTURE extends PApplet {




int desiredAgents = 1;
AgentGroup agentGroup;
KetaiCamera sourceMovie;
//KetaiCamera cam;


public void setup() 
{
   
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

public void draw()
{
  background(0);
  pushMatrix();
  agentGroup.run();
  popMatrix();


}

public void onCameraPreviewEvent()
{
 sourceMovie.read(); 
}
/*
void movieEvent(Movie m)
{
     m.read(); 
}*/

public void blender()
{
    blendMode(SUBTRACT);
    fill(10);
    noStroke();
    rect(0,0,width*2,height*2);
    blendMode(BLEND);
}     
               
class Voxel
{
   // atomfighter version of voxel  
   // class variable
   public PVector voxel_position;
   public int voxel_color;
  
   // constructor
   Voxel(PVector p, int c)
   {
     this.voxel_position = p;
     this.voxel_color = c;
   }
}
public class Agent
{
  public PVector pos;
  public int col;
  
 public Agent()
 {
   pos = new PVector(0,0);
   col = color(0);
  // float xoff = 0.0;

 }
  
 public void run()
 {
     display();
 }
 
 public void display()
 {
        
        fill(col,255);
        noStroke();
        pushMatrix();
        translate(pos.x,pos.y,pos.z);
        box(8);
        popMatrix();

 }
 
 
}
public class AgentGroup
{

  public ArrayList<Agent> group;
  public ArrayList<Voxel> infocollection;
  public ArrayList<Voxel> voxelinfo;
  public KetaiCamera sourcemovie;


  public AgentGroup(KetaiCamera source)

  {
    group = new ArrayList<Agent>();
    infocollection = new ArrayList<Voxel>();
    sourceMovie = source;
  }

  public void run()
  {
     for(Agent agent : group)
  {
      agent.run();
  }
      setAgentPos();
  }

  public void addAgent(Agent agent)
  {
    group.add(agent);
  }

  public void setAgentPos()
  {
    voxelinfo = fetchPixels(sourceMovie);
    
  for(Agent agent : group)
  {
   for(Voxel m : voxelinfo)
   {
     agent.pos = m.voxel_position;
     agent.col = m.voxel_color;
     agent.run();
    
  }
    
    
  }
  }

  public ArrayList<Voxel> fetchPixels(KetaiCamera source)
  {
    source.loadPixels();
    int skip = 16;
    int minBright = 0;
    int maxBright = 255;
    int minDepth = 0;
    int maxDepth = 400;
    infocollection.clear();
    int smw = source.width;
    int smh = source.height;



    for (int x = 0; x<smw; x+=skip)
    {
      for (int y = 0; y<smh; y+=skip)
      {
        int loc = x + y * smw;
        if (brightness(source.pixels[loc]) > 100)
        {
          PVector newpos = new PVector(x, y, map(brightness(source.pixels[loc]), 
          minBright, maxBright, minDepth, maxDepth));
          int newcol = color(source.pixels[loc]);
          Voxel t = new Voxel(newpos,newcol);
          infocollection.add(t);
        }
      }
    }
      return infocollection;  
  }
}
  public void settings() {  size(480,800,P3D); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "sketch_160517fCAPTURE" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
