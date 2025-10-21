import sys
import os
from pathlib import Path

# 测试不同的路径获取方法
print("=== 测试路径获取方法 ===")

# 方法1: 使用 sys.argv[0]（当前脚本路径）
print("方法1 - sys.argv[0]:")
print(f"当前脚本路径: {sys.argv[0]}")
print(f"脚本所在目录: {Path(sys.argv[0]).parent.resolve()}")

# 方法2: 使用 os.getcwd()（当前工作目录）
print("\n方法2 - os.getcwd():")
print(f"当前工作目录: {os.getcwd()}")

# 方法3: 使用 __file__（当前文件路径）
print("\n方法3 - __file__:")
try:
    print(f"当前文件路径: {__file__}")
    print(f"文件所在目录: {Path(__file__).parent.resolve()}")
    print(f"项目根目录: {Path(__file__).parent.parent.resolve()}")
except NameError:
    print("__file__ 未定义（在直接执行代码时）")

# 方法4: 在 file_utils.py 中获取项目根目录的正确方法
print("\n方法4 - 在 file_utils.py 中获取项目根目录:")
# 如果 file_utils.py 被导入，使用 __file__
# 如果直接执行，使用 sys.argv[0] 或 os.getcwd()

def get_project_root():
    """获取项目根目录"""
    try:
        # 如果当前文件被导入，使用 __file__
        current_file = Path(__file__)
        return current_file.parent.parent.resolve()
    except NameError:
        # 如果直接执行，使用当前工作目录
        return Path(os.getcwd()).resolve()

print(f"项目根目录: {get_project_root()}")