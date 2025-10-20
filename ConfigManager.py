import os
import json  # 需导入json模块

class ConfigManager:
    def get_config_path(self):
        """获取 config.json 文件的路径"""
        return os.path.join(os.path.dirname(__file__), 'config.json')
    
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
            return current
        except (json.JSONDecodeError, IOError):
            return default
    
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