"""
author : 胡澄宇
data   : 2024-08-26
"""

import logging
import re
 
def extract_filename_from_path(path):
    # 正则表达式匹配绝对路径，并捕获文件名
    filename_pattern = re.compile(r'.*[/\\](.*)$')
    match = filename_pattern.match(path)
    if match:
        return match.group(1)
    else:
        return None
 

def downloadInfo(path,para):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
         
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
         
    handler_file = logging.FileHandler('log_file.log')
    handler_file.setLevel(logging.DEBUG)
         
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler_console.setFormatter(formatter)
    handler_file.setFormatter(formatter)
         
    logger.addHandler(handler_console)
    logger.addHandler(handler_file)
    
    if para == 1:
        logger.info("{} exists Loading...".format(extract_filename_from_path(path)))
    if para == 0:
        logger.info("{} isn't exist.".format(extract_filename_from_path(path)))
    if para == -1:
        logger.info("{} Loading completed.".format(extract_filename_from_path(path)))
    #移除处理器
    logger.removeHandler(handler_file)
    logger.removeHandler(handler_console)

if __name__ == "__main__":
    path = 'D:\\school\\Daily\\Comsume\\Comsume.xlsx'
    datasetLoading(path)