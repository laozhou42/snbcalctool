#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import util


def parse_csv_file_from_trade_order(m_file_path):
		csv_reader = csv.reader(open(m_file_path, 'rb'))
		data_source = []
		for row in csv_reader:
				parameter_str = ','.join(row)
				parameters = parameter_str.split(',')
				if str(parameters[4]).decode('GB2312') == u'证券买入' or str(parameters[4]).decode('GB2312') == u'证券卖出':
						stock_code = util.fix_code_str(str(parameters[2]))
						if str(parameters[15]).decode('GB2312') == u'上海Ａ股':
								exchange = 'SH'
						elif str(parameters[15]).decode('GB2312') == u'深圳Ａ股':
								exchange = 'SZ'
						else:
								continue
						if str(parameters[4]).decode('GB2312') == u'证券买入':
								op = '0'
						else:
								op = '1'
						trade_dict = {
								'code': stock_code,
								'symbol': exchange + stock_code,
								'op': op,
								'date': util.format_date_str(parameters[0]),
								'price': str(parameters[6]),
								'volume': str(parameters[5]),
								'commission_rate': '0',
								'tax_rate': '0'
						}
						data_source.append(trade_dict)
				else:
						continue
		return data_source
