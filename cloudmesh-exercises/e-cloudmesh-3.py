# sp20-516-232 E.Cloudmesh.Common.3: FlatDict
from cloudmesh.common.FlatDict  import FlatDict

data = {
    'name': 'Ashok Singam',
    'address': {
        'city': 'Irvine',
        'state': 'CA'
    }
}
flat = FlatDict(data, sep='.')
print(flat)
