def main():
    filename = "cs_unipi.txt"
    letterslist = listLettersFromTXT(filename)
    freq = lettersFrequence(letterslist)
    listofmostandless = appearances(freq)
    fmin = minandmax(listofmostandless,min)
    fmax = minandmax(listofmostandless,max)
    displayUpper(fmin,fmax,filename)
def listLettersFromTXT(filename):
    infile = open(filename,'r')
    lowerline = infile.readline().lower()
    line = ""
    lowertxt = ""
    global temptxt
    temptxt = []
    for item in lowerline:
        if 'a' <= item <= 'z':
            line += (item + " ")
        if item == " ":
            lowertxt += ("!" + " ")
        else:
            lowertxt += (item + " ")
    letterslist = line.split()
    temptxt = lowertxt.split()
    infile.close()
    return letterslist
def lettersFrequence(flettersList):
    freq = {}
    for ch in flettersList:
        freq[ch] = 0
    for ch in flettersList:
        freq[ch] = freq[ch] + 1
    return freq
def appearances(freq):
    listofmostandless = []
    for ch in freq.keys():
        listofmostandless.append((ch, freq[ch]))
    return listofmostandless
def minandmax(listofmostandless,appearance):
    x = appearance(listofmostandless,key=lambda x:x[1])
    fminmax = x[0]
    return fminmax
def displayUpper(fmin,fmax,filename):
    length = len(temptxt)
    for k in range(0,length):
        if temptxt[k] == fmin:
            temptxt[k] = fmax
        elif temptxt[k] == fmax:
            temptxt[k] = fmin
        elif temptxt[k] == "!":
            temptxt[k] = " "
    finaltxt = "".join(temptxt).upper()
    print (finaltxt)
main()
