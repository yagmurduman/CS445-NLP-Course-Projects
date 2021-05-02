import re
from bs4 import BeautifulSoup
ORGANIZATION =[]
with open(r"C:\Users\Lenovo\Desktop\CS445 PROJECT01\NER_example_data.txt",  encoding="utf8") as f:
    text = f.read()

    result = re.findall(r'(?<=\s<b_enamex TYPE=\"ORGANIZATION\">)\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"ORGANIZATION\">)\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"ORGANIZATION\">)\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text)+ re.findall(r'(?<=\s<b_enamex TYPE=\"ORGANIZATION\">)\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"ORGANIZATION\">)\w+\s+\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"ORGANIZATION\">)\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text)
    locresult = re.findall(r'(?<=\s<b_enamex TYPE=\"LOCATION\">)\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"LOCATION\">)\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"LOCATION\">)\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text)+ re.findall(r'(?<=\s<b_enamex TYPE=\"LOCATION\">)\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"LOCATION\">)\w+\s+\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"LOCATION\">)\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text)
    perresult = re.findall(r'(?<=\s<b_enamex TYPE=\"PERSON\">)\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"PERSON\">)\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"PERSON\">)\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text)+ re.findall(r'(?<=\s<b_enamex TYPE=\"PERSON\">)\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"PERSON\">)\w+\s+\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text) + re.findall(r'(?<=\s<b_enamex TYPE=\"PERSON\">)\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+(?=<e_enamex>\s)', text)


    with open(r"C:\Users\Lenovo\Desktop\CS445 PROJECT01\deneme.csv",'w') as a:
        for element in result:
            a.write(str(element))
            a.write('\n')

    with open(r"C:\Users\Lenovo\Desktop\CS445 PROJECT01\locdeneme.csv",'w') as b:
        for element in locresult:
            if(element.find('�') == True):()
            else:
                b.write(str(element))
                b.write('\n')                

    with open(r"C:\Users\Lenovo\Desktop\CS445 PROJECT01\perdeneme.csv",'w') as c:
        for element in perresult:
            c.write(str(element))
            c.write('\n')
a.close()
b.close()
c.close()
f.close()