input = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ETAOINSHRDLU are the 12 most frequently
# used characters in the english language

# use ocurrences of each letter in output of each
# XOR to determine character which will give expected output
char_weights = {'e': 0.1041442, 
                't': 0.1041442,
                'a': 0.0651738,
                'o': 0.0596302,
                'i': 0.0558094,
                'n': 0.0564513,
                's': 0.0515760,
                'h': 0.0492888,
                'r': 0.0497563,
                'd': 0.0349835,
                'l': 0.0331490,
                'u': 0.0225134}

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
        print(res)
        output_i = []
    evaluteOutputs(outputs)

def evaluteOutputs(outputs):
    scores = []
    for output in outputs:
        score = 0
        for char in output:
            if char in char_weights.keys():
                score += char_weights[char]
        score = score / len(output)
        scores.append(score)
    res = [x for x,_ in sorted(zip(outputs, scores))]
    print(res[0:5])

ByteXor(input)