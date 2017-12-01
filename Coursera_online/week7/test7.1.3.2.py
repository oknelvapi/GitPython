def make_list(s):
    return s.split()


fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
for s in fin:
    make_list(s)
