
def make(_input):
    f = open('Jenkinsfile')
    file = f.read()
    end=file.find('stages')
    process_start=file[0:end+8]
    start=end+9
    end=file.find('}',start)
    process=file[start:end+11]
    process_end=file[341:348]
    '''start = my_job.find('<script>') + 8
    end = my_job.find('</script>')
    my_job.replace(my_job[start:end], jenkin)'''

    '''for i in range(0,len(file)+10):'''
        #print(i,file[i])
    _input = _input.encode('utf-8')
    len_input=len(_input.split(','))
    input=[]
    newline = '\n'
    for i in range(len_input):
        input.append(_input.split(',')[i])
    answer = process_start + newline
    for i in  range(len_input):
        process_temp=process.replace('case',input[i])
        process_temp = process_temp.replace('make', input[i])
        answer=answer+process_temp+newline
    answer=answer+process_end
    #print(answer)

    return answer


#make('casestart,caseend')

'''pipeline {
    agent any
    stages {
        stage('case') {
            steps {
                echo 'make'
            }
        }
        stage('Test'){
            steps {
                echo 'make check'
            }
        }
        stage('Deploy') {
            steps {
                echo 'make publish'
            }
        }
    }
}'''


