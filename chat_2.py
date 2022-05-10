lines = []
with open('3.txt', 'r', encoding='utf-8-sig')as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    # print(s)
    print('时间：', s[0][:5], 'Name:', s[0][5:])
