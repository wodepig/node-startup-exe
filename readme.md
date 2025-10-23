pyinstaller --onefile main.py --name my_app    --add-data "config.json;."
这个会把配置打包进去, 但是运行时没办法修改


ui.py添加:
self.admin_check_var = BooleanVar()

    def __tk_check_button_admin_check(self,parent):
        cb = Checkbutton(parent,text="高级设置",variable=self.admin_check_var)
        cb.place(x=374, y=0, width=80, height=30)
        return cb