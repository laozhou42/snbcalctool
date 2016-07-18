#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gl
import json
import util
import account_setting

endpoint = 'https://xueqiu.com'
tx_url = endpoint + '/service/poster'


def login():
		login_url = endpoint + '/user/login'
		gl.gl_session.headers = {
				'X-Requested-With': 'XMLHttpRequest'}
		post_body = {'username': account_setting.username, 'password': account_setting.password}
		login_request = gl.gl_session.post(login_url, data=post_body)
		resp_obj = json.loads(login_request.text)
		if resp_obj.get('error_description'):
				print '登录雪球失败,密码错误...'
				return False
		else:
				print '登录雪球完成...'
				return True


def get_group_id():
		group_url = endpoint + '/stock/transgroup/list.json?_=' + util.get_current_time_stamp()
		get_group_id_request = gl.gl_session.get(group_url)
		groups = json.loads(get_group_id_request.text)
		print '已取得组合ID,ID为:' + str(groups[0].get('id'))
		return str(groups[0].get('id'))


def get_group_performance(m_group_id):
		group_performance_url = endpoint + '/stock/portfolio/performances.json?size=100&page=1&showshort=1&group_id' + m_group_id + '&includeTotal=1&_=' + util.get_current_time_stamp()
		get_group_performance_request = gl.gl_session.get(group_performance_url)
		resp_obj = json.loads(get_group_performance_request.text)
		if len(resp_obj):
				trade_record_list = resp_obj[0].get('list')
		else:
				trade_record_list = []
		print '已取得之前交易记录...'
		return trade_record_list


def del_before_record(m_group_id, record):
		symbol_str = str(record.get('symbol'))
		post_body = {
				'url': '/stock/portfolio/deltrans.json',
				'data[symbol]': symbol_str,
				'data[group_id]': m_group_id,
				'data[_]': util.get_current_time_stamp()
		}
		del_record_request = gl.gl_session.post(tx_url, data=post_body)
		resp_obj = json.loads(del_record_request.text)
		if not resp_obj.get('success'):
				print '删除' + symbol_str + '此股票交易记录失败,程序结束...'
				success = False
		else:
				success = True
		return success


def add_action(stock_type, m_op, m_commission_rate, m_tax_rate):
		post_body = {
				'url': '/stock/commissiontax/add.json',
				'data[stock_type]': stock_type,
				'data[op_type]': m_op,
				'data[commission_rate]': m_commission_rate,
				'data[tax_rate]': m_tax_rate,
				'data[_]': util.get_current_time_stamp()
		}
		add_action_request = gl.gl_session.post(tx_url, data=post_body)
		resp_obj = json.loads(add_action_request.text)
		if not resp_obj.get('success'):
				print '添加股票交易记录动作失败,程序结束...'
				success = False
		else:
				success = True
		return success


def add_stock(m_symbol):
		post_body = {
				'url': '/stock/portfolio/addstock.json',
				'data[pname]': u'全部',
				'data[code]': m_symbol,
				'data[_]': util.get_current_time_stamp()
		}
		add_stock_request = gl.gl_session.post(tx_url, data=post_body)
		resp_obj = json.loads(add_stock_request.text)
		if not resp_obj.get('success'):
				print '添加' + m_symbol + '此股票交易记录失败,程序结束...'
				success = False
		else:
				success = True
		return success


def add_trans(stock_type, date_str, m_symbol, m_group_id, m_price, m_volume, m_commission_rate, m_tax_rate):
		post_body = {
				'url': '/stock/portfolio/addtrans.json',
				'data[type]': stock_type,
				'data[date]': date_str,
				'data[comment]': '',
				'data[symbol]': m_symbol,
				'data[groupId]': m_group_id,
				'data[price]': m_price,
				'data[shares]': m_volume,
				'data[commissionRate]': m_commission_rate,
				'data[taxRate]': m_tax_rate,
				'data[_]': util.get_current_time_stamp()
		}
		add_trans_request = gl.gl_session.post(tx_url, data=post_body)
		resp_obj = json.loads(add_trans_request.text)
		if not resp_obj.get('success'):
				print '添加' + m_symbol + '此股票交易失败,程序结束...'
				success = False
		else:
				success = True
		return success


def set_amount(m_group_id, m_amount):
		post_body = {
				'url': '/stock/principal/update.json',
				'data[exchange]': 'EXCHANGE_CHA',
				'data[group_id]': m_group_id,
				'data[amount]': m_amount,
				'data[_]': util.get_current_time_stamp()
		}
		set_amount_request = gl.gl_session.post(tx_url, data=post_body)
		resp_obj = json.loads(set_amount_request.text)
		if not resp_obj.get('success'):
				print '设置本金失败...'
		print '本金设置成功...'
