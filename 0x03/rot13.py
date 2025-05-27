#!/usr/bin/python
"""a cryptography algorithm using rot-13"""

def rot_13(message):
    """
    A function that encode/decode any message to rot - 13
    equivalent 
    Arggs:
        message: a string of message
    return: Ecoded or Decoded message
    """
    info = ""
    for text in message:
        if 'a' <= text <= 'm' or 'A' <= text <= 'M':
            info += chr(ord(text) + 13)
        elif 'n' <= text <= 'z' or 'N' <= text <= 'z':
            info+= chr(ord(text) - 13)
        else:
            info+= text
    return info

if __name__ == "__main__":
    message = input("Enter a message to encode/decode: ")
    print("message:", '' .join(rot_13(message)))