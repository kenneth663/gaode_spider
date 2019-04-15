import json
import requests
import time
import sys
import xlwt
from datetime import datetime


today_date = datetime.today()

hkeys = ['id', '行业类型', '名称', '行业分类', '地址', '联系电话', '定位', '省份代码','省份名称', '城市代码',
         '城市名称', '区域代码', '区域名称', '所在商圈']

bkeys = ['id', 'biz_type', 'name', 'type', 'address', 'tel', 'location', 'pcode', 'pname',
         'citycode', 'cityname', 'adcode', 'adname', 'business_area']

def get_data(page_index, url_amap):
    global total_record
    time.sleep(0.5)
    print('解析页码: ' + str(page_index) + '... ...')
    url = url_amap.replace('page_index', str(page_index))
    response = requests.get(url)
    poi_json = response.json()

    if total_record == 0:
        total_record = int(poi_json.get('count'))
    poi_lists = poi_json.get("pois")
    if poi_lists != None or '':
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
        for index, hkey in enumerate(hkeys):
            sheet.write(0, index, hkey)

        for i in range(len(poi_lists)):
            values = poi_lists[i]
            n = i + 1
            for index, key in enumerate(bkeys):
                val = ""
                if key in values.keys():
                    val = values[key]
                sheet.write(n, index, val)
        wbk.save("高德poi"+ str(today_date) + '.xls')
    return poi_json["pois"]


def getPOIdata(page_size, url_amap):
    global total_record
    print("获取POI数据开始")
    json_data = get_data(1, url_amap)
    if (total_record / page_size) != 0:
        page_number = int(total_record / page_size) + 2
    else:
        page_number = int(total_record / page_size) + 1

    for each_page in range(2, page_number):
        get_data(each_page, url_amap)


if __name__ == '__main__':
    city = []
    data = open("city.json", encoding="utf-8-sig")
    strJson = json.load(data)
    for i in range(len(strJson)):
        city.append(strJson[i]['adcode'])
    for y in range(0, len(city)):
        url_amap = 'http://restapi.amap.com/v3/place/text?key=8c5a48048b2b0ae70914079d2800c648&keywords&types=061205' + '&city=' + city[y] + '&citylimit=true&children=1&offset=20&page=page_index&extensions=all'
        page_size = 20
        page_index = r'page=1'
        global total_record
        total_record = 0
        getPOIdata(page_size, url_amap)
