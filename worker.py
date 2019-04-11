# coding=utf-8
# python 3.7.3

import crawler
import sqlite_data

# 抓取省级以上数据并入库
def fetch_provinces(year):
    print("starting fetch provinces data")
    provinces = crawler.fetch_provinces(year,'index')
    #元组(code,name)
    if len(provinces)>0:
        print("fetch provinces data success")
    else:
        print("fetch provinces data error")
        return 

    sqlite_data.save_provinces(provinces)
    return provinces

# 抓取地市级以上数据并入库
def fetch_cities(year):
    print("starting fetch cities data")
    provinces = fetch_provinces(year)
    if len(provinces)>0:
        print("fetch provinces data success")
    else:
        print("fetch provinces data error")
        return
    all_cities = []
    for province in provinces:
        cities = crawler.fetch_cities(year,province[0])
        if len(cities)>0:
            print("fetch province["+province[1]+"] cities success")
        else:
            print("fetch province["+province[1]+"] cities error")
            continue

        for index,city in enumerate(cities):
            #元组(code,name,parent)
            cities[index] = (city[0].split("/").pop(),city[1],province[0])
        sqlite_data.save_cities(cities)
        all_cities = all_cities + cities
    return all_cities


# 抓取区县级以上数据并入库
def fetch_counties(year):
    print("starting fetch counties data")
    cities = fetch_cities(year)
    if len(cities)>0:
        print("fetch cities data success")
    else:
        print("fetch cities data error")
        return 
    all_counties = []
    for city in cities:
        counties = crawler.fetch_counties(year,city[2][0:2]+"/"+city[0])
        if len(counties)>0:
            print("fetch city["+city[1]+"] counties success")
        else:
            print("fetch city["+city[1]+"] counties error")
            continue

        for index,county in enumerate(counties):
            #元组(code,name,parent)
            counties[index] = (county[0].split("/").pop(),county[1],city[0])
        sqlite_data.save_counties(counties)
        all_counties = all_counties + counties
    return all_counties

# 抓取乡镇街道级以上数据并入库
def fetch_towns(year):
    print("starting fetch towns data")
    counties = fetch_counties(year)
    if len(counties)>0:
        print("fetch counties data success")
    else:
        print("fetch counties data error")
        return 
    all_towns = []
    for county in counties:
        towns = crawler.fetch_towns(year,county[2][0:2]+"/"+county[2][2:4]+"/"+county[0])
        if len(towns)>0:
            print("fetch county["+county[1]+"] towns success")
        else:
            print("fetch county["+county[1]+"] towns error")
            continue

        for index,town in enumerate(towns):
            #元组(code,name,parent)
            towns[index] = (town[0].split("/").pop(),town[1],county[0])
        sqlite_data.save_towns(towns)
        all_towns = all_towns + towns
    return all_towns

# 抓取村委居委级以上数据并入库
def fetch_villages(year):
    print("starting fetch villages data")
    towns = fetch_towns(year)
    if len(towns)>0:
        print("fetch towns data success")
    else:
        print("fetch towns data error")
        return 
    all_villages = []
    for town in towns:
        villages = crawler.fetch_villages(year,town[2][0:2]+"/"+town[2][2:4]+"/"+town[2][4:6]+"/"+town[0])
        if len(villages)>0:
            print("fetch town["+town[1]+"] villages success")
        else:
            print("fetch town["+town[1]+"] villages error")
            continue

        for index,village in enumerate(villages):
            #元组(code,name,parent)
            villages[index] = (village[0].split("/").pop(),village[1],village[0])
        sqlite_data.save_villages(villages)
        all_villages = all_villages + villages
    return all_villages