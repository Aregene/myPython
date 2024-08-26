"""
author : 胡澄宇
data   : 2024-08-26
"""

def pathSpecification(path):
    # 将所有的"//"替换为"\\"
    modified_path = path.replace("//", "\\\\")
    # 将所有的"/"替换为"\\"
    modified_path = modified_path.replace("/", "\\\\")
    return modified_path
    
# 示例
if __name__ == "__main__":
    path = r"\home/user//example/file.txt"  # Unix/Linux风格的绝对路径，‌包含"//"
    modified_path = pathSpecification(path)
    print(modified_path)  # 输出: \home\\user\\example\\file.txt
    
    path = r"C:/Users/Example/Documents/file.txt"  # Windows风格的绝对路径
    modified_path = pathSpecification(path)
    print(modified_path)  # 输出: C:\\Users\\Example\\Documents\\file.txt
    