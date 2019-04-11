# coding=utf-8
# python 3.7.3

import worker

import sqlite_data

sqlite_data.init_data()

# 省级
# worker.fetch_provinces('2018')

# 省级 地市级
# worker.fetch_cities('2018')

# 省级 地市级 区县级
# worker.fetch_counties('2018')

# 省级 地市级 区县级 乡镇街道级
# worker.fetch_towns('2018')

# 省级 地市级 区县级 乡镇街道级 村委居委级
worker.fetch_villages('2018')