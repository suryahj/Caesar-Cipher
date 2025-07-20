def encrypt(user_input,pass_key):
    output_str=""
    for i in user_input:
        o_ind=ord(i)
        en_ind=(o_ind+int(pass_key)) % 127
        if en_ind<32:
            en_ind=31+en_ind
        output_str+=chr(en_ind)
    return output_str

if __name__=="__main__":
    s="cde"
    p=2
    print(encrypt(s,p))