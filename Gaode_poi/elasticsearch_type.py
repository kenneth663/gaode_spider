from elasticsearch_dsl import DocType, Keyword, Integer
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])

class Gaode_Poi(DocType):
    id = Keyword()
    biz_type = Keyword()
    name = Keyword()
    type = Keyword()
    address = Keyword()
    tel = Keyword()
    #location = GeoPoint()
    location = Keyword()
    pcode = Integer()
    #pcode = Keyword()
    pname = Keyword()
    citycode = Integer()
    #citycode = Keyword()
    cityname = Keyword()
    adcode = Integer()
    #adcode = Keyword()
    adname = Keyword()
    business_area = Keyword()

    class Meta:
        index = "gaode_requests"
        doc_type = "poi_data"

if __name__ == "__main__":
    Gaode_Poi.init()