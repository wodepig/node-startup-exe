# http://upgrade.toolsetlink.com/的工具类
from upgradelink_api_python import models as upgrade_link_models
from upgradelink_api_python.client import Client
def check_config(ak, sk, fk, log_handler=None):
    """
    检查配置是否完整
    Args:
        ak: 访问密钥
        sk: 密钥
        fk: 文件id
        log_handler: 可选的日志处理函数，接收消息作为参数
    """
    if not all([ak, sk, fk]):
        if log_handler:
            log_handler(evt=None,msg="配置不完整，缺少访问密钥、密钥或fileKey", color='red')
        return False
    # log_handler(evt=None,msg=f"ak:{ak},sk:{sk},fk:{fk}", color='green')
    return True
    
def get_first_version(ak, sk, fk, log_handler=None):
    pass

def get_new_version(ak, sk, fk, log_handler=None):
    """
    获取新的版本信息
    Args:
        ak: 访问密钥
        sk: 密钥
        fk: 文件id
        log_handler: 可选的日志处理函数，接收消息作为参数
    """
    flag = check_config(ak, sk, fk, log_handler)
    if not flag:
        return None
    response = send_post(ak,sk,fk)
    print(response)
    if response.code == 200:
        print("请求成功!")
        print(f"消息: {response.msg}")
        print(f"跟踪ID: {response.trace_id}")
        
        # 处理升级数据
        if response.data:
            data = response.data
            print("\n升级信息:")
            print(f"URL Key: {data.url_key}")
            print(f"版本名称: {data.version_name}")
            print(f"版本号: {data.version_code}")
            print(f"URL路径: {data.url_path}")
            print(f"升级类型: {data.upgrade_type}")  # 1: 强制升级, 2: 推荐升级, 3: 可选升级
            print(f"升级提示内容: {data.prompt_upgrade_content}")
            
            # 根据升级类型进行不同处理
            if data.upgrade_type == 1:
                print("\n这是一个强制升级，请立即升级应用。")
                # 执行强制升级逻辑
            elif data.upgrade_type == 2:
                print("\n这是一个推荐升级，建议用户升级应用。")
                # 执行推荐升级逻辑
            elif data.upgrade_type == 3:
                print("\n这是一个可选升级，用户可以选择是否升级。")
                # 执行可选升级逻辑
    else:
        print(f"请求失败，错误码: {response.code}")
        print(f"错误信息: {response.msg}")
        print(f"跟踪ID: {response.trace_id}")
def send_post(ak,sk,fk):
        # 创建配置对象
    config = upgrade_link_models.Config(
        access_key=ak,  # 示例密钥，请替换为您的实际密钥
        access_secret=sk,  # 示例密钥，请替换为您的实际密钥
        protocol="HTTPS",
        endpoint="api.upgrade.toolsetlink.com"
    )
    # 创建客户端
    client = Client(config)
    
    # 设置请求参数
    file_key = fk  # URL应用的唯一标识
    version_code = 0  # 当前应用版本号
    appoint_version_code = 0  # 指定版本号，0表示最新版本
    dev_model_key = ""  # 设备模型标识，可选
    dev_key = ""  # 设备标识，可选
    # 构建请求对象
    request = upgrade_link_models.FileUpgradeRequest(
        file_key=file_key,
        version_code=version_code,
        appoint_version_code=appoint_version_code,
        dev_model_key=dev_model_key,
        dev_key=dev_key
    )
    # 调用API接口
    response = client.file_upgrade(request)
    return response
    
def format_upgrade_link(link, log_handler=None):
    """
    格式化升级链接，添加换行符
    
    Args:
        link: 需要格式化的链接字符串
        log_handler: 可选的日志处理函数，接收消息作为参数
    """
    try:
        result = link.replace("\\n", "\n")
        if log_handler:
            log_handler(msg=f"成功格式化升级链接: {link}", color='green')
        return result
    except Exception as e:
        if log_handler:
            log_handler(msg=f"格式化升级链接时出错: {str(e)}", color='red')
        raise
