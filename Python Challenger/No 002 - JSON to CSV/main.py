import json

'''
'r'  -> Usado somente para ler algo;
'w'  -> Usado somente para escrever algo;
'r+' -> Usado para LER e ESCREVER algo;
'a'  -> Usado para acrescentar algo.
'''

if __name__ == '__main__':
    try:
        with open('No 002 - JSON to CSV/input.json', 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
        
        with open('No 002 - JSON to CSV/output.csv', 'w') as f:
            f.write(output)
        
        print('\033[32mCONVERSÃO FEITA COM SUCESSO!\033[m')
    
    except Exception as ex:
        print(f'ERROR: \033[31m{str(ex)}\033[m')