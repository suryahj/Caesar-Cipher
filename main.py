import tkinter as tk
from tkinter import messagebox
from tkinter import *
import decryption,encryption

class caesar_cipher():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("600x600")
        self.root.config(bg="#101539")
        #self.root.resizable(False,False)
        self.create_widgets()

    def create_widgets(self):
        title_l=Label(self.root, text="ENCRYPT USING CAESAR CIPHER",font=("Arial",20,"bold"), fg='#e74c3c', bg='#101539',justify=CENTER)
        title_l.pack(pady=5)

        # # Main game frame
        # main_frame = tk.Frame(self.root, bg='#101539')
        # main_frame.pack(expand=True, fill='both', padx=20, pady=10)

        def call_func(user_input,user_pass,rout):
            input_str = user_input.get()
            pass_key = user_pass.get()

            if int(pass_key)<0:
                messagebox.showerror("Invalid Key", "Please enter a +ve numeric key!")
                return
            if not pass_key.isdigit():
                messagebox.showerror("Invalid Key", "Please enter a numeric key!")
                return
            
            if rout == 0:
                tk.messagebox.showinfo("Your encrypted string", encryption.encrypt(input_str, pass_key))
            else:
                tk.messagebox.showinfo("Your decrypted string", decryption.decrypt(input_str, pass_key))
            
            # Clear the inputs
            user_input.set("")
            user_pass.set("")

################################################################################################################################################

        # Left side - ENCRYPTION
        left_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=2, width=250)
        left_frame.pack(side='left', fill="both", expand=True, padx=(10, 10) ,pady=(0,5))
        encrypt_title_l=Label(left_frame, text="ENCRYPTION",font=("Arial",15,"bold"), fg='#75ccee',bg='#34495e')
        encrypt_title_l.pack(pady=1)

        # user input for encryption
        user_input_en=StringVar()
        input_text_l=Label(left_frame, text="Enter the String :",font=("Arial",12), fg='#75ccee',bg='#34495e',justify=LEFT)
        input_text_l.place(y=50)
        input_l=Entry(left_frame, font=("corbel",10), textvariable=user_input_en,bd=2)
        input_l.place(y=50,x=120)

        #user pass input for encryption
        user_pass_en=StringVar()
        input_pass_l=Label(left_frame, text="Enter the key :",font=("Arial",12), fg='#75ccee',bg='#34495e',justify=LEFT)
        input_pass_l.place(y=100)
        input_l=Entry(left_frame, font=("corbel",10), textvariable=user_pass_en,bd=2)
        input_l.place(y=100,x=120)

        #button for submit
        b1_submit=Button(left_frame,text="ENTER" ,font=("Arial",12,"bold"), bg="#4d53a3", fg="#db949c",command=lambda: call_func(user_input_en,user_pass_en,0))
        b1_submit.pack(pady=120)

############################################################################################################################################

        # Right side - DECRYPTION
        right_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=2)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 10) , pady=(0,5))
        decrypt_title_l=Label(right_frame, text="DECRYPTION",font=("Arial",15,"bold"), fg='#75ccee' , bg='#34495e')
        decrypt_title_l.pack(pady=1)


        # user input for decryption
        user_input=StringVar()
        input_text_l=Label(right_frame, text="Enter the String :",font=("Arial",12), fg='#75ccee',bg='#34495e',justify=LEFT)
        input_text_l.place(y=50)
        input_l=Entry(right_frame, font=("corbel",10), textvariable=user_input,bd=2)
        input_l.place(y=50,x=120)

        #user pass input for decryption
        user_pass=StringVar()
        input_pass_l=Label(right_frame, text="Enter the key :",font=("Arial",12), fg='#75ccee',bg='#34495e',justify=LEFT)
        input_pass_l.place(y=100)
        input_l=Entry(right_frame, font=("corbel",10), textvariable=user_pass,bd=2)
        input_l.place(y=100,x=120)

        #button for submit
        b_submit=Button(right_frame,text="ENTER" ,font=("Arial",12,"bold"), bg="#4d53a3", fg="#db949c",command=lambda: call_func(user_input,user_pass,1))
        b_submit.pack(pady=120)

##################################################################################################################################################

def main():
    root=Tk()
    caesar_cipher(root)
    root.mainloop()

if __name__=="__main__":
    print("encryption.encrypt exists?", hasattr(encryption, 'encrypt'))
    main()

