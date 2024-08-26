"""
author : 胡澄宇
data   : 2024-08-26
"""

import os
from log import downloadInfo
from pathspecification import pathSpecification 
import pandas as pd


def datasetLoading(path):
    # 格式化路径
    path = pathSpecification(path)
    # 判断文件是否存在并获取文件路径
    if os.path.exists(path):
        downloadInfo(path,para=1)
        return True
    else:
        downloadInfo(path,para=0)
        return Flase

if __name__ == "__main__":
    path = 'D:\\school\\Daily\\Comsume\\Comsume.xlsx'
    if datasetLoading(path):
        dataframe = pd.read_excel(path)
        downloadInfo(path,para=-1)
    else: # TODO：当转化为Web应用防止地址错误，提供在死循环下的重复输入。正确后跳过 
        pass