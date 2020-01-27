import os
from cloudmesh.common.util import banner
# can be installed with pip install cloudmesh-common

class Provider:

    def __init__(self, name):
        self.name = name

    def start(self):
        os.system(f"multipass start {self.name}")
 
    def delete(self):
	# terminate and purge
	    os.system(f"multipass delete {self.name}")
		#Once purged it cannot be recovered. So commenting purge cmd
		#os.system(f"multipass purge")
    def list(self):
 	# list instances
        banner("list")
        os.system("multipass ls")

    def images(self):
        banner("images list")
        os.system("multipass find")

    def shell(self):
        print("shell")
        os.system(f"multipass shell {self.name}")

    def run(self, command):
        # please add self.name so the command gets started on the named vm 
        print (f"run {self.name} {command}")
        # improve next line
        os.system(f"multipass exec -- {self.name} {command}")

        
if __name__ == "__main__":
    # excellent-titmouse is multipass instance name
    p = Provider("excellent-titmouse")
    p.list()
    p.start()
    p.list()
    p.run("uname -r")
    p.images()
    p.delete()
    p.list()
