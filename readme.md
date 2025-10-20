pyinstaller --onefile main.py --name my_app    --add-data "config.json;."
这个会把配置打包进去, 但是运行时没办法修改