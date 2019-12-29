from SingleByteXorCipher import ByteXor, evaluteOutputs

def DetectXor(out, file):
    # get text hex and convert to bytes
    text = [bytes.fromhex(line.strip()) for line in open(file)]
    
    # evaluate and get most likely single char xor'd string for each
    # hex string

    res = [evaluteOutputs(ByteXor(line)) for line in text]
    print(res[0])
    with open(out, 'w') as f:
        f.writelines(res)

def main():
    DetectXor('data_out.txt', 'data.txt')

if __name__ == '__main__':
    main()