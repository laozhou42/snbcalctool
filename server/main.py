#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import service
import csv_file_parser
import webbrowser

if __name__ == '__main__':
		# 1.登陆(目的是获取session)
		print '登录雪球中...'
		service.xueqiu_login()
		# print '获取组合ID...'
		# # 2.取得持仓盈亏里所用的组合ID
		# group_id = service.get_xueqiu_group_id()
		# print '正在设置本金...'
		# service.set_group_amount(group_id, '1000000.00')
		# # 3.清空组合里原有的交易记录
		# print '正在取得之前的交易记录...'
		# records_list = service.get_before_records_list(group_id)
		# print '正在清空之前的交易记录...'
		# service.clear_befor_records(group_id, records_list)
		# # 4.从CSV文件中导入交易记录并发送到雪球
		# print '检测读取导入的CSV文件...'
		# if len(sys.argv) == 1:
		#     print '程序没有检测到导入的CSV文件,程序结束...'
		#     exit()
		# file_path = str(sys.argv[1])
		# suffix = '.csv'
		# if str.endswith(file_path, suffix, file_path.find('.')):
		#     print '检测导入CSV文件有效...'
		# else:
		#     print '程序检测导入无效的csv文件,程序结束...'
		#     exit()
		# print '正在读取导入的CSV文件...'
		# trades = csv_file_parser.parse_csv_file_from_trade_order(file_path)
		# print '解析CSV文件完成,正将数据发送到雪球...'
		# service.add_trans_records_to_xueqiu(group_id, trades)
		# print '正在打开Chrome浏览器...'
		# webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("https://xueqiu.com/performance")
