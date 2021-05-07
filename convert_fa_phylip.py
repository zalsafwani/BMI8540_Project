#!/usr/bin/python
import sys

inputFile = sys.argv[1]
contents = open(inputFile,"r")
currLine = contents.readline()
seqList = {}
phyml = ""
while(currLine):
    if currLine.startswith('>'):
        if len(phyml) == 0:
            pass
        else:
             phyml_info = phyml.split('       ')
             seqList[phyml_info[0]] = phyml_info[1]
        #print(phyml)
        phyml = ""
        seq_num = currLine.strip('>').strip().split(' ')
        phyml = phyml + seq_num[0] + '       '
        currLine = contents.readline()
    else:
        seq = currLine.strip()
        phyml = phyml + seq 
        currLine = contents.readline()

#outFile = inputFile.strip('.fa') + '.phylip'
#out = open(outFile, "w")

print('', len(seqList), end = ' ')
valueList = list(seqList.values())
print(len(valueList[0].strip()))
#print(phyml, end = '')
for item in seqList:
    print(item + '       ' + seqList[item])
