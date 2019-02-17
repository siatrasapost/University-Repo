def main():
    intervals = int(input("Πόσα διαστήματα με αριθμούς; "))
    list1 = []
    #Εισαγωγή αταξινόμητων στοιχείων στην list1(temp_list)
    for i in range (0,intervals):
        listx = []
        print ("\nΔιάστημα ",i+1,"από ",intervals,".\n")
        num1 = int(input("Πρώτος Όρος: "))
        listx.append(num1)
        num2 = int(input("Δεύτερος Όρος: "))
        listx.append(num2)
        list1.append(listx)
    sum = sumIntervals(list1,intervals)
    print ("\nΤο άθροισμα του μήκους των διαστημάτων είναι: ",sum)
def sumIntervals(temp_list, intrv):
    #Ταξινόμηση στοιχείων με βάση το πρώτο στοιχείο των πλειάδων
    temp_list.sort(key=Num1sort)
    fsum = 0
    new_list = []
    k = 0
    fsum_k = 0
    #ΑΡΧΗ τοποθέτησης σε λίστα για υπολογισμό μήκους
    while k != intrv-1:
        if temp_list[k][1] >= temp_list[k+1][0]:
            fcopy_ep(k,temp_list,new_list)
            if k == intrv-1:
                fcopy_ep(k+1,temp_list,new_list)
        else:
            fsum_k += temp_list[k+1][0] - temp_list[k][1]
            if k == 0:
                fcopy_k(k-1,temp_list,new_list)
                fcopy_k(k,temp_list,new_list)
            else:
                fcopy_k(k,temp_list,new_list)
        k +=1
    #ΤΕΛΟΣ τοποθέτησης σε λίστα
    #ΑΡΧΗ υπολογισμός μήκους
    min1 = min(new_list)
    max1 = max(new_list)
    rel_sum = max1 - min1
    fsum = rel_sum - fsum_k
    #ΤΕΛΟΣ υπολογισμός
    return fsum
def fcopy_ep(k_indx,ftemp_list,fnew_list):
    tmp1 = ftemp_list[k_indx][0]
    fnew_list.append(tmp1)
    tmp2 = ftemp_list[k_indx+1][1]
    fnew_list.append(tmp2)
def fcopy_k(k_indx,ftemp_list,fnew_list):
    tmp1 = ftemp_list[k_indx+1][0]
    fnew_list.append(tmp1)
    tmp2 = ftemp_list[k_indx+1][1]
    fnew_list.append(tmp2)
def Num1sort(e):
    return min(e)
main()
