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


