import sys
import os
from pathlib import Path
print(f'打包状态：sys.executable 是.exe的路径{sys.executable}')
def hh():
    exe_dir = os.path.dirname(sys.executable)
    return Path(exe_dir).resolve()
if __name__ == '__main__':
    print(hh())