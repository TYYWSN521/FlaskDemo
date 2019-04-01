from orm import model

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:123456@localhost/flaskdb',
                       encoding="utf8", echo=True)

from sqlalchemy.orm import sessionmaker
session = sessionmaker()()


def insertUser(username, password):
    result = session.add(model.User(username=username, password=password))
    session.commit()
    session.close()
    print(result)


def queryUser(username):
    result = session.query(model.User).filter(model.User.username == username).first()
    if result:
        return result
    else:
        return -1


def insertNov(novel, author, desc="待完善"):
    result = session.add(model.Novel(novel=novel,  desc=desc, author=author))
    session.commit()
    session.close()


def editNov(author,id):
    result = session.query(model.Novel).filter(model.Novel.id == id).update({model.Novel.author:author})
    session.commit()
    session.close()


def queryNovel(id):
    result = session.query(model.Novel).filter(model.Novel.id == id).first()

    if result:
        return result
    else:
        return -1


def queryNovels():
    result = session.query(model.Novel).all()
    if result:
        return result
    else:
        return False


def delNovel(id):
    try:
        result = session.query(model.Novel).filter(model.Novel.id == id)
        if result:
            result.delete()
        session.commit()
        return result
    except Exception:
        return False


if __name__ == "__main__":
    insertUser("2", "2")
    insertNov('全球高武', "方平")
