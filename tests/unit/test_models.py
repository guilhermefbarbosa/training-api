from app.src.models.posts import Posts
from app.src import Repo_as_DB
import json

def test_add_post(test_client):
    Repo_as_DB.save(title="a", created_on="1991-10-25", author="c", text="d")
    assert len(Repo_as_DB.get_all()) == 1

def test_get_json(test_client):
    assert Repo_as_DB.get_json()

def test_get_post_by_title(test_client):
    Repo_as_DB.save(title="b", created_on="1991-10-25", author="c", text="d")
    assert Repo_as_DB.get_by_title("a")[0].title == "a"

def test_del_post_by_title(test_client):
    Repo_as_DB.save(title="c", created_on="1991-10-25", author="c", text="d")
    Repo_as_DB.del_by_title("c")
    assert len(Repo_as_DB.get_by_title("c")) == 0

def test_add_post_duplicado(test_client):
    assert not Repo_as_DB.save(title="b", created_on="1991-10-25", author="c", text="d")

def test_add_post_parcial(test_client):
    assert not ((Repo_as_DB.save(title="d", author="c", text="d")) or \
                (Repo_as_DB.save(title="b", created_on="1991-10-25", text="d")) or \
                (Repo_as_DB.save(title="b", created_on="1991-10-25", author="c")) or \
                (Repo_as_DB.save(created_on="1991-10-25", author="c", text="d")))

def test_get_by_keyword(test_client):
    Repo_as_DB.save(title="como realizar um teste", created_on="1991-10-25", author="c", text="Engenharia de software II")
    Repo_as_DB.save(title="testes são importantes", created_on="1991-10-25", author="c", text="Engenharia de software")
    Repo_as_DB.save(title="testes são necessários", created_on="1991-10-25", author="c", text="Software")
    assert len(Repo_as_DB.get_by_keyword("SOFTWARE")) == 3

def test_invalid_date(test_client):
    Repo_as_DB.save(title="teste de data", created_on="aaaaaaa", author="c", text="SADASDASD")
    assert len(Repo_as_DB.get_by_title("teste de data")) == 0

def test_del_example(test_client):
    example = Posts(title="testes são necessários", created_on="1991-10-25", author="c", text="Software")
    assert Repo_as_DB.del_by_example(example)

def test_del_all(test_client):
    Repo_as_DB.del_all()
    assert len(Repo_as_DB.get_all())==0

