import sys
script,encoding,errors=sys.argv     #命令行参数处理


def main(language_file,encoding,errors):
    line=language_file.readline()       #用readline()处理文本

    if line:
        print_line(line,encoding,errors)        #防止函数永远循环下去
        return main(language_file,encoding,errors)


def print_line(line,encoding,errors):       #对langusges.txt中每一行字符进行编码
    next_lang=line.strip()              #移除头尾空格
    raw_bytes=next_lang.encode(encoding,errors=errors)
    cooked_string=raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes,"<===>",cooked_string)


languages=open("languages.txt",encoding="utf-8")

main(languages,encoding,errors)