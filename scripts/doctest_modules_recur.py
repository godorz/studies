#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Time: 2021-09-27 3:44 下午

Author: huayang

Subject: 递归对指定模块（指定文件夹下的所有模块）进行文档测试

Examples:
    >>> doctest_modules(r'../src/huaytools/python')
    0
    >>> doctest_modules([r'../src/huaytools/python', r'../huaytools/nlp'])
    0

    # 命令行调用
    >>> os.system('python doctest_modules_recur.py ../src')
    0

"""
import os
import sys
import doctest
import logging
import pkgutil
import importlib

from typing import *

from transformers.modeling_utils import logger  # noqa

logging.basicConfig(level=logging.ERROR)
logger.setLevel(logging.ERROR)

repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src_path = os.path.join(repo_path, 'src')
# sys.path.append(src_path)
# print(src_path)


def doctest_modules(paths: Union[str, List[str]]):
    """"""
    if isinstance(paths, list) and len(paths) == 1:
        paths = paths[0]

    if isinstance(paths, str):
        if os.path.exists(os.path.join(paths, '__init__.py')):
            paths = [paths]
        else:
            paths = [os.path.join(paths, fn) for fn in os.listdir(paths)]
            paths = [fp for fp in paths if os.path.isdir(fp) or fp.endswith('.py')]

    num_failed = 0
    for p in paths:
        # 示例：path = '../code'
        path = os.path.abspath(p)  # /Users/huayang/workspace/my/studies/code
        base = os.path.basename(path)  # code
        dir_path = os.path.dirname(path)  # /Users/huayang/workspace/my/studies

        # sys.path.append(path)  # 把自己添加到环境变量
        sys.path.append(dir_path)  # 把父目录添加到环境变量

        if os.path.isdir(path):
            tmp_failed = _doctest_module(path, base)
        else:
            file_name, ext = os.path.splitext(base)
            tmp_failed = _doctest_py(file_name)
        num_failed += tmp_failed

    return num_failed


def _doctest_py(module_name):
    """"""
    num_failed = 0
    module = importlib.import_module(module_name)
    if hasattr(module, 'doctest'):  # 如果该模块中使用了文档测试
        num_failed = doctest.testmod(module, optionflags=doctest.ELLIPSIS).failed
        if num_failed > 0:
            logging.error(f'=== `{module.__name__}` doctest failed! ===')

    return num_failed


def _doctest_module(path, base):
    """"""
    num_failed = 0
    for p, module_name, is_pkg in pkgutil.walk_packages([path], base + '.'):
        # print(path, module_name, is_pkg)
        num_failed += _doctest_py(module_name)

    return num_failed


def _test():
    """"""
    doctest.testmod()

    # code_path = r'../code'
    # n_failed = doctest_modules(code_path)
    # print(n_failed)


if __name__ == '__main__':
    """"""
    # sys.argv = 'code/scripts/doctest_modules_recur.py /Users/huayang/workspace/my/studies/code/my'.split()
    if len(sys.argv) > 1:
        # sys.stdout = open(os.devnull, 'w')
        pkg_path = sys.argv[1:]
        failed = doctest_modules(pkg_path)
        # sys.stdout = sys.__stdout__
    else:
        failed = doctest_modules(src_path)
        # _test()

        # 抑制标准输出，只打印 WARNING 信息
        # sys.stdout = open(os.devnull, 'w')
        # assert 0 == os.system('python doctest_modules_recur.py ../code')

    print(failed)
