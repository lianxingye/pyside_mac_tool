# ------------------------
# Variables
# ------------------------
WORKDIR=/usr/local/src/trv-chef
BUILD_TAG='21'
CONTAINER="${BUILD_TAG}"

#jenkins-job
JENKINS_URL_DEV=""
JENKINS_URL_STG=""
custom_command=${custom_command:-uname -a}
ENVIRONMENT=dev

TARGET=qtrqa5
recipe=trv_nodejs
target_env=stg

ENVIRONMENT=$target_env
HOST_GROUP=$TARGET
if [ "${ENVIRONMENT}" != "prod" ]; then
    SVR_01="${ENVIRONMENT}-${HOST_GROUP}01z"
else
    SVR_01="${HOST_GROUP}01z"
fi  

SPEC_COMMAND="
export PATH=/usr/local/chef/embedded/bin:\$PATH
cd serverspec
LOCAL_EXEC=1 opt=debug /usr/local/chef/embedded/bin/rake SPEC_OPTS="-fd" spec:${SVR_01}['${spec_name%/*}'] || exit 1
"

spec_name=$recipe

now=$(date +"%T")
echo "Current time : $now"

for ENVIRONMENT in `echo ${target_env} | sed 's/,/ /g'`; do 
for HOST_GROUP in `echo $TARGET | sed 's/,/ /g'`; do 
  echo "===============================TEST $now=================================="
  echo "===============================TEST $now=================================="
  echo "===============================TEST $now=================================="
  echo "===============================TEST $now=================================="
  echo "===============================TEST $now=================================="
  echo "===============================TEST $now=================================="
  echo "===============================TEST $now=================================="
  echo "===============================TEST $now=================================="
  echo "===============================TEST $now=================================="
  docker exec jenkins-docker_TEST_ALL_ENV-1249 /bin/bash -c "unset http_proxy https_proxy;/usr/local/chef/embedded/bin/chef-client -z -l error -c solo.rb -j nodes/$TARGET.json -F doc -o $recipe -W || exit 1"
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  echo "===============================REAL $now=================================="
  docker exec jenkins-docker_TEST_ALL_ENV-1249 /bin/bash -c "unset http_proxy https_proxy;/usr/local/chef/embedded/bin/chef-client -z -l error -c solo.rb -j nodes/$TARGET.json -F doc -o $recipe || exit 1"
#  echo "===============================(SKIPPED)RUNSPEC $now=================================="
  #docker exec jenkins-docker_TEST_ALL_ENV-1249 /bin/bash -c "$(cat <<EOL
#${SPEC_COMMAND}
#EOL
#    )"
done
done
echo "=================DONE $now======================"
