from datasource import DataSource

class DocDataSource(DataSource):
    def __init__(self):
        self.db = "MONGO SERVER"
    
    def publish(self, article):
        super().publish(article)
        print("storing to %s content %s" % (self.db, article.getContent()))
        document = self.__prepareDocumet(article)
        self.storeDocument(document)
        print ("Content inserted to db")
        
    def __prepareDocumet(self, article):
        return {
            "documentType": "article",
            "content": article.getContent()
        }
    
    def storeDocument(self, doc):
        print ("storign doc", doc)
        
