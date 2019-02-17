import urllib.request
def main():
    readpage = requestWebpage()
    listpage(readpage)
def requestWebpage():
    f = urllib.request.urlopen(input("Eισάγετε ένα URL: "))
    tmp = f.read().decode('utf-8')
    return tmp
def listpage(rpage):
    temp = rpage.split()
    length = len(temp)
    pcounter = 0
    brcounter = 0
    hrcounter = 0
    for k in range(0,length):
        tmp = temp[k]
        pcounter += tmp.count('<p')
        brcounter += tmp.count('<br')
        hrcounter += tmp.count('href')
    print (pcounter,brcounter,hrcounter)
main()
