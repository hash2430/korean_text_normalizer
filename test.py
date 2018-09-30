from korean import normalize

# read from test.txt and run normalize()
file = open('./test.txt', 'r')
while(True):
    line = file.readline();
    outLine = normalize(line);
    print(outLine)
    if (not line):
        break