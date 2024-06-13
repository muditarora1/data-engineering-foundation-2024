'''
write a code to turn every odd index of your name to upper case only if it is a vowel.
'''
name = 'mudit_arora'
l=''
index=1
for i in name:
    if index%2==0:
        #print(i,'-->',index)
        l=l+i
    else:
        if i in ('a','e','i','o','u'):
            #print(i, '-->', index)
            l = l+i.upper()
        else:
            #print(i, '-->', index)
            l=l+i
    index += 1
#l = str(l)
print(l)