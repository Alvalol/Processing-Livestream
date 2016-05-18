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

  ArrayList<Voxel> fetchPixels(KetaiCamera source)
  {
    source.loadPixels();
    int skip = 32;
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
          color newcol = color(source.pixels[loc]);
          Voxel t = new Voxel(newpos,newcol);
          infocollection.add(t);
        }
      }
    }
      return infocollection;  
  }
}