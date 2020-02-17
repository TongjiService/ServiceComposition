


def service(_input,_output):
    #_input = _input.encode('utf-8')
    #_output = _output.encode('utf-8')

    len_input=len(_input.split(','))
    input=[]
    for i in range(len_input):
        input.append(_input.split(',')[i])

    len_output=len(_output.split(','))
    output=[]
    for i in range(len_output):
        output.append(_output.split(',')[i])
    print(input,output)
    return 0




service('1,1,1,1,1','2,2,2,2')