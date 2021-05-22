class Person:
    def __init__(self, name):
        self.name = name
        
    def likeArticle(self, article, datasource):
        print(self.name, "likes an article and it will be republished to a tracker")
        datasource.publish(article)
        