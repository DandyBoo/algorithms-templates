s = 'AAABJBKDLFHLELVFVLJLCJQOEUTUHIEJIPOWJJC'
d = {}
for i in range(256):
    d[i] = 0
for char in s:
    d[ord(char)] = d.get(ord(char), 0) + 1
for key, value in d.items():
    if value > 0:
        print(chr(key), end='')
