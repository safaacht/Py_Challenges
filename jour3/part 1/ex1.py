messages = {
    "INFO": [],
    "WARNING": [],
    "ERROR": [],
    "DEBUG": [],
    "CRITICAL": []
}

with open('jour3/exercice.txt' , 'r') as file :
    lines = file.readlines()

    for line in lines :
        line_splt = line.split(']')
        line_splited = line_splt[0].split('[')
        # print(line_splited)
        for key in messages :
            if line_splited[1] == key:
                messages[key].append(line_splt[1]) 

        # print(messages)

with open('jour3/résumé_logs.txt' , 'w') as file :

    for i in messages :
        logs = len(messages[i])
        print(i ," : ",logs)
            
