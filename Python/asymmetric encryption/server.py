import random
import pickle
import socket

def Cenc(mes, k):
    return [chr((ord(i) + k)%65536)for i in mes]

def Cdec(mes, k):
    return [chr((65536 + (ord(i) - k) % 65536) % 65536) for i in mes]

class Cryptographer:
    def __init__(self, g=10, p=5, rmin=1, rmax=10):
        self.g = g
        self.p = p
        self.secret_key = random.randint(rmin, rmax)

    def CreateOpenKey(self):
        '''Создает секретный ключ'''
        self.open_key = self.g ** self.secret_key % self.p
        return self.open_key, self.g, self.p

    def Decrypt(self, B):
        '''Получает общий секретный ключ K'''
        return B ** self.secret_key % self.p

    def CreateSharedKey(self, A, g, p):
        '''Получает внешний открытый ключ, создает свой открытый ключ, а также обший секретный'''
        return g ** self.secret_key % p, A ** self.secret_key % p

Cr = Cryptographer()
sock = socket.socket()

sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

data = conn.recv(1024)
data = pickle.loads(data)
if data[0] == 'open_key':
    OpenKey = data[1]
(B, K) = Cr.CreateSharedKey(*OpenKey)
SharedKeyClient = K
conn.send(pickle.dumps(["open_key", Cr.CreateOpenKey(), B]))


while True:
    data = conn.recv(1024)
    data = pickle.loads(data)
    K = Cr.Decrypt(data[2])
    mesin = data[1]
    mesin = 'Client: '+''.join(Cdec(Cdec(mesin, K), SharedKeyClient))
    print(mesin)
    if "exit" in mesin.lower():
        conn.close()
        exit()

    mesout = input('>')
    print("---")
    data = ["messeg", Cenc(Cenc(mesout, K), SharedKeyClient)]

    conn.send(pickle.dumps(data))

    if "exit" in mesout.lower():
        conn.close()
        exit()
