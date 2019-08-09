curl -sb -H "Accept: application/json" -u tosoth:123123 http://localhost:7990/rest/api/1.0/projects/TRVCHEF/repos/trv_chef/pull-requests > /tmp/pr

curl -sb -H "Accept: application/json" -u tosoth:123123 http://localhost:7990/rest/api/1.0/projects/TRVCHEF/repos/trv_chef/pull-requests/1/activities > /tmp/1

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
python $DIR/test_me.py

