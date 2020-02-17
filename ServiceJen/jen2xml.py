import jenkins
import xmlescape


def jenk2xml(jenkin):
    server = jenkins.Jenkins('http://localhost:8080', username='louie', password='1234')
    my_job = server.get_job_config('demo')
    my_job=my_job.encode('gbk')
    start = my_job.find('<script>') + 8
    end = my_job.find('</script>')
    ppp=my_job.replace(my_job[start:end], jenkin)
    return ppp









'''server = jenkins.Jenkins('http://localhost:8080', username='louie', password='129c143b134c141b')



my_job = server.get_job_config('demo')

savedBinFile = open("jenkinsxml",'w'); # open a file, if not exist, create it
savedBinFile.write(my_job);
savedBinFile.close();
start=my_job.find('<script>')+8
end=my_job.find('</script>')

f=open("Jenkinsfile")
lines=f.read()
a=xmlescape.xml_escape(lines)




my_job.replace(my_job[start:end],a)
print my_job
server.create_job('luyifan2',my_job)
server.enable_job('luyifan2')
server.build_job('luyifan2')

#print a#str'''