from datasource import DataSource
from random import random

class HttpDataSource(DataSource):
    def __init__(self):
        self.serverNumber = self.__selectSuitableServer()
    
    def publish(self, article):
        super().publish(article)
        print("http publish to server %s content %s" % (self.serverNumber, article.getHtmlContent()))
            
    def __selectSuitableServer(self):
        return int(random() * 4 + 1)
