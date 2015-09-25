
class Prefix:

    def __init__(self, bits, format='str'):
        if format is 'str':
            # bits in string format
            if len(bits) > 32:
                raise Exception("the string of bits is too long")

            self.length = len(bits)
            self.bits = int(bits, base=2)
        else:
            # unsupported format
            raise Exception("unsupported prefix input format")

    def __iter__(self):
        self.iterations = 0
        return self

    def __next__(self):
        if self.iterations >= self.length:
            raise StopIteration()

        # get the next bit based on the number of iterations
        bit = self.bits & 2**(self.length - self.iterations - 1)
        bit >>= self.length - self.iterations - 1
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