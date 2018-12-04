import json
import requests
from pprint import pprint

with open('/Users/tosoth/Projects/bitbucket/trv_chef/1') as f:
    data = json.load(f)

values=data["values"]

def reply(id, content):
      auth='tosoth:123123'
      url='http://localhost:7990/rest/api/1.0/projects/TRVCHEF/repos/trv_chef/pull-requests/1/comments'
      payload='{"text": "'+content+'","parent": {"id":'+str(id)+'}}'
      headers={'Content-type': 'application/json'}
      r = requests.post(url, data=payload, headers=headers, auth=('tosoth', '123123'))
      print r
      r.close()

for i in values:
  if i[u'action'] == u'COMMENTED':
    replies = i[u'comment'][u'comments']
    if replies == []:
      print "BINGO!"
      id=i[u'comment'][u'id']
      reply(id, "test done")
