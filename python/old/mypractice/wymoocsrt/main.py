# -*- coding: utf-8 -*-
import confparse
# 配置日志
# 初始化数据库
'CREATE TABLE IF NOT EXISTS'


def main():
    # 获取配置文件数据
    info = confparse.client_info('conf.ini')
    info.cfg_load()
    conf = info.get_all_items_dict()

    # 配置日志

    # 初始化数据库

main()