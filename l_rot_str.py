'''
INPUT: a list of elements, l, and an integere r, denoting the frequency at which the elements
in the list l will be left retotate
OUTPUT: a single line string containing all the elements in the rotated list, all separated by comma
'''
def rotLeft(l, r):
    new_a = a[d:]
    new_a.extend(a[:d])
    single_line_num =''
    
    for i in range(len(new_a)):
        single_line_num += ' '+str(new_a[i])
        #print(single_line_num)
    
    
    return single_line_num.lstrip()