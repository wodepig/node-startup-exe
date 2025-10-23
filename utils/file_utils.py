import os
import sys
import requests
import zipfile
import shutil
from pathlib import Path
from utils.utils import get_system_architecture
def log_msg(msg,logHandle=None):
    """打印日志
    msg:日志内容
    color:日志颜色
    """
    if color == "red":
        print(f"\033[91m{msg}\033[0m")
    elif color == "green":
        print(f"\033[92m{msg}\033[0m")
    else:
        print(msg)
def unzip_file(file,folder,logHandle=None):
    """解压文件
    file: 文件名
    folder:解压到的目录(相对于项目根目录)
    """
    try:
        if logHandle:
            logHandle(evt=None,msg=f"开始解压: {file}")
        import zipfile
        zip_path = Path(get_project_root()) / file
        extract_dir = Path(get_project_root()) / folder
        if not check_file_exist(file):
            if logHandle:
                logHandle(evt=None,msg=f"文件不存在: {file}",color="red")
            return False
            # 检查zip文件是否有效
        if not zipfile.is_zipfile(zip_path):
            if logHandle:
                logHandle(evt=None,msg=f"解压失败: 不是有效的zip文件 - {zip_path}",color="red")
            return False
        # 创建解压目录（如果不存在）
        os.makedirs(extract_dir, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # 测试zip文件是否损坏
            test_result = zip_ref.testzip()
            if test_result is not None:
                if logHandle:
                    logHandle(evt=None,msg=f"解压失败: zip文件损坏 - {test_result}",color="red")
                return False
            
            # 获取压缩包中的文件列表
            file_list = zip_ref.namelist()
            # 直接解压所有文件，不使用tqdm进度条
            for fileTemp in file_list:
                zip_ref.extract(fileTemp, extract_dir)
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(folder)
        if logHandle:
            logHandle(evt=None,msg=f"解压完成: {file}",color="green")
        return True
    except Exception as e:
        print(e)
        if logHandle:
            logHandle(evt=None,msg=f"解压失败: {str(e)}",color="red")
        return False
def handle_dist_zip(logHandle=None):
    """处理dist.zip文件"""
    if not unzip_file('dist.zip','dist',logHandle):
        return False
def handle_node_zip(logHandle=None):
    """处理node.zip文件"""
    node_dir = Path(get_project_root()) / 'node' 
    # 解压并处理node.zip（如果不存在）
    if  os.path.exists(node_dir):
        if logHandle:
            logHandle(evt=None,msg="node目录已存在，无需处理",color="green")
        return True
    if not unzip_file('node.zip','node_tmp',logHandle):
        return False
    node_temp_dir = Path(get_project_root()) / 'node_tmp' 
    node_version_dir = detect_node_version_dir(node_temp_dir)
    if not node_version_dir:
        if logHandle:
            logHandle(evt=None,msg="无法识别node版本目录",color="red")
        return False
    # 将版本目录中的内容移动到最终的node目录
    if not move_node_contents(node_temp_dir, node_dir, node_version_dir):
        if logHandle:
            logHandle(evt=None,msg="无法处理node文件",color="red")
        return False
    return True

def detect_node_version_dir(temp_dir):
    """自动检测node压缩包解压后的版本目录"""
    try:
        # 获取临时目录中的所有项目
        items = os.listdir(temp_dir)
        
        # 寻找看起来像node版本的目录
        for item in items:
            item_path = os.path.join(temp_dir, item)
            if os.path.isdir(item_path) and item.startswith("node-v"):
                return item
        
        # 如果没找到明显的版本目录，检查是否有直接包含node.exe的目录
        for item in items:
            item_path = os.path.join(temp_dir, item)
            if os.path.isdir(item_path):
                for root, _, files in os.walk(item_path):
                    if "node.exe" in files:
                        return item
                
        return None
        
    except Exception as e:
        print(f"检测node目录时出错: {str(e)}")
        return None
def move_node_contents(temp_dir, target_dir, version_dir):
    """将node版本文件夹中的内容移动到目标node文件夹"""
    try:
        # 构建完整的版本目录路径
        version_path = os.path.join(temp_dir, version_dir)
        
        if not os.path.exists(version_path):
            return False
        if os.path.exists(target_dir):
            # 先删除目标目录（如果存在）
            shutil.rmtree(target_dir)
        # 创建目标目录
        # os.makedirs(target_dir, exist_ok=True)
        
        # 获取所有项目
        # items = os.listdir(version_path)
        shutil.copytree(version_path, target_dir)
        # 删除临时解压目录
        shutil.rmtree(temp_dir)
        return True
    except Exception as e:
        print(f"移动node文件失败: {str(e)}")
        return False

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
            progress_callback(evt=None,msg=f"开始下载: {os.path.basename(save_path)}")
            progress_callback(evt=None,msg=f"文件大小: {total_size / (1024*1024):.2f} MB")
        
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
            progress_callback(evt=None,msg=f"下载完成: {os.path.basename(save_path)}")
        if progress_update_callback:
            progress_update_callback(100, total_size, total_size)
        
        return True
    except Exception as e:
        if progress_callback:
            progress_callback(evt=None,msg=f"下载失败: {str(e)}",color="red")
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
