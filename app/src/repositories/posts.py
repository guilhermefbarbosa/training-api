from app.src.models.posts import Post


class PostsRepository:

    @staticmethod
    def get_all():
        posts = Post().query.all()
        return_value = []
        for post in posts:
            return_value.append({
                'title': post.title,
                'created_on': post.created_on,
                'author': post.author,
                'content': post.content
            })
            return return_value
