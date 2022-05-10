data = []
count = 0
with open('reviews.txt', 'r')as f:
    for line in f:
        data.append(line)
        count += 1
# print('档案读取完成，总共有', len(data), '笔资料！')
wc = {}
for d in data:
    words = d.split()  # 里面不写，就是用空格分隔，不会出现多个空格的空字符串
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  # 新增Key

# for word in wc:
#    if(wc[word])>100:
#        print(word, wc[word])
# print(len(wc))
while True:
    word = input('请问你查什么字？')
    if word == 'q':
        break
    elif word in wc:
        print(word, "出现过得次数", wc[word])
    else:
        print('这个字没有出现过！')
print('感谢使用本查询')
