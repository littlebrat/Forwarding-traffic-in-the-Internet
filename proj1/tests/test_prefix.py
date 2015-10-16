from prefix import Prefix

prefix = Prefix("000110101")
print(prefix)

for bit in prefix:
    print(bit, end='')
print()

prefix.set(0)
print(prefix)
prefix.unset(0)
print(prefix)
