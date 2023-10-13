# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import psycopg2


class ScrapySrealityPipeline:
    def __init__(self):
        
        hostname = 'db'
        username = 'postgres'
        password = 'scraper'
        database = 'listings'
        port='5432'
        
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, database=database, port = port
            )
        self.connection.autocommit = True
        self.cur = self.connection.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS listings (
            id serial PRIMARY KEY, 
            title text,
            imageURL text
            
        )
        """)


    def process_item(self, item, spider):
        self.cur.execute(""" insert into listings (title, imageURL) values (%s,%s)""", (
            item["title"],
            item["imageURL"],
            
        ))

       
        self.connection.commit()
        return item
