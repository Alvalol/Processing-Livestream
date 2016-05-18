public class AgentGroup
{

  public ArrayList<Agent> group;
  public ArrayList<Voxel> infocollection;
  public ArrayList<Voxel> voxelinfo;
  public Movie sourcemovie;


  public AgentGroup(Movie source)

  {
    group = new ArrayList<Agent>();
    infocollection = new ArrayList<Voxel>();
    sourceMovie = source;
  }

  void run()
  {
     for(Agent agent : group)
  {
      agent.run();
  }
      setAgentPos();
  }

  void addAgent(Agent agent)
  {
    group.add(agent);
  }

  void setAgentPos()
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

  ArrayList<Voxel> fetchPixels(Movie source)
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
        if (brightness(source.pixels[loc]) > 1)
        {
          PVector newpos = new PVector(x, y, map(brightness(source.pixels[loc]), 
          minBright, maxBright, minDepth, maxDepth));
          color newcol = color(source.pixels[loc]);
          Voxel t = new Voxel(newpos,newcol);
          infocollection.add(t);
        }
      }
    }
      return infocollection;  
  }
}