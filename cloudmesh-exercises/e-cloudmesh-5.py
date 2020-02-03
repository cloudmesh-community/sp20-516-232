# sp20-516-232 E.Cloudmesh.Common.5: StopWatch
from cloudmesh.common.StopWatch import StopWatch
from time import sleep

StopWatch.start('timer')
sleep(1)
StopWatch.stop('timer')

print (StopWatch.get('timer'))

StopWatch.benchmark()
