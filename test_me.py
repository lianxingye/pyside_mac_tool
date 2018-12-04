import json
import requests
from pprint import pprint

#curl -sb -H "Accept: application/json" -u tosoth:123123 http://localhost:7990/rest/api/1.0/projects/TRVCHEF/repos/trv_chef/pull-requests/1/activities > /tmp/1
def get_pr_detail(my_id):
      auth='tosoth:123123'
      url='http://localhost:7990/rest/api/1.0/projects/TRVCHEF/repos/trv_chef/pull-requests/'+str(my_id)+'/activities'
      headers={'Content-type': 'application/json'}
      r = requests.get(url, headers=headers, auth=('tosoth', '123123'))
      with open('/tmp/1','w') as f:
        f.write(r.text)
      r.close()

def handle(my_id):
  with open('/tmp/'+str(my_id)) as f:
    data = json.load(f)

  values=data["values"]
  for i in values:
   if i[u'action'] == u'COMMENTED':
    replies = i[u'comment'][u'comments']
    if replies == []:
      print "BINGO!"
      id=i[u'comment'][u'id']
      reply(id, "test done1")

def reply(id, content):
      auth='tosoth:123123'
      url='http://localhost:7990/rest/api/1.0/projects/TRVCHEF/repos/trv_chef/pull-requests/1/comments'
      payload='{"text": "'+content+'","parent": {"id":'+str(id)+'}}'
      headers={'Content-type': 'application/json'}
      r = requests.post(url, data=payload, headers=headers, auth=('tosoth', '123123'))
      print r
      r.close()

def get(url):
      url='http://localhost:7990/rest/api/1.0/projects/TRVCHEF/repos/trv_chef/pull-requests'
      headers={'Content-type': 'application/json'}
      r = requests.get(url, headers=headers, auth=('tosoth', '123123'))
      r.close()



if True:
      url='http://localhost:7990/rest/api/1.0/projects/TRVCHEF/repos/trv_chef/pull-requests'
      headers={'Content-type': 'application/json'}
      r = requests.get(url, headers=headers, auth=('tosoth', '123123'))
      pr_text = r.text
      r.close()

with open('/tmp/pr','w') as f:
    f.write(pr_text)

with open('/tmp/pr') as f:
    data_pr = json.load(f)

for i in data_pr["values"]:
  pr_content=i[u'description']
  pr_id=i[u'id']
  print pr_id
  get_pr_detail(pr_id)
  handle(pr_id)
  
