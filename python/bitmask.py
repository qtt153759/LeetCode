import sys


def get_bit(value, bit_index):
    return value & (1 << bit_index)


def get_normalized_bit(value, bit_index):
    return (value >> bit_index) & 1


def set_bit(value, bit_index):
    return value | (1 << bit_index)


def clear_bit_at(value, bit_index):
    return value & ~(1 << bit_index)

def clear_bit_left(value, bit_index) :
    mask = (1 << bit_index) - 1
    return value & mask

def clear_bit_right(value,bit_index):
    mask=(-1<<(bit_index+1))
    return mask&value

def update_bit(value,bit_index,bit_val):
    mask=~(1<<bit_index)
    return mask&value|(bit_val<<bit_index)

def toggle_bit(value, bit_index):
    return value ^ (1 << bit_index)

def toggle(bitmask,character):
    if bitmask & (1<<(ord(character)-ord('a')))==0 :
            bitmask|=1<<(ord(character)-ord('a'))
    else:
        bitmask&=~(1<<(ord(character)-ord('a')))
    return bitmask

def count_set_bits(bitmask):
    count=0
    while bitmask:
        count+=bitmask&1
        bitmask>>=1
    return count

def check_exact_one_bit_set(bitmask):
    return (bitmask & (bitmask-1))==0

def module(dividend,divisor):
    return dividend&((1 << divisor) - 1)

def swap(a,b): #without using temp variable
    a^=b
    b^=a
    a^=b
    return a,b

def sign(a):
    return (a>>31)&1

def flip(a):
    return a^1
def find_max(a,b): #without operator
    c=a-b
    sa,sb,sc=sign(a),sign(b),sign(c)
    k=flip(sc)+sb*sc
    return a*k+b*flip(k)


if __name__ == "__main__":
    fruits = {"apple", "banana", "tomato"}
    veggies = {"eggplant", "tomato"}
    print(fruits | veggies)
    print(fruits & veggies)
    print(fruits ^ veggies)
    print(fruits - veggies)
    print(bin(0b0001 ^ 0b1011))
    print((0b1011 >> 1))
    print(bin(update_bit(0b1011, 2,1)))
    print(bin(1024&0x1F ))
    print(bin(10111))
    print("ok",sys.getsizeof(0b11101000))
    print(module(13,2))
    abc={"Hồ Gươm":["yes","no"], 'Hồ Tây':["yes","no"],'Tháp Rùa':["yes","no"],"Cầu Thê Húc":["yes","no"],"Bưu Điện":["yes","no"],"Vườn Hoa":["yes","no"],"Chùa Trấn Quốc":["yes","no"],"Đền Quán Thánh":["yes","no"],"Khách Sạn":["yes","no"],"Công Viên Nước":["yes","no"]}
    print(find_max(-6,5))
    print(bin(1/10))