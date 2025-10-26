pyinstaller --onefile main.py --name py37    --add-data "config.json;."
这个会把配置打包进去, 但是运行时没办法修改


ui.py添加:
self.admin_check_var = BooleanVar()

    def __tk_check_button_admin_check(self,parent):
        cb = Checkbutton(parent,text="高级设置",variable=self.admin_check_var)
        cb.place(x=374, y=0, width=80, height=30)
        return cb

## 使用说明

## 开发/构建说明

1. 设置python环境
推荐开发环境**Python 3.7**, py3.7打包后可以在win7下运行
**构建说明**
- 确保已安装 PyInstaller
- 运行 `pyinstaller --onefile main.py --name py37    --add-data "config.json;."` 进行构建