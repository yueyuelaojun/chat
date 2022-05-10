def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig')as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    allen_word_count = 0
    allen_sticker_count = 0  # 贴图
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)

        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen说了', allen_word_count, '传了', allen_sticker_count, '个贴图', '传了', allen_image_count, '个图片')
    print('Wiki说了', viki_word_count, '传了', viki_sticker_count, '个贴图', '传了', viki_image_count, '个图片')


def main():
    filename = "line.txt"
    lines = read_file(filename)
    convert(lines)


if __name__ == '__main__':
    main()
