import os
import json  # 需导入json模块
import sys
from pathlib import Path
# from utils.file_utils import get_project_root
class ConfigManager:

    def get_config_path(self):
        """获取 config.json 文件的路径"""
        # return os.path.join(os.path.dirname(__file__), 'config.json')
        # print('配置文件位置:')
        # print(Path(self.get_project_root()) / 'config.json')
        # print(os.path.join(os.path.dirname(__file__), 'config.json'))
        # return os.path.join(os.path.dirname(__file__), 'config.json')
        return Path(self.get_project_root()) / 'config.json'
    
    def read(self, key, default=None):
        """从 config.json 读取指定键的值（支持嵌套键）"""
        config_path = self.get_config_path()  # 需用self调用实例方法
        print(f'(cfg)读取配置文件：{config_path}')
        if not os.path.exists(config_path):
            return default
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            keys = key.split('.')
            current = config
            for k in keys:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                else:
                    return default
            return current
        except (json.JSONDecodeError, IOError):
            return default
    def get_project_root(tmp=False):
        """获取项目根目录（main.py所在的目录）"""
        try:
            # 如果当前文件被导入，使用 __file__ 获取项目根目录
            if getattr(sys, 'frozen', False) and not tmp:
                print(f'(cfg)打包状态：sys.executable 是.exe的路径{sys.executable}')
                # 打包状态：sys.executable 是.exe的路径
                exe_dir = os.path.dirname(sys.executable)
                return Path(exe_dir).resolve()
            else:
                print(f'(cfg)开发状态：__file__ 是当前脚本路径{__file__}')
                    # 开发状态：__file__ 是当前脚本路径
                # exe_dir = os.path.dirname(__file__)
                # exe_dir = os.path.dirname(os.path.abspath(__file__))
                return Path(__file__).parent.resolve()
        except NameError:
            print('(cfg)无法获取项目根目录，使用当前工作目录')
            # 如果直接执行，使用当前工作目录
            return Path(os.getcwd()).resolve()

    def write(self, key, value):  # 修复缩进：函数定义需缩进
        """向 config.json 写入/更新指定键的值（支持嵌套键）"""
        config_path = self.get_config_path()  # 需用self调用实例方法
        config = {}
        
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            except (json.JSONDecodeError, IOError):
                return False
        
        keys = key.split('.')
        current = config
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            if not isinstance(current[k], dict):
                current[k] = {}  # 若当前键不是字典，强制转为字典（避免覆盖非字典值）
            current = current[k]
        current[keys[-1]] = value  # 设置最终键的值
        
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False


# 使用示例
if __name__ == "__main__":
    cfg = ConfigManager()
    # 写入测试
    success = cfg.write('ulConf.url', 'https://xxx')
    print("写入成功" if success else "写入失败")
    # 读取测试
    print("ulConf.url 的值：", cfg.read('ulConf.url'))