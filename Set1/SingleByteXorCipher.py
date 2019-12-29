input = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ETAOINSHRDLU are the 12 most frequently
# used characters in the english language

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

def ByteXor(input):
    outputs = []
    output_i = []
    for char in alphabet:
        for byte in input:
            xor = char ^ byte
            xorChar = chr(xor)
            output_i.append(xorChar)
        res = "".join(output_i)
        outputs.append(res)
        output_i = []
    return evaluteOutputs(outputs)

def evaluteOutputs(outputs):
    scores = []
    for output in outputs:
        score = 0
        for char in output:
            if char in char_weights.keys():
                score += char_weights[char]
        score = score / len(output)
        scores.append(score)
    res = [x for x,y in sorted(zip(outputs, scores), key=lambda x: x[1], reverse=True)]
    return res[0]

res = ByteXor(input)
assert res == "Cooking MC's like a pound of bacon"