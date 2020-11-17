from pwn import *

def myStrat(color):
        if 'red' in color:
                return 'yellow\n'
        if 'yellow' in color:
                return 'blue\n'
        if 'blue' in color:
                return 'red\n'

def myStrat2(color):
        if 'red' in color:
                return 'blue\n'
        if 'yellow' in color:
                return 'red\n'
        if 'blue' in color:
                return 'yellow\n'

def myStrat3(color):
        if 'red' in color:
                return b'yellow\n'
        if 'yellow' in color:
                return b'blue\n'
        if 'blue' in color:
                return b'green\n'
        if 'green' in color:
                return b'red\n'

def myStrat4(color):
        if 'red' in color:
                return b'yellow\n'
        if 'yellow' in color:
                return b'blue\n'
        if 'blue' in color:
                return b'red\n'
        if 'green' in color:
                return b'yellow\n'

conn = remote('35.242.192.203',30769)


conn.recvuntil(b'Should we start?')
conn.send('\n')
conn.recvuntil(b'Ok?')
conn.send('\n')
conn.recvuntil(b'Ok?')
conn.send('\n')
conn.recvuntil(b'Ok?')
conn.send('\n')

for x in range(101):
	conn.recvuntil(b'I am chosing')
	color = conn.recvline()
	payload = myStrat(color)
	conn.send(payload)


for x in range(101):
	conn.recvuntil(b'I am chosing')
	color = conn.recvline()
	payload = myStrat2(color)
	conn.send(payload)

conn.recvuntil(b'Ok?')
conn.send('\n')
conn.recvuntil(b'Ok?')
conn.send('\n')
conn.recvuntil(b'Ok?')
conn.send('\n')
conn.recvuntil(b'Ok?')
conn.send('\n')

for x in range(101):
	conn.recvuntil(b'I am chosing')
	color = conn.recvline()
	payload = myStrat3(color)
	conn.send(payload)


for x in range(101):
	conn.recvuntil(b'I am chosing')
	color = conn.recvline()
	payload = myStrat4(color)
	conn.send(payload)

conn.interactive()
