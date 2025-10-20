#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
import os


# 尝试导入所需模块，处理可能的依赖错误
try:
    from upgradelink_api_python.client import Client
    from upgradelink_api_python import models as upgrade_link_models
    from darabonba_base_python.client import Client as DarabonbaBaseClient
    DEPENDENCIES_INSTALLED = True
except ImportError as e:
    print(f"警告: 无法导入依赖模块: {e}")
    print("请先安装依赖: pip install upgradelink-api-python")
    DEPENDENCIES_INSTALLED = False


class UpgradeLinkClient():
    def __init__(self, access_key, access_secret, protocol="HTTPS", endpoint="api.upgrade.toolsetlink.com", log_handler=None):
        # 接收外部传入的配置参数
        self.access_key = access_key
        self.access_secret = access_secret
        self.log_handler = log_handler
        self.config = upgrade_link_models.Config(
            access_key=access_key,
            access_secret=access_secret,
            protocol=protocol,
            endpoint=endpoint
        )      
    def test_get_url_upgrade(self):
        """获取url应用升级内容"""
        try:
            # 创建客户端
            client = Client(self.config)
            
            # 设置请求参数
            url_key = "uJ47NPeT7qjLa1gL3sVHqw"
            version_code = 1
            appoint_version_code = 0
            dev_model_key = ""
            dev_key = ""
            
            # 构建请求对象
            request = upgrade_link_models.UrlUpgradeRequest(
                url_key=url_key,
                version_code=version_code,
                appoint_version_code=appoint_version_code,
                dev_model_key=dev_model_key,
                dev_key=dev_key
            )
            
            # 调用接口
            info, err = None, None
            try:
                info = client.url_upgrade(request)
            except Exception as e:
                err = e
            
            # 打印结果
            if err:
                print("err: ", err)
            else:
                print("info: ", info)
                
        except Exception as e:
            print(f"测试过程中出错: {e}")
    def check_config(self, ak, sk, fk):
        """
        检查配置是否完整
        Args:
            ak: 访问密钥
            sk: 密钥
            fk: 文件id
            log_handler: 可选的日志处理函数，接收消息作为参数
        """
        if not all([ak, sk, fk]):
            if self.log_handler:
                self.log_handler(evt=None,msg="配置不完整，缺少访问密钥、密钥或fileKey", color='red')
            return False
        # log_handler(evt=None,msg=f"ak:{ak},sk:{sk},fk:{fk}", color='green')
        return True
    
    def get_file_upgrade(self, fk):
        """获取file应用升级内容"""
        try:
            # 检查配置是否完整
            flag = self.check_config(self.access_key, self.access_secret, fk)
            if not flag:
                return None
            # 创建客户端
            client = Client(self.config)
            # 设置请求参数
            file_key = fk
            version_code = 1
            appoint_version_code = 0
            dev_model_key = ""
            dev_key = ""
            
            # 构建请求对象
            request = upgrade_link_models.FileUpgradeRequest(
                file_key=file_key,
                version_code=version_code,
                appoint_version_code=appoint_version_code,
                dev_model_key=dev_model_key,
                dev_key=dev_key
            )
            
            # 调用接口
            info, err = None, None
            try:
                info = client.file_upgrade(request)
            except Exception as e:
                err = e
            
            # 打印结果
            if err:
                print("err: ", err)
                if self.log_handler:
                    self.log_handler(evt=None,msg=f"获取file应用升级内容失败: {err}", color='red')
            else:
                print("info: ", info)
            return info
        except Exception as e:
            if self.log_handler:
                self.log_handler(evt=None,msg=f"测试过程中出错: {e}", color='red')
            print(f"测试过程中出错: {e}")
    def test_get_apk_upgrade(self):
        """获取apk应用升级内容"""
        try:
            # 创建客户端
            client = Client(self.config)
            
            # 设置请求参数
            apk_key = "isVZBUvkFhv6oHxk_X-D0Q"
            version_code = 1
            appoint_version_code = 0
            dev_model_key = ""
            dev_key = ""
            
            # 构建请求对象
            request = upgrade_link_models.ApkUpgradeRequest(
                apk_key=apk_key,
                version_code=version_code,
                appoint_version_code=appoint_version_code,
                dev_model_key=dev_model_key,
                dev_key=dev_key
            )
            
            # 调用接口
            info, err = None, None
            try:
                info = client.apk_upgrade(request)
            except Exception as e:
                err = e
            
            # 打印结果
            if err:
                print("err: ", err)
            else:
                print("info: ", info)
                
        except Exception as e:
            print(f"测试过程中出错: {e}")
    
    def test_get_configuration_upgrade(self):
        """获取配置升级内容"""
        try:
            # 创建客户端
            client = Client(self.config)
            
            # 设置请求参数
            configuration_key = "q1hfB1VUQaK9VksTZGPU1Q"
            version_code = 1
            appoint_version_code = 0
            dev_model_key = ""
            dev_key = ""
            
            # 构建请求对象
            request = upgrade_link_models.ConfigurationUpgradeRequest(
                configuration_key=configuration_key,
                version_code=version_code,
                appoint_version_code=appoint_version_code,
                dev_model_key=dev_model_key,
                dev_key=dev_key
            )
            
            # 调用接口
            info, err = None, None
            try:
                info = client.configuration_upgrade(request)
            except Exception as e:
                err = e
            
            # 打印结果
            if err:
                print("err: ", err)
            else:
                print("info: ", info)
                
        except Exception as e:
            print(f"测试过程中出错: {e}")
    
    def test_post_app_report(self):
        """上报事件 - app_start 应用-启动事件"""
        try:
            # 创建客户端
            client = Client(self.config)
            
            # 设置请求参数
            event_type = "app_start"  # app_start 应用-启动事件
            app_key = "LOYlLXNy7wV3ySuh0XgtSg"
            target = "darwin"
            arch = "x86_64"
            dev_model_key = ""
            dev_key = ""
            version_code = 1
            timestamp = DarabonbaBaseClient.time_rfc3339()
            
            # 构建事件数据
            event_data = upgrade_link_models.AppReportRequestEventData(
                launch_time=timestamp,
                version_code=version_code,
                target=target,
                arch=arch,
                dev_model_key=dev_model_key,
                dev_key=dev_key
            )
            
            # 构建请求对象
            request = upgrade_link_models.AppReportRequest(
                event_type=event_type,
                app_key=app_key,
                timestamp=timestamp,
                event_data=event_data
            )
            
            # 调用接口
            info, err = None, None
            try:
                info = client.app_report(request)
            except Exception as e:
                err = e
            
            # 打印结果
            if err:
                print("err: ", err)
            else:
                print("info: ", info)
                
        except Exception as e:
            print(f"测试过程中出错: {e}")


if __name__ == '__main__':
    unittest.main()