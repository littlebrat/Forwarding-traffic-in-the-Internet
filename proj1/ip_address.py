# converts an ip address in quad-doted format to it's decimal format
def quad_doted_to_decimal(ip_address):
    bytes = ip_address.split('.')
    address = 0
    for i in range(0, 3):
        address |= int(bytes[i])
        address <<= 8

    address |= int(bytes[3])
    return address


# converts an ip address in decimal format to quad-doted format
# it assumes that the ip_address is a decimal value of 32 bits
def decimal_to_quad_doted(ip_address):
    value = ip_address
    # add first byte value to the string
    quad_doted = str(value % 256)

    for i in range(1, 4):
        # move the next byte of the address to the least signifcant bits
        value >>= 8
        # add the next byte to the left of the string
        quad_doted = str(value % 256) + '.' + quad_doted

    return quad_doted


# converts an ip address in binary format to it's decimal format
def binary_to_decimal(ip_address):
    return int(ip_address, base=2)


# converts an ip address from decimal format to the binary format
def decimal_to_binary(ip_address):
    # start with empty string
    string = ''
    # convert decimal in to string with value in base 2
    decimal = ip_address
    while decimal != 0:
        string = str(decimal % 2) + string
        decimal = int(decimal / 2)

    # add 0s to the left of the string to account for the 0s with no value
    for i in range(len(string), 32):
        string = '0' + string

    return string

