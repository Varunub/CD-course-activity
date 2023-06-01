terminals="abcdefghijklmnopqrstuvwxyz1234567890id()+-*/=/{/}"
first={}
def fc(h,b):
    temp=[]
    flag=0
    for i in b:
        for j in i:
            if j=='ε':
                temp.append('ε')
                break
            elif j in terminals:
                temp.append(j)
                break
            elif j==h:
                print("Left Recursion Exist")
                exit(0)
            else:
                if first.keys().__contains__(j):
                    # print(first[j])
                    if 'ε' in first[j]:
                        data=list(first[j].copy())
                        data.pop(data.index('ε'))
                        temp.extend(data)
                        continue
                    else:
                        temp.extend(first[j])
                        break
                else:
                    flag=1
        if flag==1:
            break
    
    if(flag==0):
        return temp
    else:
        return []

def firstSymbol(input):
    # print(dict)
    keys=input.keys()
    for k in keys:
        temp=fc(k,input[k])
        if temp.__len__()!=0:
            first[k]=temp
        else:
            continue
    validatefirst(input)
    # print(first)
    return first

def modifyfirst():
    for i in first.keys():
        first[i]=set(first[i])


def validatefirst(input):
    rem=input.keys()-first.keys()
    if rem.__len__()==0:
        # print(first)
        modifyfirst()
    else:
        # print("In else")
        for k in rem:
            # print(input[k])
            temp=fc(k,input[k])
            # print(temp)
            if temp.__len__()!=0:
                first[k]=temp
            else:
                continue
        validatefirst(input)



