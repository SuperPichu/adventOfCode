import re
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
def find_all(line,sub):
    return [(a.start(), a.end()) for a in list(re.finditer(sub, line))]
def checkForPattern(line,lindex,rindex,source):
    x = 0
    y = 1
    while y < len(line):
        charx = line[x]
        chary = line[y]
        #print('curr x,y ' + charx + ', ' + chary)
        test = charx + chary + chary + charx
        foundx = source.find(test)
        #print(foundx)
        foundy = foundx + 3
        #print(foundy)
        if foundx > -1 and charx != chary and '[' not in test and ']' not in test:
            z = 0
            while z < len(lindex):
                if foundx > lindex[z] and foundy < rindex[z]:
                    return False
                z = z + 1
            print(str(foundx) + ', ' + str(foundy))
            return True
        else:
            #print(line + ':F')
            x = y
            y = y + 1
    return -1
def checkForPattern2(line,lindex,rindex,source):
    w = 0
    x = 1
    y = 2
    while y < len(line):
        charw = line[w]
        charx = line[x]
        chary = line[y]
        if charw is chary:
            test = charw + charx + chary
            test2 = charx + chary + charx
            if source.find(test) > -1 and source.find(test2) > -1 and charx != chary and '[' not in test and ']' not in test:
                supernet = False
                hypernet = False
                finds = find_all(source,test)
                print(test)
                for foundx,foundy in finds:
                    print(str(foundx) + ', ' + str(foundy))
                    z = 0
                    while z < len(lindex):
                        if foundx > lindex[z] and foundy <= rindex[z]:
                            hypernet = True
                            print(test + ' in hyper')
                        z = z + 1
                if hypernet:
                    finds = find_all(source,test2)
                    for foundx,foundy in finds:
                        z = 0
                        count = 0
                        while z < len(lindex):
                            if foundx > lindex[z] and foundy <= rindex[z]:
                                count = count + 1
                                print(test2 + ' in hyper')
                            z = z + 1
                        if count is 0:
                            print(test2 + ' in super')
                            supernet = True
                else:
                    finds = find_all(source,test2)
                    for foundx,foundy in finds:
                        z = 0
                        while z < len(lindex):
                            if foundx > lindex[z] and foundy <= rindex[z]:
                                hypernet = True
                                print(test2 + ' in hyper')
                            z = z + 1
                    if hypernet:
                        finds = find_all(source,test)
                        for foundx,foundy in finds:
                            z = 0
                            count = 0
                            while z < len(lindex):
                                if foundx > lindex[z] and foundy <= rindex[z]:
                                    count = count + 1
                                    print(test + ' in hyper')
                                z = z + 1
                            if count is 0:
                                print(test + ' in super')
                                supernet = True
                if supernet and hypernet:
                    return True
                # if hypernet:
                #     foundx = source.find(test2)
                #     foundy = foundx + 2
                #     z = 0
                #     while z < len(lindex):
                #         if not foundx < lindex[z] and not foundy > rindex[z]:
                #             print(test2 + ' in super')
                #             return True
                #         z = z + 1
                # if supernet:
                #     foundx = source.find(test2)
                #     foundy = foundx + 2
                #     z = 0
                #     while z < len(lindex):
                #         if foundx > lindex[z] and foundy < rindex[z]:
                #             print(test2 + ' in hyper')
                #             return True
                #         z = z + 1
        w = w + 1
        x = x + 1
        y = y + 1
    return -1
inp = open('day7.txt','r')
count = 0
for line in inp:
    line = line.replace(' ','')
    line = line.replace('\n', '')
    lindex = find(line,'[')
    #print(lindex)
    rindex = find(line,']')
    #print(rindex)
    check = checkForPattern2(line,lindex,rindex,line)
    if check is True:
        print(line + ':T')
        count = count + 1
print(count)
