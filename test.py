from korean import normalize

# read from test.txt and run normalize()
file = open('./test.txt', 'r')
wFile = open('./testResult.txt', 'w')
while(True):
    line = file.readline();
    outLine = normalize(line);
    print(outLine)
    wFile.write(outLine)
    wFile.write("\n")
    if (not line):
        break