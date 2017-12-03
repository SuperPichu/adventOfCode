import hashlib
doorId = "cxdnnyjw"
#doorId = "abc"
index = 0
password = ['~','~','~','~','~','~','~','~']
positions = []
while '~' in password:
    m = hashlib.md5()
    m.update((doorId + str(index)).encode('utf-8'))
    checksum = m.hexdigest()
    if checksum.startswith('00000'):
        pos = checksum[5]
        ch = checksum[6]
        if pos not in positions and pos.isdigit() and int(pos) < 8:
            password[int(pos)] = ch
        positions.append(pos)
    index = index + 1
print(password)
