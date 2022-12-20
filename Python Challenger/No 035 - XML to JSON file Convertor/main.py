import json
import xmltodict
import xml.etree.ElementTree as E


"""
    'r'  -> Usado somente para ler algo;
    'r+' -> Usado para LER e ESCREVER algo;
    'w'  -> Usado somente para escrever algo;
    'w+' -> escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo);
    'a'  -> Usado para acrescentar algo;
    'a+' -> leitura e escrita (abre o arquivo para atualização)
"""

data_xml = E.parse('No 035 - XML to JSON file Convertor/country_data.xml')
root_xml = data_xml.getroot()
info_dic = {}

for content in root_xml:
    if content.tag not in info_dic:
        info_dic[content.tag] = [] # < details > - dicionário

        # ---- Values do arquivo XML
    value_dic={}
    for child_content in content:
        #key.....[child_content.tag]
        #value...[child_content.text]
        if child_content.tag not in value_dic:
            value_dic[child_content.tag] = child_content.text

    info_dic[content.tag].append(value_dic)
#  print(info_dic) -> Printar o dicionário com as informações

with open('No 035 - XML to JSON file Convertor/country_data.xml', 'r') as xml_file:
    data_dic = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dic)

with open('No 035 - XML to JSON file Convertor/country_data.json', 'w') as json_file:
    json_file.write(json_data)