import os
import json  # 需导入json模块
import sys
from pathlib import Path
 # Fernet 是 AES 的简化封装，更易用
from cryptography.fernet import Fernet
# 配置文件中需要加密的字段
need_encrypt = ['ulConf.sk','sk']
KEY = b'abedefg'  # 替换为你生成的密钥 Fernet.generate_key()



class ConfigManager:

    def get_config_path(self):
        """获取 config.json 文件的路径"""
        return Path(self.get_project_root()) / 'config.json'
    def encrypt_data(self,data):
        """加密字符串（先转为 bytes）"""
        cipher = Fernet(KEY)
        return cipher.encrypt(data.encode()).decode()  # 加密后转为字符串，方便存储

    def decrypt_data(self,encrypted_data):
        """解密字符串（先转为 bytes）"""
        cipher = Fernet(KEY)
        return cipher.decrypt(encrypted_data.encode()).decode()

    def read(self, key, default=None):
        """从 config.json 读取指定键的值（支持嵌套键）"""
        config_path = self.get_config_path()  # 需用self调用实例方法
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
            if key in need_encrypt:
                return self.decrypt_data(current)
            return current
        except (json.JSONDecodeError, IOError):
            return default

    def get_project_root(tmp=False):
        """获取项目根目录（main.py所在的目录）"""
        try:
            # 如果当前文件被导入，使用 __file__ 获取项目根目录
            if getattr(sys, 'frozen', False) and not tmp:
                # print(f'(cfg)打包状态：sys.executable 是.exe的路径{sys.executable}')
                exe_dir = os.path.dirname(sys.executable)
                return Path(exe_dir).resolve()
            else:
                # print(f'(cfg)开发状态：__file__ 是当前脚本路径{__file__}')
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
        if key in need_encrypt:
            value = self.encrypt_data(value)
        current[keys[-1]] = value  # 设置最终键的值
        
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False


# 使用示例
if __name__ == "__main__":
    sk = 'UpgradeLink的SecretKey'
    # cfg = ConfigManager()
    # 1. 先生成密钥
    # key = Fernet.generate_key()
    # print(f'生成的密钥：{key}')
    # 2. 用密码加密ulConf.sk
    # encrypted = cfg.encrypt_data(sk)
    # print(f'加密后的字符串：{encrypted}')
    # 3. 把加密后的字符串手动写入配置文件
    # 4. 解密测试
    # decrypted = cfg.read('ulConf.sk')
    # print(f'解密后的字符串：{decrypted}')

