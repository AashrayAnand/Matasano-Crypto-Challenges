from SingleByteXorCipher import XorTryAllKeys, evaluteOutputs

def DetectXor(out, file):

    text = [bytes.fromhex(line.strip()) for line in open("data.txt")]
    # get most likely byte-xor'd string for each hex output
    res = [evaluteOutputs(XorTryAllKeys(line)) for line in text]
    # for the most likely string for each hex output, get the most
    # likely string
    return sorted(res, key=lambda x: x[1], reverse=True)[0][0]

def main():
    res = DetectXor('data_out.txt', 'data.txt')
    assert res.decode().rstrip() == 'Now that the party is jumping'

if __name__ == '__main__':
    main()