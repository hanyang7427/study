# -*- coding: utf-8 -*-
from django import template
register = template.Library()

# 定义一个将日期中的月份转换为大写的过滤器，如8转换为八

# 可以用装饰器的方式注册,默认和函数名一样，也可以用@register.filter(name='bbb')来指定过滤器名称


@register.filter
def month_to_upper(key):
        return ['一', '二', '三', '四', '五', '六', '七',
			'八', '九', '十', '十一', '十二'][key.month - 1]

# 另一种注册过滤器的方法
# register.filter('month_to_upper', month_to_upper)
