from datasource import DataSource

class SQLDataSource(DataSource):
    def __init__(self):
        self.db = "MYSQL SERVER"
    
    def publish(self, article):
        super().publish(article)
        print("storing to %s content %s" % (self.db, article.getContent()))
        sql = self.__prepareSQLSth(article)
        self.execSQL(sql)
        print ("Content inserted to db")
        
    def __prepareSQLSth(self, article):
        return "insert into ARTICLES (id, content) values (some id, %s )" % article.getContent()
    
    def execSQL(self, sql):
        print ("executint sql order" + sql)