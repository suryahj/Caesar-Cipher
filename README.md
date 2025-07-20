# 🔐 Caesar Cipher – Python GUI Encryption-Decryption Tool

A modern take on the **Caesar Cipher** encryption method using **Python**.  
Includes a user-friendly **Tkinter-based GUI** to **encrypt and decrypt messages** with a numeric key.

---

## 📚 Index

1. [📌 About the Project](#-about-the-project)  
2. [🧠 Core Logic](#-core-logic)  
3. [📂 Project Structure](#-project-structure)  
4. [🧮 Data Structures Used](#-data-structures-used)  
5. [🪜 Encryption & Decryption Algorithms](#-encryption--decryption-algorithms)  
6. [🖼️ GUI Design Overview](#-gui-design-overview)  
7. [📈 Enhancements Ideas](#-enhancements-ideas)  
8. [🤖 AI Assistance](#-ai-assistance)  
9. [📝 License](#-license)  
10. [🙋‍♂️ Author](#-author)

---

## 📌 About the Project

This project brings the ancient **Caesar Cipher** technique to life with:
- **Encryption**: Shifting characters forward based on a key.
- **Decryption**: Reversing the shift using the same key.
- A **GUI interface** to interact easily without needing the terminal.

The goal is to **demonstrate encryption-decryption basics** using simple modular Python logic and a visual interface.

---

## 🧠 Core Logic

The Caesar Cipher works by shifting the Unicode value of each character by a certain number of positions (the key).  
This project ensures:
- Printable characters are preserved (ASCII 32 to 126).
- Only **positive integers** are accepted as keys.
- Inputs are dynamically cleared post action.

---

## 📂 Project Structure

| File Name        | Description                                       |
|------------------|---------------------------------------------------|
| `main.py`        | Tkinter-based GUI with both encryption & decryption UI |
| `encryption.py`  | Contains the Caesar cipher encryption logic       |
| `decryption.py`  | Contains the decryption logic (reverse Caesar cipher) |

---

## 🧮 Data Structures Used

| Type     | Purpose                                                         |
|----------|-----------------------------------------------------------------|
| `str`    | To iterate characters in input and build output                 |
| `int`    | Used for the shift (key) and ASCII manipulation                 |
| `tk.StringVar` | Stores live input from Tkinter `Entry` widgets         |

---

## 🪜 Encryption & Decryption Algorithms

### 🔒 Encryption Logic

```python
def encrypt(user_input, pass_key):
    output_str = ""
    for i in user_input:
        o_ind = ord(i)
        en_ind = (o_ind + int(pass_key)) % 127
        if en_ind < 32:
            en_ind = 31 + en_ind
        output_str += chr(en_ind)
    return output_str
Shifts each character forward by the key.

Wraps back if it goes beyond printable range.

🔓 Decryption Logic
python
Copy
Edit
def decrypt(user_input, pass_key):
    output_str = ""
    for i in user_input:
        o_ind = ord(i)
        en_ind = (o_ind - int(pass_key))
        if en_ind < 32:
            en_ind = 32 - en_ind
            output_str += chr(128 - en_ind)
        else:
            output_str += chr(en_ind)
    return output_str
Reverses the shift.

Handles wrap-around for printable character range (ASCII 32–126).

⚠️ Note: This logic assumes the same key is used for both operations.

🖼️ GUI Design Overview
💡 Technologies:
tkinter

messagebox (pop-up alerts)

Entry, Label, Button, Frame widgets

🧱 Layout Breakdown
Section	Purpose
Left Panel	🔐 Encrypt Section – Input string + key
Right Panel	🔓 Decrypt Section – Encrypted string + key
Message Boxes	Show the result of encryption/decryption
Styling	Dark-themed background with accent color buttons

🧼 Auto Clear Feature:
Each action (Encrypt/Decrypt) clears the inputs automatically for next use.

📈 Enhancements Ideas
Add key validation for non-integer inputs.

Export encrypted/decrypted results to a text file.

Add theme switcher (dark/light mode).

Add history of past encrypted messages.

Option to copy result to clipboard.

🤖 AI Assistance
While all logic and implementation were authored by Suryanath Tripathy, AI tools such as ChatGPT assisted in:

Refactoring code

Optimizing encryption wrap logic

GUI design decisions

📝 License
This project is open-source.
Please refer to the LICENSE file for license details.

🙋‍♂️ Author
Made with 🧠 + ❤️ by SURYANATH TRIPATHY

💬 Connect, fork, suggest or build something awesome on top of this.