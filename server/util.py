#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def get_current_time_stamp():
		return str(time.time())


def fix_code_str(code_str):
		if len(code_str) < 6:
				diff = 6 - len(code_str)
				i = 0
				fix_str = ''
				while i < diff:
						fix_str += '0'
						i += 1
				return fix_str + code_str
		else:
				return code_str


def format_date_str(date_str):
		if not str.isdigit(date_str):
				return ''
		year_str = date_str[0:4]
		month_str = date_str[4:6]
		day_str = date_str[6:8]
		return year_str + '-' + month_str + '-' + day_str
