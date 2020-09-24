from tkinter import *
from tkinter import messagebox
import os
import sys
from random import shuffle
from string import printable

py = sys.executable
Devanagari_alphabets = ["ै", "ौ", "ृ", "ु", "ू", "ि", "ी", "ो", "ा", "े", "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ",
                        "ण", "त", "थ", "द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "स", "श", "ष", "ह",
                        "ञ"]
English_alphabets = list(printable)

# GUI
root = Tk()
root.title("INDIVIDUAL PROJECT WORK")
root.geometry('400x400')
root.resizable(width=False, height=False)
color = '#20c997'
root.configure(bg=color)


def get_value_encrypt():
    msg = enter.get("1.0", 'end-1c')
    output.insert("1.0", encrypt(msg))


def get_value_decrypt():
    msg = output.get("1.0", 'end-1c')
    output1.insert("1.0", decrypt(msg))


def get_clear():
    enter.delete("1.0", END)
    output.delete("1.0", END)
    output1.delete("1.0", END)


# Maps for Devanagari_alphabets
keys_devanagari = list(Devanagari_alphabets)
shuffled_keys_devanagari = list(Devanagari_alphabets)
shuffle(shuffled_keys_devanagari)

# Maps for English_alphabets
keys_english = list(English_alphabets)
shuffled_keys_english = list(English_alphabets)
shuffle(shuffled_keys_english)

# dict for Devanagari_alphabets maps
maps_devanagari = dict(zip(keys_devanagari, shuffled_keys_devanagari))
reversed_maps_devanagari = dict(zip(shuffled_keys_devanagari, keys_devanagari))

# dict for English_alphabets maps
maps_english = dict(zip(keys_english, shuffled_keys_english))
reversed_maps_english = dict(zip(shuffled_keys_english, keys_english))


def encrypt(message):
    cipher = []
    for alphabets in message:
        if alphabets in Devanagari_alphabets:
            cipher_devanagari = maps_devanagari[alphabets]
            cipher.append(cipher_devanagari)
        elif alphabets in English_alphabets:
            cipher_english = maps_english[alphabets]
            cipher.append(cipher_english)
    return "".join(cipher)


def decrypt(ciphers):
    plaintext = []
    for alphabets in ciphers:
        if alphabets in Devanagari_alphabets:
            plaintext_devanagari = reversed_maps_devanagari[alphabets]
            plaintext.append(plaintext_devanagari)
        elif alphabets in English_alphabets:
            plaintext_english = reversed_maps_english[alphabets]
            plaintext.append(plaintext_english)
    return "".join(plaintext)


def log():
    conf = messagebox.askyesno("Confirm", "Are you sure you want to quit?")
    if conf:
        root.destroy()
        os.system('%s %s' % (py, 'main.py'))


def add_user():
    os.system('%s %s' % (py, 'addUser.py'))


def rem_user():
    os.system('%s %s' % (py, 'removeUser.py'))


menubar = Menu(root)
menubar.add_command(label="Add User", command=add_user)
menubar.add_command(label="Remove User", command=rem_user)
menubar.add_command(label="Exit", command=log)
root.config(menu=menubar)

label_heading = Label(root, text="Mono Alphabetic Cipher", font=("Helvetica Neue", 20, 'bold'), bg="#17a2b8",
                      fg='#f8f9fa')
label_heading.place(x=40, y=15)

label_entry = Label(root, text="Plain Text:", font=("Helvetica Neue", 14, 'bold'), bg=color, fg='black')
label_entry.place(x=40, y=80)

enter = Text(root, height=2, width=20)
enter.place(x=160, y=75)

label_output = Label(root, text="Encrypted Text", font=("Helvetica Neue", 14, 'bold'), bg=color, fg='black')
label_output.place(x=25, y=135)

output = Text(root, height=8, width=20)
output.place(x=20, y=165)

label_output1 = Label(root, text="Decrypted Text", font=("Helvetica Neue", 14, 'bold'), bg=color, fg='black')
label_output1.place(x=215, y=135)

output1 = Text(root, height=8, width=20)
output1.place(x=210, y=165)

button = Button(root, text="Encrypt", bg='#28a745', fg='#f9f9f9', command=lambda: get_value_encrypt(), width=10,
                height=2,
                font=("Helvetica Neue", 12, 'bold'))
button.place(x=25, y=325)

button1 = Button(root, text="Decrypt", bg='#28a745', fg='#f9f9f9', command=lambda: get_value_decrypt(), width=10,
                 height=2,
                 font=("Helvetica Neue", 12, 'bold'))
button1.place(x=145, y=325)

button_clear = Button(root, text="Clear", bg='#ffc107', fg='#f9f9f9', command=lambda: get_clear(), width=10, height=2,
                      font=("Helvetica Neue", 12, 'bold'))
button_clear.place(x=265, y=325)

# a=encrypt("मेरो देश नेपाल हो!, I'm kunja!")
# print("Encrypted Letters is: ",a)
# b=decrypt(a)
# print("Decrypted Letters is:",b)

root.mainloop()