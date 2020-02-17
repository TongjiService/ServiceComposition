import jenkins
import xmlescape
import jen2xml

def addservice(name,jenkinsfile):
    #jenkinsfile=jenkinsfile.encode('utf-8')
    name=name.encode('utf-8')
    server = jenkins.Jenkins('http://localhost:8080', username='louie', password='1234')
    #f=open("Jenkinsfile")
    #lines=f.read()
    #print(type(jenkinsfile))
    a=xmlescape.xml_escape(jenkinsfile)
    #print(a)
    #print(type(a))
    my_job=jen2xml.jenk2xml(a)
    #print(my_job)
    #print(type(my_job))
    server.create_job(name,my_job)
    server.enable_job(name)
    server.build_job(name)

#server = jenkins.Jenkins('http://localhost:8080', username='louie', password='1234')
#print(server.jobs_count())
#jobs = server.get_jobs()
#print(jobs[1])


#server.delete_job()
'''<type 'str'>
<type 'str'>
<type 'unicode'>
'''