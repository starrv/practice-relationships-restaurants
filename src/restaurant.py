from review import *

class Restaurant:
    
    def __init__(self,name):
        self.name=name
        self.reviews=[]

    def get_name(self):
        return self.name
    
    def add_review(self,review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews
    
    def average_rating(self):
        reviews=self.get_reviews()
        ratings=[review.get_rating() for review in reviews]
        return sum(ratings)/len(ratings)