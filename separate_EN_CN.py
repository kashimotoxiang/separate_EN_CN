#!/usr/bin/python3

import sys
import os
import fileinput
import re


def isalp(a):
    """
    判断是否为ASCII码
    ord()用于将字符a转换整数
    """
    if (ord(a) < 128):
        return True
    else:
        return False


def separate(i_contents):
    '''
    内容分离
    '''
    flag = 0  # 0-英文；1-中文
    o_contents = ['']
    for i in range(0, len(i_contents)):
        str = i_contents[i]

        # 中文
        # 等待换行
        if flag == 1:
            if str == '\n':
                flag = 0

        # 英文
        else:
            if not isalp(str):
                o_contents.append('\t')
                flag = 1
        o_contents.append(str)

    return ''.join(o_contents)


def is_up_case_and_symbol(ch):
    '''
    判断是否为大写字母
    '''
    if(((ch >= "A")& (ch <= "Z"))
        | (ch == '.')| (ch == '-')):
        return True
    else:
        return False


def auto_up_down_case(contents, mode):
    '''
    智能大小写转换
    全大写的缩写词保持不变
    一般单词的首字母变成小写
    '''
    # mode = 1中-英; 其他英-中
    if(mode == 1):
        index = 1
    else:
        index = 0

    o_contents = ['']

    try:
        contents = contents.split("\n")
        for line in contents:
            words = line.split("\t")
            if (len(words)!=2):
                continue
            if(mode == 1):
                cn = words[0][::-1]
                en = words[1][::-1]
            else:
                cn = words[1]
                en = words[0]

            first_letter = en[0]
            second_letter = en[1]

            if (is_up_case_and_symbol(first_letter) & ~is_up_case_and_symbol(second_letter)):
                en = en.lower()

            #文档错误修复
            def _fix_error(str,i,ch):
                if(str[i]==ch):
                    return True
                else:
                    return False

            if(_fix_error(en,-1,'(')):
                en=en[0:-1]
                cn='('+cn

            if(_fix_error(en, -1, '-')):
                en = en[0:-1]

            o_contents.append(en)
            o_contents.append('\t')
            o_contents.append(cn)
            o_contents.append('\n')
    except IndexError:
        print ("auto_up_down_case NameError")

    return ''.join(o_contents)


def main():
    # 获取文件名
    filename = sys.argv[1]
    mode = sys.argv[2]
    input = open(filename)
    i_contents = input.read()

    # 清洗文件
    i_contents = i_contents.replace('\t', '')
    i_contents = i_contents.replace('  ', ' ')

    # 删除多余空行
    rep = re.compile("\n{2,}")
    i_contents = re.sub(rep, '\n', i_contents)

    outfilename = os.path.splitext(filename)[0] + '_OUTPUT' + '.txt'
    output = open(outfilename, 'w')

    # mode = 1中-英; 其他英-中
    if(mode == '1'):
        i_contents = i_contents[::-1]

    s_contents = separate(i_contents)

    # 删除无效行
    rep = re.compile("\n\t.*")
    s_contents = re.sub(rep, '\n', s_contents)

    # 删除多余空行
    rep = re.compile("\n{2,}")
    i_contents = re.sub(rep, '\n', i_contents)

    # 智能大小写转换
    s_contents = auto_up_down_case(s_contents, mode)

    # 保存结果
    if(mode == '1'):
        o_contents = s_contents[::-1]
    else:
        o_contents = s_contents

    output.write(o_contents)

    # 关闭文件
    input.close()
    output.close()


if __name__ == "__main__":
    main()
