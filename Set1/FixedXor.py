x  = "1c0111001f010100061a024b53535009181c"
y = "686974207468652062756c6c277320657965"
out = "746865206b696420646f6e277420706c6179"

# string of hex digits, index of each digit is the
# equivalent decimal value of the digit
hex = "0123456789abcdef"

def FixedXor(x, y):
    output = []
    for i in range(len(x)):
        # get ith hex digit of each input
        xi = x[i]
        yi = y[i]

        # get decimal values for each hex digit
        xn = int(xi, 16)
        yn = int(yi, 16)

        # apply Xor to the digits from each number
        xor = xn ^ yn

        # get hex character that corresponds 
        # to the decimal xor result, add to
        # the list of characters
        output.append(hex[xor])
    return "".join(output)

res = FixedXor(x, y)
print("output value is:", res)
print("expected value is:", out)
assert res == out