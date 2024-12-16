def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='ascii', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

if __name__ =="__main__":
    
    with open(r"D:\kal\Untitled1.slx",'rb') as file:
    
        binars =file.read()
    
        
    with open('./decoded.xml', 'wb') as output:
        output.write(binars)
      
        output.close()