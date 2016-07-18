#!/usr/bin/env python
# -*- coding: utf-8 -*-


import network


def xueqiu_login():
		network.login()


def get_xueqiu_group_id():
		return network.get_group_id()


def set_group_amount(m_group_id, m_amount):
		network.set_amount(m_group_id, m_amount)


def get_before_records_list(m_group_id):
		return network.get_group_performance(m_group_id)


def clear_befor_records(m_group_id, m_records_list):
		if len(m_records_list):
				for record in m_records_list:
						network.del_before_record(m_group_id, record)
		print '已清空之前交易记录...'


def add_trans_records_to_xueqiu(m_group_id, trades):
		for trade in trades:
				add_action_success = network.add_action('1', trade.get('op'), trade.get('commission_rate'), trade.get('tax_rate'))
				add_stock_success = network.add_stock(trade.get('symbol'))
				add_trans_success = network.add_trans('1', trade.get('date'), trade.get('symbol'), m_group_id, trade.get('price'),
													trade.get('volume'), trade.get('commission_rate'), trade.get('tax_rate'))
				if add_action_success and add_stock_success and add_trans_success:
						return True
				else:
						if not add_action_success:
								print ("Add_Action环节出错")
						elif not add_stock_success:
								print ("Add_Stock环节出错")
						elif not add_trans_success:
								print ("Add_Trans环节出错")
						return False
