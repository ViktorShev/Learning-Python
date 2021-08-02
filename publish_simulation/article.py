class Article:
    def __init__(self, content):
        self.content = content
        
    def getContent(self):
        return self.content
        
    def getHtmlContent(self):
        return "<br><h>%s</h><br>" % self.content