from enum import Enum


class Format(Enum):
    quad_doted = 1
    binary = 2
    decimal = 3


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


# converts any decimal integer to binary representation
def _decimal_to_binary(decimal_number, length=-1):
    # start with empty string
    binary = ''

    decimal = int(decimal_number)
    while decimal != 0:
        binary = str(decimal % 2) + binary
        decimal = int(decimal / 2)

    # add 0s to the left of the binary representation to guarantee the needed length
    for i in range(len(binary), length):
        binary = '0' + binary

    return binary


# converts an ip address from decimal format to the binary format
def decimal_to_binary(ip_address):
    return _decimal_to_binary(ip_address, length=32)


def quad_doted_to_binary(ip_address):
    binary = ''
    for byte in ip_address.split('.'):
        # convert byte decimal value to it's binary representation
        binary += _decimal_to_binary(byte, length=8)

    return binary


def binary_to_quad_doted(ip_address):
    quad_doted = ''
    # for each byte in the binary ip address
    for i in range(0, 24, 8):
        byte = ip_address[i:i + 8]
        quad_doted += str(int(byte, base=2)) + '.'

    # don't include the '.' in the last byte
    byte = ip_address[24:32]
    quad_doted += str(int(byte, base=2))

    return quad_doted


def to_binary(ip_address, format):
    if format is ip.Format.quad_doted:
        binary_address = ip.quad_doted_to_binary(ip_address)
    elif format is ip.Format.decimal:
        binary_address = ip.decimal_to_binary(ip_address)
    elif format is ip.Format.binary:
        binary_address = ip_address
    else:
        raise Exception("invalid ip address format")

    return binary_address
