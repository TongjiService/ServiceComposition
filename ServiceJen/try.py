import jenkins
import makejenkinsfile
import service
server = jenkins.Jenkins('http://localhost:8080', username='louie', password='1234')
user = server.get_whoami()
version = server.get_version()
#server.create_job('empty2', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()

_description='ads,asfsa,asdfsaf'
_title='qqwe'
description = makejenkinsfile.make(_description)

service.addservice(_title, description)