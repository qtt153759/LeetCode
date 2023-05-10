def get_bit(value, bit_index):
    return value & (1 << bit_index)


def get_normalized_bit(value, bit_index):
    return (value >> bit_index) & 1


def set_bit(value, bit_index):
    return value | (1 << bit_index)


def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)


def toggle_bit(value, bit_index):
    return value ^ (1 << bit_index)


if __name__ == "__main__":
    fruits = {"apple", "banana", "tomato"}
    veggies = {"eggplant", "tomato"}
    print(fruits | veggies)
    print(fruits & veggies)
    print(fruits ^ veggies)
    print(fruits - veggies)
    print(bin(0b0001 ^ 0b1011))
    print((0b1011 >> 1))
    print(bin(set_bit(0b1011, 2)))
