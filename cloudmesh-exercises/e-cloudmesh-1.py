from cloudmesh.common.util import banner
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.variables import Variables

variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

class CommonPrintUtil:

    def __init__(self, str):
        self.str = str

    def printBanner(self):
        banner(self.str)

    def demoVerbose(self):
        m = {'ZipCode': '90503'}
        VERBOSE(m)

    def printHeader(self):
        HEADING(self.str, c='#', color='HEADER')

if __name__ == "__main__":
    c = CommonPrintUtil("Welcome to sp20-516-232 Class!")
    c.printBanner()
    c.demoVerbose()
    c.printHeader()
