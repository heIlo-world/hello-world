from commiter import commiter
from os import getcwd
from json import loads
from time import sleep
import schedule
import json

cwd = getcwd()
alreadyDoneFile = open('./done.txt', 'a')
alreadyDone = open('./done.txt', 'r').read().split(';')

def onTheDay():
  with open('./pixels.json') as jason:
    days = json.load(jason)

    for idx in range(len(days)):
      dayCount = 'p{}'.format(idx + 1)
      
      if dayCount not in alreadyDone:
        if days[dayCount]:
          print('today is commit day')
          commiter(cwd)

        alreadyDoneFile.write('{};'.format(dayCount))
        break

schedule.every().day.at('12:00').do(onTheDay)
while True:
  schedule.run_pending()
  sleep(30)