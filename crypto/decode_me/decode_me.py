import cryptography.fernet
import base64

filename = "Decode.txt"
with open(filename, "r") as f:
    key, msg = tuple([x.encode() for x in f.read().split('\n\n')])

f = cryptography.fernet.Fernet(key)

msg_decoded = f.decrypt(msg)
msg_decoded = base64.decodebytes(msg_decoded).decode()

print("*****************************************")
print("*****************************************")
print('[1] Go to https://zb3.me/malbolge-tools/')
print('[2] Select Crackme by zb3')
print('[3] Decode this :')
print(msg_decoded)
print("*****************************************")
print("**********************************PABlond")