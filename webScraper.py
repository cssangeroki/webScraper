from bs4 import BeautifulSoup
import requests
import json

source = requests.get('https://www.joblist.com/b/all-jobs').text
jsonDict = {}
jobArray = []
soup = BeautifulSoup(source, 'lxml')

for jobs in soup.find_all('li'):
    job = jobs.text
    if job == 'Accounting & Finance':
        break
    jobArray.append({'name': job})

jsonDict['jobs'] = jobArray


with open('results.json', 'w') as outfile:
    json.dump(jsonDict, outfile)
