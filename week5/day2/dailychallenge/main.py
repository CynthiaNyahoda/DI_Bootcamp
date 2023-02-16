class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        self.pageSize = int(pageSize)
        self.totalPages = (len(self.items) - 1) // self.pageSize + 1
        self.currentPage = 1 if self.totalPages > 0 else 0
    
    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]
    
    def prevPage(self):
        self.currentPage -= 1
        if self.currentPage < 1:
            self.currentPage = 1
        return self
    
    def nextPage(self):
        self.currentPage += 1
        if self.currentPage > self.totalPages:
            self.currentPage = self.totalPages
        return self
    
    def firstPage(self):
        self.currentPage = 1
        return self
    
    def lastPage(self):
        self.currentPage = self.totalPages
        return self
    
    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        if pageNum < 1:
            pageNum = 1
        elif pageNum > self.totalPages:
            pageNum = self.totalPages
        self.currentPage = pageNum
        return self
 

