
class Prefix:

    def __init__(self, bits, format='str'):
        if format is 'str':
            # bits in string format
            if len(bits) > 32:
                raise Exception("the string of bits is too long")

            if len(bits) == 0:
                # empty prefix
                self.length = 0
                self.bits = 0
            else:
                self.length = len(bits)
                self.bits = int(bits, base=2)
        else:
            # unsupported format
            raise Exception("unsupported prefix input format")

    def get(self, bit_position):
        bit = self.bits & 2**(self.length - bit_position - 1)
        bit >>= self.length - bit_position - 1
        return bit

    def set(self, bit_position):
        self.bits |= 2 ** (self.length - bit_position - 1)

    def unset(self, bit_position):
        self.bits &= ~(2 ** (self.length - bit_position - 1))

    def length(self):
        return self.length

    def __iter__(self):
        self.iterations = 0
        return self

    def __next__(self):
        if self.iterations >= self.length:
            raise StopIteration()

        # get the next bit based on the number of iterations
        bit = self.get(self.iterations)

        # increase iteration count
        self.iterations += 1

        return bit

    def __str__(self):
        # start with empty string
        string = ''

        # convert decimal in to string with value in base 2
        decimal = self.bits
        while decimal != 0:
            string = str(decimal % 2) + string
            decimal = int(decimal / 2)

        # add 0s to the left of the string to account for the 0s with no value
        for i in range(len(string), self.length):
            string = '0' + string

        return string
