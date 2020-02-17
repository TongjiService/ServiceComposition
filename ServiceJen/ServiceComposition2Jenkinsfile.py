
f = open('Jenkinsfile')
a=f.read()
print(type(a))
print(a)
print(a.replace("stage", "is",2))

