from app.src.models.posts import Posts
from datetime import datetime
import json

class PostsRepository:

    def __init__(self):
        self.post_list = []

    def get_all(self):
        return self.post_list

    def get_by_title(self, title: str):
        result = []
        for each in self.post_list:
            if each.title == title:
                result.append(each)
        return result

    def get_by_keyword(self, keyword: str):
        result = []
        for each in self.post_list:
            if keyword.lower() in each.title.lower() or\
                    keyword.lower() in each.text.lower() or\
                    keyword.lower() in each.author.lower():
                result.append(each)
        return result

    def get_by_period(self, start: str, end: str):
        result = []
        for each in self.post_list:
            if datetime.strptime(start, "%d/%m/%Y") < datetime.strptime(each.created_on, "%d/%m/%Y") < datetime.strptime(end, "%d/%m/%Y"):
                result.append(each)
        return result

    def get_by_author(self, author: str):
        result = []
        for each in self.post_list:
            if author.lower() == each.author.lower():
                result.append(each)
        return result

    def del_by_title(self, title: str):
        for aux in range(0, len(self.post_list)):
            if self.post_list[aux].title == title:
                self.post_list.pop(aux)
                return True
        return False

    def del_all(self):
        self.post_list = []
        return True

    def del_by_example(self, example: Posts):
        for aux in range(0, len(self.post_list)):
            if self.post_list[aux].is_equal(example):
                self.post_list.pop(aux)
                return True
        return False

    def get_json(self):
        return_value = {}
        for post in self.post_list:
            return_value[post.title] = post.to_serializable()
        return return_value

    def save(self, title=None, created_on=None, author=None, text=None):
        entry = Posts(title, created_on, author, text)
        if self.is_valid(entry):
            self.post_list.append(entry)
            return True
        else:
            return False

    def is_valid(self, post_to_evaluate: Posts):
        return len(self.get_by_title(post_to_evaluate.title))==0 and\
               post_to_evaluate.is_valid()


