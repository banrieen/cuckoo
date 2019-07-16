from distutils.log import warn as printf
import sys
from bosonnlp import BosonNLP
import yaml
from os.path import expanduser
import os
import collections
import subprocess
import datetime


home = expanduser("~")
with open(os.path.join(home,".ibot.yml")) as f:
   config = yaml.load(f)
   bosonnlp_token = config["token"]


def parse(self, query_string):
       """
       input:
       1月12号 济南到兖州的高铁票
       output:
       [{'entity': [[0, 3, 'time'], [3, 4, 'location'], [5, 6, 'location']], # 需要理解实体出现的模式，这块需要理解上下文
       'tag': ['t', 'm', 'q', 'ns', 'p', 'ns', 'ude', 'n', 'n'],
        'word': ['1月', '12', '号', '济南', '到', '兖州', '的', '硬座', '票']}]
       """
       result = self.nlp.ner(query_string)[0]
       words = result['word']
       tags = result['tag']
       entities = result['entity']
       return (words,entities,tags)

def get_entity(self,parsed_words,index_tuple):
       """
       获取已识别的实体
       采用filter
       参考 python cookbook部分
       input:
           entities : 二元组
           parsed_words : 解析好的词组
       """
       return parsed_words[index_tuple[0]:index_tuple[1]]

def format_entities(self,entities):
       """
       给元组命名
       """
       namedentity = collections.namedtuple('namedentity','index_begin index_end entity_name')
       return [namedentity(entity[0],entity[1],entity[2]) for entity in entities]

def get_format_time(self,time_entity):
       """
       output
       {'timestamp': '2018-12-20 23:30:29', 'type': 'timestamp'}
       """
       basetime = datetime.datetime.today()
       result = self.nlp.convert_time(
           time_entity,
           basetime)
       #print(result)
       timestamp = result["timestamp"]
       return timestamp.split(" ")[0]

       