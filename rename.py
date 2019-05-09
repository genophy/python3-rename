#!/usr/local/bin/python3
# -*- utf-8 -*-


import os
import re

''' 
获取正则表达式文件列表
'''


def get_reg_file_list(ori_txt, _rep_string):
    _file_maps = []
    # 列出目录下所有文件和目录
    for file in os.listdir('.'):
        # 判断是否为文件，且通过正则搜索到该文件
        # re.search(ori_txt, file)若未搜索到，则值为None
        if os.path.isfile(file) and re.search(ori_txt, file):
            # 使用正则进行文本替换
            new_file = re.sub(ori_txt, _rep_string, file)
            # 追究追加到文件map中
            _file_maps.append({
                'old_file': file,
                'new_file': new_file
            })

            print(file, '\t->\t', new_file)
    return _file_maps


'''
获取正常的文件列表
'''


def get_normal_file_list(ori_txt, _rep_string):
    _file_maps = []
    # 列出目录下所有文件和目录
    for file in os.listdir('.'):
        # 判断是否为文件，且通过文件名字符串搜索
        if os.path.isfile(file) and file.find(ori_txt) > -1:
            # 使用普通文本替换
            new_file = file.replace(ori_txt, _rep_string)
            # 追究追加到文件map中
            _file_maps.append({
                'old_file': file,
                'new_file': new_file
            })

            print(file, '\t->\t', new_file)
    return _file_maps


'''
初始化文件
'''


def init_file():
    _ori_txt = input('需要批量替换的字符:[默认为空]')
    _rep_string = input('替换成什么字符串:[默认为空]')
    _is_reg = input('是否是正则表达式:[y/N]')

    # 是否采用正则表达式
    if _is_reg:
        _file_maps = get_reg_file_list(_ori_txt, _rep_string)

    else:
        _file_maps = get_normal_file_list(_ori_txt, _rep_string)

    return _file_maps


'''
主方法
'''
if __name__ == '__main__':

    file_maps = init_file()
    # 若已经匹配到了文件， 则询问用户是否真的要进行重命名操作
    if len(file_maps) > 0:
        if input('\n确定重命名?[y/N] : ').lower() == 'y':
            for i in file_maps:
                # os的重命名操作
                os.rename(i['old_file'], i['new_file'])
                print('更名成功: ', i['old_file'], '\t->\t', i['new_file'])
            print('-- 所有文件，重命名结束 --')
        else:
            print('-- 用户取消操作 -- \n')
    else:
        print('-- 未匹配到需要批量重命名的文件 -- \n')
