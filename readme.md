pyinstaller --onefile main.py --name py37    --add-data "config.json;."
这个会把配置打包进去, 但是运行时没办法修改


ui.py添加:
self.admin_check_var = BooleanVar()

    def __tk_check_button_admin_check(self,parent):
        cb = Checkbutton(parent,text="高级设置",variable=self.admin_check_var)
        cb.place(x=374, y=0, width=80, height=30)
        return cb
## 原理讲解

## 使用说明

## 开发/本地打包

1. 设置python环境
推荐开发环境**Python 3.7**, py3.7打包后可以在win7下运行
2. 安装依赖
3. 创建默认的config.json, 可根据config.demo.json做修改
4. 启动项目
python main.py
依赖正确的情况下就能展示主界面了
5. 更新ui
ui界面用的是[Tkinter布局助手](https://www.pytk.net/), 是一个[开源项目](https://github.com/iamxcd/tkinter-helper).
打开[Tkinter布局助手](https://www.pytk.net/), 把'程序启动器.tk'文件导入, 就可以直接在网页上做布局了.
![](./images/tk-helper01.png)
添加控件后, 可以点击'窗口布局代码', 一键复制布局代码到ui.py中
![](./images/tk-helper02.png)
> 注意:
布局器中的高级设置没有绑定variable,需要手动修改一下
> ```python
>     def __init__(self):
>         super().__init__()
>         self.__win()
>         self.admin_check_var = BooleanVar() #这是新增的
>         ...其他代码...
>     def __tk_check_button_admin_check(self,parent):
>         #variable=self.admin_check_va是新增的
>         cb = Checkbutton(parent,text="高级设置",variable=self.admin_check_var)
>         cb.place(x=374, y=0, width=80, height=30)
>        return cb
> ```
**该网站没有撤销/历史记录, 记得及时导出备份!!!**
**该网站没有撤销/历史记录, 记得及时导出备份!!!**
**该网站没有撤销/历史记录, 记得及时导出备份!!!**
6. 更新逻辑
布局器生成的'窗口控制器代码'不要复制, 自己根据事件新建并实现即可
7. 打包
> --add-data "config.json;."是为了把配置文件打包进去, 解释请看运行原理
```python
# 打包个调试版本, 启动有黑窗口能看到print
pyinstaller --onefile main.py --name 文件名    --add-data "config.json;."
# 打包个正常版本, 启动无黑窗口
pyinstaller --onefile main.py --name 文件名 --noconsole    --add-data "config.json;."

```


**构建说明**
- 确保已安装 PyInstaller
- 运行 `pyinstaller --onefile main.py --name py37    --add-data "config.json;."` 进行构建