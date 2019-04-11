# coding=utf-8
# python 3.7.3

import urllib.request
import re
import time
i = 200

#定义一个重试修饰器，默认重试一次
def retry(num_retries=1):
    def wrapper(func):
        def wrapper(*args,**kwargs):
            last_exception = None
            for _ in range(num_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("error occurred: retry fecthing data")
                    last_exception = e
                    #如果要看抛出错误就可以抛出
                    raise last_exception
        return wrapper
    return wrapper


#取得网页内容
@retry(5)
def fetch_html_content(url,charset='utf-8'):
    global i
    if i <= 1:
        print("sleeping 30s")
        time.sleep(30)
        i = 200
    i -= 1
    content = ""
    try:
        page = urllib.request.urlopen(url,timeout=10)
        content = page.read().decode(charset)
    except Exception:
        print("failure: "+url)
    return content

#国家统计局-统计用区划和城乡划分代码-链接格式
#{year}为从2009开始有效的年份数,{path}主要为区域代码拼装的路径串
url_template="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/{year}/{path}.html"

#抓取
def fetch_data(url_template,year,path):
    url_template_year = url_template.replace('{year}',year).replace('{path}',path)
    print("fetching from "+url_template_year)
    return fetch_html_content(url_template_year,'gbk')

## 抓取省级
def fetch_provinces(year,path):
    data = fetch_data(url_template,year,path)
    pattern = re.compile(r'<td><a href=\'(.*?)\.html\'>(.*?)<br\/><\/a>')
    items = re.findall(pattern, data)
    return items

## 抓取地市级
def fetch_cities(year,path):
    data = fetch_data(url_template,year,path)
    pattern = re.compile(r'<tr class=\'citytr\'><td><a href=\'(.*?)\.html\'>.*?<\/a><\/td><td><a.*?>(.*?)<\/a>')
    items = re.findall(pattern, data)
    return items

## 抓取区县级
def fetch_counties(year,path):
    data = fetch_data(url_template,year,path)
    pattern = re.compile(r'<tr class=\'countytr\'><td><a href=\'(.*?)\.html\'>.*?<\/a><\/td><td><a.*?>(.*?)<\/a>')
    items = re.findall(pattern, data)
    return items

## 抓取乡镇街道级
def fetch_towns(year,path):
    data = fetch_data(url_template,year,path)
    pattern = re.compile(r'<tr class=\'towntr\'><td><a href=\'(.*?)\.html\'>.*?<\/a><\/td><td><a.*?>(.*?)<\/a>')
    items = re.findall(pattern, data)
    return items

## 抓取村委居委级
def fetch_villages(year,path):
    data = fetch_data(url_template,year,path)
    pattern = re.compile(r'<tr class=\'villagetr\'><td>(.*?)<\/td><td>.*?<\/td><td>(.*?)<\/td>')
    items = re.findall(pattern, data)
    return items

# provinces = fetch_provinces('2018','index')
# cities = fetch_cities('2018','11')
# counties = fetch_counties('2018','11/1101')
# towns = fetch_towns('2018','11/01/110101')
# villages = fetch_villages('2018','11/01/01/110101001')