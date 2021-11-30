from app.src.models.posts import Posts


class PostsRepository:

    @staticmethod
    def get_all():
        posts = Posts().query.all()
        return_value = []
        for post in posts:
            return_value.append(Posts(post.title, post.created_on, post.author, post.text))
        return return_value

    @staticmethod
    def get_json():
        posts = Posts().query.all()
        return_value = []
        for post in posts:
            return_value.append({
                'title': post.title,
                'created_on': post.created_on,
                'author': post.author,
                'text': post.text
            })
        return return_value

    @staticmethod
    def save(title, created_on, author, text):
        entry = Posts(title, created_on, author, text)
        entry.save()
        return True
