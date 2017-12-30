#!/usr/bin/python3

import sys
import os
import fileinput


def isalp(a):
    """
    判断是否为ASCII码
    ord()用于将字符a转换整数
    """
    if (ord(a) < 128):
        return True
    else:
        return False


def split_EN_CN(i_contents):
    '''
    内容分离
    '''
    flag = 0  # 0-英文；1-中文
    o_contents=['1']
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
                o_contents.append('@')
                flag = 1
        o_contents.append(str)

    return ''.join(o_contents)


def main():
    # 获取文件名
    filename = sys.argv[1]
    mode = sys.argv[2]
    input = open(filename)
    i_contents = input.read()
    i_contents = i_contents.replace('\t', '')

    outfilename = os.path.splitext(filename)[0] + '_OUTPUT' + '.txt'
    output = open(outfilename, 'w')

    # mode = 1中-英; 其他英-中
    if(mode == '1'):
        i_contents = i_contents[::-1]

    s_contents = split_EN_CN(i_contents)

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
