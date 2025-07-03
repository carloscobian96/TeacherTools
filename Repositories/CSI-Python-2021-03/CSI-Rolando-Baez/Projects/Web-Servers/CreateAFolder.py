import os
  
directory = "responses"
  
parent_dir = "Projects\Web-Servers"
  
path = os.path.join(parent_dir, directory)
  
os.mkdir(path)
print("Directory '% s' created" % directory)

