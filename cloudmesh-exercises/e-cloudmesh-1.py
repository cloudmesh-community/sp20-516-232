# sp20-516-232 E.Cloudmesh.Common.1 ---- Work inprogress

from cloudmesh.common.util import banner
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING

# banner
banner('Welcome to sp20-516-232 Class!')

# verbos
m = {'ZipCode': '90503'}
VERBOSE(m)

#heading
class Example(object):
    def doit(self):
        HEADING()
        print ('Hello')
