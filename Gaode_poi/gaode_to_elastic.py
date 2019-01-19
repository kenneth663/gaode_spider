import json
import requests
import time
from elasticsearch import Elasticsearch
from .elasticsearch_type import Gaode_Poi


client = Elasticsearch(hosts=["127.0.0.1"])

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
        for poi in poi_lists:
            poi_dict = {}
            poi_dict["id"] = poi.get('id')
            poi_dict["biz_type"] = poi.get('biz_type')
            poi_dict["name"] = poi.get('name')
            poi_dict["type"] = poi.get('type')
            poi_dict["address"] = poi.get('address')
            poi_dict["tel"] = poi.get('tel')
            poi_dict["location"] = poi.get('location')
            poi_dict["pcode"] = poi.get('pcode')
            poi_dict["pname"] = poi.get('pname')
            poi_dict["citycode"] = poi.get('citycode')
            poi_dict["cityname"] = poi.get('cityname')
            poi_dict["adcode"] = poi.get('adcode')
            poi_dict["adname"] = poi.get('adname')
            poi_dict["business_area"] = poi.get('business_area')

            es_poi = Gaode_Poi()
            es_poi.id = poi_dict["id"]
            es_poi.biz_type = poi_dict["biz_type"]
            es_poi.name = poi_dict["name"]
            es_poi.type = poi_dict["type"]
            es_poi.address = poi_dict["address"]
            es_poi.tel = poi_dict["tel"]
            es_poi.location = poi_dict["location"]
            es_poi.pcode = poi_dict["pcode"]
            es_poi.pname = poi_dict["pname"]
            es_poi.citycode = poi_dict["citycode"]
            es_poi.cityname = poi_dict["cityname"]
            es_poi.adcode = poi_dict["adcode"]
            es_poi.adname = poi_dict["adname"]
            es_poi.business_area = poi_dict["business_area"]
            es_poi.save()
    else:
        pass
    return poi_json.get("pois")


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
        url_amap = 'http://restapi.amap.com/v3/place/text?key=此处填写你的key&types=061205' + '&city=' + city[y] + '&citylimit=true&children=1&offset=20&page=page_index&extensions=all'
        page_size = 20
        page_index = r'page=1'
        global total_record
        total_record = 0
        getPOIdata(page_size, url_amap)


