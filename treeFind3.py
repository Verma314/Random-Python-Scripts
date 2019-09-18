import os
import humanize


def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


root = os.path.dirname(os.path.realpath(__file__))


for path, subdirs, files in os.walk(root):

	diskOfParent = get_size(path)
	human_size_ = humanize.naturalsize(diskOfParent, gnu=True) 
	print ("total disk usage by parent path", path , " is ",  human_size_)
	print ( "\n\n\n")

	for name in files:
		
		val = os.path.join(path,name)
		print ( " disk usage by " , val  )
		
		disk = os.path.getsize(val)
		human_size = humanize.naturalsize(disk, gnu=True) 
		
		print (human_size)
		print ( "\n\n\n")
	
	

	