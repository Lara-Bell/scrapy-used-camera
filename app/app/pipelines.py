# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy.orm import sessionmaker
from .models import KitamuraUsedDB, MapcameraUsedDB ,db_connect, create_table

class AppPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()

        if item.get('ac') is not None:
            kitamura_used_db = KitamuraUsedDB()
            kitamura_used_db.ac = item["ac"]
            kitamura_used_db.maker = item["maker"]
            kitamura_used_db.name = item["name"]
            kitamura_used_db.price = item["price"]
            kitamura_used_db.shop = item["shop"]
            kitamura_used_db.state = item["state"]
            kitamura_used_db.date = item["date"]

        if item.get('mapcode') is not None:
            mapcamera_used_db = MapcameraUsedDB()
            mapcamera_used_db.mapcode = item["mapcode"]
            mapcamera_used_db.jancode = item["jancode"]
            mapcamera_used_db.maker = item["maker"]
            mapcamera_used_db.name = item["name"]
            mapcamera_used_db.price = item["price"]
            mapcamera_used_db.state = item["state"]
            mapcamera_used_db.point = item["point"]

        try:
            if item.get('ac') is not None:
                session.add(kitamura_used_db)

            if item.get('mapcode') is not None:
                session.add(mapcamera_used_db)

            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item