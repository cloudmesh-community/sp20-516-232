# sp20-516-232 E.Cloudmesh.Common.1 
from cloudmesh.common.util import banner
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.variables import Variables

variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

# banner
print ('')
banner('Welcome to sp20-516-232 Class!')

#verbose
m = {'ZipCode': '90503'}
VERBOSE(m)

#heading
HEADING(txt='Welcome to sp20-516-232 Class!', c='#', color='HEADER')
