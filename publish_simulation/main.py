from article import Article
from http_ds import HttpDataSource
from sql_ds import SQLDataSource
from mongo_ds import DocDataSource
from person import Person

someArticle = Article("is very liked by juan, talks about WAR")
gameArticle = Article("Quake winner is fatality")

juan = Person("Juan")
ivan = Person("Ivan")
jess = Person("Jess")

http1 = HttpDataSource()
http2 = HttpDataSource()

db = SQLDataSource()
mongodb = DocDataSource()

juan.likeArticle(someArticle, http1)
juan.likeArticle(someArticle, http2)
juan.likeArticle(someArticle, db)
juan.likeArticle(someArticle, mongodb)

ivan.likeArticle(gameArticle, http1)

jess.likeArticle(gameArticle, mongodb)
