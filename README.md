
# 爬取高德地图全国poi的爬虫

## 基于python3.6的爬取高德全国poi数据的爬虫,稳定性更高,爬取效率更快,由于高德poi的数据量比较大，这里使用了mongodb和Elasticsearch作为存储，只需要修改key值和types种类即可,每个种类都是遍历全国的抓取.

![image](https://raw.githubusercontent.com/kenneth663/gaode_spider/master/images/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-01-17%20%E4%B8%8B%E5%8D%883.06.13.png)
---

[高德开发者申请](https://lbs.amap.com/)

[所有types的列表](https://github.com/kenneth663/gaode_spider/blob/master/Gaode_poi/amap_poicode.xlsx)

[所有的城市列表](https://github.com/kenneth663/gaode_spider/blob/master/Gaode_poi/city.json)

---
##  所需库
   ```
   elasticsearch 5.1.1
   pip install requests
   pip install elasticsearch==5.1.0
   pip install elasticsearch-dsl==5.1.0
   pip install pymongo
   ```

## 实际运行图
***Elasticsearch***
![elasticsearch](https://raw.githubusercontent.com/kenneth663/gaode_spider/master/images/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-01-17%20%E4%B8%8B%E5%8D%882.51.01.png)

***Mongodb***
![mongodb](https://raw.githubusercontent.com/kenneth663/gaode_spider/master/images/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-01-17%20%E4%B8%8B%E5%8D%882.52.00.png)







  
   
