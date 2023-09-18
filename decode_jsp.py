import os
import encodings
import re
import argparse

def unideco(inputfile, outputfile):
    with open(inputfile, encoding='utf-8') as readfile:
        textline = readfile.read()
        textline = re.sub(r"\\u+", r"\\u", textline)
        decode_str = textline.encode('utf-8').decode('unicode_escape')
    with open(outputfile, 'w', encoding='utf-8') as writefile:
        writefile.write(str(decode_str))
        writefile.close()

parser = argparse.ArgumentParser(description='To decode a string with escaped Unicode')
parser.add_argument('--inputfile', '-i', help='原始文件，请使用绝对路径')
parser.add_argument('--outputfile', '-o', help='解码后文件，请使用绝对路径，默认在当前目录下生成output.txt', default='output.txt')
args = parser.parse_args()

if __name__ == '__main__':
    try:
        unideco(args.inputfile, args.outputfile)
    except Exception as e:
        print(e)



