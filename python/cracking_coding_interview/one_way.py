def one_way(s1,s2):
    s1_bitmask=0b0
    s2_bitmask=0b0
    for c1 in s1:
         s1_bitmask=toggle(s1_bitmask,c1)
    for c2 in s2:
         s2_bitmask=toggle(s2_bitmask,c2)
    print(bin(s1_bitmask),bin(s2_bitmask))
    xor=s1_bitmask^s2_bitmask
    return check_at_most_two(xor)

def toggle(bitmask,character):
    if bitmask & (1<<(ord(character)-ord('a')))==0 :
            bitmask|=1<<(ord(character)-ord('a'))
    else:
        bitmask&=~(1<<(ord(character)-ord('a')))
    return bitmask

def check_at_most_two(bitmask):
    count=0
    while bitmask:
        if (bitmask&1)==1:
            count+=1
            if count>2:
                 return False
        bitmask>>=1
    return True
print(one_way('pale', 'ales'))

print(check_at_most_two(0b10000000000000))

#bitmask don't care order => wrong)