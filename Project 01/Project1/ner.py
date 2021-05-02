import re
import sys

def main():
    output = ""
    input_file_path = sys.argv[1]

    a = open(r'C:\Users\Lenovo\Desktop\CS445 PROJECT01\location.csv', encoding="utf8")
    LOCATIONS = a.read().splitlines()
    for location in LOCATIONS:
        if (location.find('�') != -1):
            LOCATIONS.remove(location)
    a.close()
        
    b = open(r'C:\Users\Lenovo\Desktop\CS445 PROJECT01\organization.csv', encoding="utf8")
    ORGANIZATIONS =  b.read().splitlines() 
    b.close()

    c = open(r'C:\Users\Lenovo\Desktop\CS445 PROJECT01\names.csv', encoding="utf8")
    PERSONS = c.read().splitlines()
    for person in PERSONS:
        if (person.find('?') != -1):
            PERSONS.remove(person)
    c.close()


    line_count= 0
    f = open(input_file_path, encoding="utf-8")
    for x in f:
        SAMPLE_TEXT = x
        line_count+=1

    #------------ PERSON RULES ------------
        perTemp = []
        found = False

        #Bey ve Hanım karışıklık olmasın diye önce
        if 'Bey' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Bey*',SAMPLE_TEXT)[0]
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word):
                        found = True
                if(found == False):
                    perTemp.append(word.split(" Bey")[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word) + '\n')

        if 'Hanım' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Hanım*',SAMPLE_TEXT)[0]
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word):
                        found = True
                if(found == False):
                    perTemp.append(word.split(" Hanım")[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word) + '\n')



        #assuming people can have at most 4 names
        for uppercaseWord in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜ]*[a-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT):
            uppercaseWord = SAMPLE_TEXT[uppercaseWord.start():uppercaseWord.end()]
            name = uppercaseWord.split(" ")
            cont = True
            contList = ['Sokak','Mahallesi','Dağı','Köyü','Köprüsü','Mezarlığı','Sarayı','Üniversitesi','Holding','Vakfı','Federasyonu',
                            'Enstitüsü','Kurumu','Bankası']
            for i in name:
                for j in contList:
                    if(i ==j):
                        cont = False
        
            if(cont == True):
                firstname = name[0]
                if(uppercaseWord in PERSONS):
                    if(len(perTemp)!= 0):
                        for word in perTemp:
                            if(word == firstname):
                                found = True
                        if(found == False):
                            perTemp.append(uppercaseWord)
                            output += ("Line " + str(line_count) + ": " + "PERSON " + str(uppercaseWord) + '\n')
                        found= False
                    else:
                        perTemp.append(uppercaseWord)
                        output += ("Line " + str(line_count) + ": " + "PERSON " + str(uppercaseWord) + '\n')

                elif firstname in PERSONS:
                    if(len(perTemp)!= 0):
                        for word in perTemp:
                            if(word == firstname):
                                found = True
                        if(found == False):
                            perTemp.append(uppercaseWord)
                            output += ("Line " + str(line_count) + ": " + "PERSON " + str(uppercaseWord) + '\n')
                        found= False
                    else:
                        perTemp.append(uppercaseWord)
                        output += ("Line " + str(line_count) + ": " + "PERSON " + str(uppercaseWord) + '\n')


        # RULE_EXAMPLE 3
        if 'Prof. Dr.' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Prof. Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Prof. Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')

        if 'Prof.' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Prof. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Prof. Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')
        
        if 'Dr.' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')
        
        if 'Av.' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Av. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Prof. Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')


        if 'Sayın' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Sayın )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Sayın )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')

        if 'Sevgili' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Sevgili )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Sevgili )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')
        
        if 'Cumhurbaşkanı' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Cumhurbaşkanı )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Cumhurbaşkanı )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')

        if 'Vali' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Vali )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Vali )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')

        if 'Belediye Başkanı' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Belediye Başkanı )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Belediye Başkanı )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')

        if 'Bakan' in SAMPLE_TEXT:
            word = re.findall(r'(?<=Bakan )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|(?<=Bakan )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for person in perTemp:
                    if(person == word[0]):
                        found = True
                if(found == False):
                    perTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "PERSON " + str(word[0]) + '\n')

        
        #---------------- LOCATION RULES ------------
        locTemp = []

        for word in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT):
            word = SAMPLE_TEXT[word.start():word.end()]
            if word in LOCATIONS:
                locTemp.append(word)
                output += ("Line " + str(line_count) + ": " +"LOCATION " + word + '\n')

        for word in re.finditer(r'[A-ZÇĞİÖŞÜ]*',SAMPLE_TEXT):
            word = SAMPLE_TEXT[word.start():word.end()]
            if word in LOCATIONS:
                locTemp.append(word)
                output += ("Line " + str(line_count) + ": " +"LOCATION " + word + '\n')

        if 'şehri' in SAMPLE_TEXT: #daha çok şehri şeklinde bulunur cümlelerde
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* şehri*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* şehri*',SAMPLE_TEXT)
            if(len(temp) != 0):
                temp = temp[0]
                print(temp)
                locWord = temp.split(" şehri")[0]
                print(locWord)
                found = False
                for loc in locTemp:
                    if(loc == locWord):
                        found = True
                if(found == False):
                    locTemp.append(locWord)
                    output += ("Line " + str(line_count) + ": " +"LOCATION " + locWord + '\n')
        
        if 'ülke' in SAMPLE_TEXT:
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* ülke\w+',SAMPLE_TEXT)[0]
            locWord = temp.split(" ")[0]
            found = False
            for loc in locTemp:
                if(loc == locWord):
                    found = True
            if(found == False):
                locTemp.append(locWord)
                output += ("Line " + str(line_count) + ": " +"LOCATION " + locWord + '\n')

        if 'Sokak' in SAMPLE_TEXT:
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Sokak\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Sokak\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Sokak\w+',SAMPLE_TEXT)
            if(len(temp) != 0):
                temp = temp[0]
                locWord = temp.split(" Sokak")[0]
                found = False
                for loc in locTemp:
                    if(loc == locWord):
                        found = True
                if(found == False):
                    locTemp.append(temp)
                    output += ("Line " + str(line_count) + ": " +"LOCATION " + temp + '\n')

        if 'Mahalle' in SAMPLE_TEXT:
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Mahalle\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Mahalle\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Mahalle\w+',SAMPLE_TEXT)
            if(len(temp) != 0):
                temp = temp[0]
                locWord = temp.split(" Mahalle")[0]
                found = False
                for loc in locTemp:
                    if(loc == locWord):
                        found = True
                if(found == False):
                    locTemp.append(temp)
                    output += ("Line " + str(line_count) + ": " +"LOCATION " + temp + '\n')

        if 'Dağ' in SAMPLE_TEXT:
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Dağ\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Dağ\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Dağ\w+',SAMPLE_TEXT)
            if(len(temp) != 0):
                temp = temp[0]
                locWord = temp.split(" Dağ")[0]
                found = False
                for loc in locTemp:
                    if(loc == locWord):
                        found = True
                if(found == False):
                    locTemp.append(temp)
                    output += ("Line " + str(line_count) + ": " +"LOCATION " + temp + '\n')

        if 'Köy' in SAMPLE_TEXT:
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Köy\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Köy\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Köy\w+',SAMPLE_TEXT)
            if(len(temp) != 0):
                temp = temp[0]
                locWord = temp.split(" Köy")[0]
                found = False
                for loc in locTemp:
                    if(loc == locWord):
                        found = True
                if(found == False):
                    locTemp.append(temp)
                    output += ("Line " + str(line_count) + ": " +"LOCATION " + temp + '\n')
        
        if 'Köprü' in SAMPLE_TEXT:
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Köprü\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Köprü\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Köprü\w+',SAMPLE_TEXT)
            if(len(temp) != 0):
                temp = temp[0]
                locWord = temp.split(" Köprü")[0]
                found = False
                for loc in locTemp:
                    if(loc == locWord):
                        found = True
                if(found == False):
                    locTemp.append(temp)
                    output += ("Line " + str(line_count) + ": " +"LOCATION " + temp + '\n')

        if 'Saray' in SAMPLE_TEXT:
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Saray\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Saray\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Saray\w+',SAMPLE_TEXT)
            if(len(temp) != 0):
                temp = temp[0]
                locWord = temp.split(" Saray")[0]
                found = False
                for loc in locTemp:
                    if(loc == locWord):
                        found = True
                if(found == False):
                    locTemp.append(temp)
                    output += ("Line " + str(line_count) + ": " +"LOCATION " + temp + '\n')


        if 'Mezarlı' in SAMPLE_TEXT:
            temp = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Mezarlı\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Mezarlı\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Mezarlı\w+',SAMPLE_TEXT)
            if(len(temp) != 0):
                temp = temp[0]
                locWord = temp.split(" Mezarlı")[0]
                found = False
                for loc in locTemp:
                    if(loc == locWord):
                        found = True
                if(found == False):
                    locTemp.append(temp)
                    output += ("Line " + str(line_count) + ": " +"LOCATION " + temp + '\n')


    #-------------- ORGANIZATION RULES --------------
        orgTemp = []
        #Based on organization patterns I've seen
        for uppercaseWord in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT):
            uppercaseWord = SAMPLE_TEXT[uppercaseWord.start():uppercaseWord.end()]
            if uppercaseWord in ORGANIZATIONS:
                found = False
                for org in orgTemp:
                    if(org == uppercaseWord):
                        found = True
                if(found == False):
                    orgTemp.append(uppercaseWord)
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + uppercaseWord + '\n')


        for uppercaseWord in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT):
            uppercaseWord = SAMPLE_TEXT[uppercaseWord.start():uppercaseWord.end()]
            if uppercaseWord in ORGANIZATIONS:
                found = False
                for org in orgTemp:
                    if(org == uppercaseWord):
                        found = True
                if(found == False):
                    orgTemp.append(uppercaseWord)
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + uppercaseWord + '\n')



        for word in re.finditer(r'[A-ZÇĞİÖŞÜ]*',SAMPLE_TEXT):
            word = SAMPLE_TEXT[word.start():word.end()]
            if word in ORGANIZATIONS:
                orgTemp.append(word)
                output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + word + '\n')


        if 'Üniversite' in SAMPLE_TEXT:
            word= re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]\w+ Üniversite\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]\w+ Üniversite\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]\w+ Üniversite\w+|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Üniversite\w+',SAMPLE_TEXT)
            if(len(word) != 0):
                word = word[0]
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')

        if 'Şirket' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Şirket[A-ZÇĞİÖŞÜa-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')
        
        if 'Holding' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Holding[A-ZÇĞİÖŞÜa-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')

        if 'Takım' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Takım[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Takım[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Takım[A-ZÇĞİÖŞÜa-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')

        if 'Vakfı' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Vakfı[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Vakfı[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Vakfı[A-ZÇĞİÖŞÜa-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')

        if 'Federasyonu' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Federasyonu[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Federasyonu[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Federasyonu[A-ZÇĞİÖŞÜa-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')

        if 'Enstitü' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Enstitü[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Enstitü[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Enstitü[A-ZÇĞİÖŞÜa-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')
        
        if 'Kurumu' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Kurumu[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Kurumu[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Kurumu[A-ZÇĞİÖŞÜa-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')

        if 'Banka' in SAMPLE_TEXT:
            word = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Banka[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Banka[A-ZÇĞİÖŞÜa-zçğıöşü]*|[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Banka[A-ZÇĞİÖŞÜa-zçğıöşü]*',SAMPLE_TEXT)
            if(len(word) != 0):
                found = False
                for org in orgTemp:
                    if(org == word):
                        found = True
                if(found == False):
                    orgTemp.append(word[0])
                    output += ("Line " + str(line_count) + ": " + "ORGANIZATION " + str(word[0]) + '\n')

        #---------------------- TIME RULES ---------------
        AY_LIST= {"ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"}
        GUN_LIST= {"pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"}

        #for finding dates like yyyy-mm-dd etc.
        for dateWord in re.finditer(r'\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4}|\d{4}\/\d{2}\/\d{2}|\d{2}\/\d{2}\/\d{4}|\d{2}(\\)\d{2}(\\)\d{4}|\d{4}(\\)\d{2}(\\)\d{2}|\d{2}.\d{2}.\d{4}|\d{4}.\d{2}.\d{2}',SAMPLE_TEXT):
            dateWord = SAMPLE_TEXT[dateWord.start():dateWord.end()]
            print("Line",line_count,":","TIME", dateWord)

        #12 Mayıs 1998, 12 mayıs 1998 ve 12 mayıs, 12 Mayıs
        for dateWord in re.finditer(r'\d{2}\s[A-ZÇĞIÖŞÜa-zçğıöşü]*\s\d{4}|\d{2}\s[A-ZÇĞIÖŞÜa-zçğıöşü]*',SAMPLE_TEXT):
            dateWord = SAMPLE_TEXT[dateWord.start():dateWord.end()]
            month = dateWord.split(" ")[1]
            for ay in AY_LIST:
                    if(month.lower() == ay): 
                        output += ("Line " + str(line_count) + ": " + "TIME " + dateWord + '\n')

        #1999'da
        for dateWord in re.finditer(r'\d{4}\'[A-ZÇĞIÖŞÜa-zçğıöşü]*',SAMPLE_TEXT):
            dateWord = SAMPLE_TEXT[dateWord.start():dateWord.end()]
            dateWord = dateWord.split('\'')[0]
            output += ("Line " + str(line_count) + ": " + "TIME " + dateWord + '\n')
        
        if 'yıl' in SAMPLE_TEXT:
            word= re.findall(r'\d{4}(?=\s+yıl\w+)',SAMPLE_TEXT)
            output += ("Line " + str(line_count) + ": " + "TIME " + str(word[0]) + '\n')
        
        if 'sene' in SAMPLE_TEXT:
            word = re.findall(r'\d{4}(?=\s+sene\w+)',SAMPLE_TEXT)
            output += ("Line " + str(line_count) + ": " + "TIME " + str(word[0]) + '\n')

        if 'ay' in SAMPLE_TEXT:  #Mart ayı 
            word = re.findall(r'([A-ZÇĞIÖŞÜa-zçğıöşü]*(?=\s+ay[a-zçğıöşü]))',SAMPLE_TEXT)
            if(len(word) != 0):
                for ay in AY_LIST:
                    if(word[0].lower() == ay): 
                        output += ("Line " + str(line_count) + ": " + "TIME " + str(word[0]) + '\n')

        if 'gün' in SAMPLE_TEXT: #Pazar günü
            word = re.findall(r'[A-ZÇĞIÖŞÜa-zçğıöşü]*(?=\s+gün\w+)',SAMPLE_TEXT)
            if(len(word) != 0):
                    for gun in GUN_LIST:
                        if(word[0].lower() == gun): 
                            output += ("Line " + str(line_count) + ": " + "TIME " + str(word[0]) + '\n')

        if 'saat' in SAMPLE_TEXT: #saat 12, saat 12:00
            word= re.findall(r'((?<=saat )\d{2}\:\d{2}|(?<=saat )\d{2}\.\d{2}|(?<=saat )\d{2}|(?<=saat )\d{1})',SAMPLE_TEXT)
            if(len(word) != 0):
                output += ("Line " + str(line_count) + ": " + "TIME " + str(word[0]) + '\n')

    print(output)

if __name__ == "__main__":
    main()