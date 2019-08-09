docker rm -f jenkins-docker_TEST_ALL_ENV-1249
docker run --privileged=true --name=jenkins-docker_TEST_ALL_ENV-1249 -h=stg-qtrqa501z.stg.jp.docker.local -v ~/Projects/trv-chef:/usr/local/src/trv-chef -v /sys/fs/cgroup:/sys/fs/cgroup -w /usr/local/src/trv-chef -u root -e USER=root -d docker-regi.intra.rakuten-it.com/trv/centos7.3:rbc-lg /sbin/init
