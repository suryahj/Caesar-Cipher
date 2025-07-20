def decrypt(user_input,pass_key):
    output_str=""
    for i in user_input:
        o_ind=ord(i)
        en_ind=(o_ind-int(pass_key))
        if en_ind<32:
            output_str+=chr(128-(32-en_ind))
        else:
            output_str+=chr(en_ind)
    return output_str

if __name__=="__main__":
    s="cde"
    p=2
    print(decrypt(s,p))