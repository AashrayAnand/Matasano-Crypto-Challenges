
alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# use ocurrences of each letter in output of each
# XOR to determine character which will give expected output
char_weights = {
    'a': 0.0651738,
    'b': 0.0124248, 
    'c': 0.0217339, 
    'd': 0.0349835, 
    'e': 0.1041442, 
    'f': 0.0197881, 
    'g': 0.0158610,
    'h': 0.0492888, 
    'i': 0.0558094, 
    'j': 0.0009033, 
    'k': 0.0050529, 
    'l': 0.0331490, 
    'm': 0.0202124, 
    'n': 0.0564513,
    'o': 0.0596302, 
    'p': 0.0137645, 
    'q': 0.0008606, 
    'r': 0.0497563, 
    's': 0.0515760, 
    't': 0.0729357, 
    'u': 0.0225134,
    'v': 0.0082903, 
    'w': 0.0171272, 
    'x': 0.0013692, 
    'y': 0.0145984, 
    'z': 0.0007836, 
    ' ': 0.1918182
}

def XorTryAllKeys(input):
    outputs = []
    for char in range(256):
        outputs.append(SingleCharXor(input, char))
    return outputs

# apply single byte xor to given input with a specified character
def SingleCharXor(input, char):
    output = b''
    for byte in input:
        xor = char ^ byte
        xorChar = bytes([xor])
        output += xorChar
    return output

# get the char. frequency score for a given string
def getScore(output):
    score = 0
    for byte in output:
        char = chr(byte).lower()
        score += char_weights.get(char, 0)
    return score

# given a list of potential byte-xor'd strings, return the 
# one that quantitatively is the highest quality string
# by character frequency
def evaluteOutputs(outputs):
    scores = []
    for output in outputs:
        scores.append(getScore(output))
    res = [(x, y) for x,y in sorted(zip(outputs, scores), key=lambda x: x[1], reverse=True)]
    return res[0]

def main():
    line = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    res = XorTryAllKeys(line)
    out = evaluteOutputs(res)
    assert out[0].decode().rstrip() == "Cooking MC's like a pound of bacon"

if __name__ == '__main__':
    main()