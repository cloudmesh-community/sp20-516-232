# sp20-516-232 E.Cloudmesh.Common.2: DotDic
from cloudmesh.common.dotdict import dotdict

data = {
    'name': 'Ashok Singam',
    'course':'sp20-516-232'
}

data = dotdict(data)
print(data.name)
print(data.course)
