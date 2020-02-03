# sp20-516-232 E.Cloudmesh.Common.2: DotDic
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.util import banner

person = {'name': 'John Doe', 'age': '40', 'sex': 'Male'}

data = dotdict(person)

banner('Demo dot dictionary')
print(data.name+' '+data.age+' '+data.sex)
