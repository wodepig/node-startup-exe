import os
import sys
from pathlib import Path
def handle_dist_zip(url):
    pass
def handle_node_zip(url):
    pass
def handle_dist_zip(url):
    pass

def down_file(url,file_name,progress_callback=None, progress_update_callback=None):
    """下载文件
    url:文件url
    file_name:文件名
    """
    save_path = Path(get_project_root()) / file_name  # 用 Path 的 / 运算符拼接路径
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1KB
        downloaded_size = 0
        
        if progress_callback:
            progress_callback(f"开始下载: {os.path.basename(save_path)}")
            progress_callback(f"文件大小: {total_size / (1024*1024):.2f} MB")
        
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    size = file.write(chunk)
                    downloaded_size += size
                    
                    if total_size > 0:
                        progress = (downloaded_size / total_size) * 100
                        if progress_update_callback:
                            progress_update_callback(progress, downloaded_size, total_size)
        
        if progress_callback:
            progress_callback(f"下载完成: {os.path.basename(save_path)}")
        if progress_update_callback:
            progress_update_callback(100, total_size, total_size)
        
        return True
    except Exception as e:
        if progress_callback:
            progress_callback(f"下载失败: {str(e)}")
        return False
def check_file_exist(file_name):
    """检查文件是否存在,可传文件名或目录名"""
    # 使用 Path 拼接路径（推荐纯 Path 语法）
    file_path = Path(get_project_root()) / file_name  # 用 Path 的 / 运算符拼接路径
    if not file_path.exists():
        return False
    return True

def get_project_root():
    """获取项目根目录（main.py所在的目录）"""
    try:
        # 如果当前文件被导入，使用 __file__ 获取项目根目录
        current_file = Path(__file__)
        return current_file.parent.parent.resolve()
    except NameError:
        # 如果直接执行，使用当前工作目录
        import os
        return Path(os.getcwd()).resolve()

# 测试输出项目根目录
print("项目根目录:", get_project_root())