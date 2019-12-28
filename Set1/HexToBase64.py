# expected input/output
in_ = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
out_ = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

# string of b64 characters, index of each character in string is the
# equivalent numerical value of the string in decimal
b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# pre: input must be a valid hexadecimal string
# post: outputs resulting b64 encoded string for input hex string
def hexToB64(in_):
    # to convert hexadecimal to b64, we note that a single hex digit 
    # can be encoded by a nibble (4 bits), while a single b64 digit
    # can be encoded by 6 bits, we can deduce from this that the representational
    # power of 6 hex digits is the equivalent of 4 b64 digits, and thus we can
    # convert each 6 bits of a hex string to a b64 string character

    out_ = []
    currentDigit = 0
    # we will add either 4 or 2 bits at a time when encoding to b64,
    # need to track the missingDigits at each step to know how many
    # digits we must still add
    missingDigits = 6
    for hexChar in reversed(in_):
        # convert digit of hex string to numerical value
        hexNum = int(hexChar, 16)
        # case 1: we have not included any hex bits in the current
        # base64 digit, in this case, we want to add all 4 bits of
        # the current hex digit, and set the missing digits to 2
        # as we are encoding groups of 6 bits
        if missingDigits == 6:
            currentDigit = hexNum
            missingDigits = 2
        # case 2: the previous hex character in the hex string has
        # been added to the currentDigit value, and thus we only need
        # the two remaining most significant bits to complete our
        # six bit b64 digit, we can apply the below bitwise operations
        # to get the two LSB of the current hex digit, and shift them to
        # be the 2 MSB of currentDigit
        elif missingDigits == 2:
            lastTwoBits = (hexNum & 0x3) << 4
            currentDigit += lastTwoBits
            # get the b64 character that represents the numerical value
            # of the six bits of the currentDigit
            out_.append(b64[currentDigit])
            # use remaining two MSB of the current hex character as the
            # two LSB of the next b64 numerical value
            currentDigit = (hexNum >> 2) & 0x3
            missingDigits = 4
        # case 3: the previous hex character was split up between the last
        # and current b64 digit, meaning that the 2 LSB of the current b64
        # digit have already been determined, we can now use all four 
        # bits of the current hex digit as the 4 MSB of the next b64 digit
        elif missingDigits == 4:
            lastFourBits = hexNum << 2
            currentDigit += lastFourBits
            out_.append(b64[currentDigit])
            currentDigit = 0
            missingDigits = 6
    
    # combine each b64 character into resulting output string
    return "".join(reversed(out_))

res = hexToB64(in_)
print("output value is:", res)
print("expected value is:", out_)
assert res == out_