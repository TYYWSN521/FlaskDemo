from flask import Flask, render_template,request, redirect,make_response
from orm import model
from orm import ormmanage
app = Flask(__name__)


# 将http://127.00.1:5000/和index视图函数绑定


@app.route('/')
def index():
    user = None
    user = request.cookies.get('name')
    return render_template('index.html', userinfo=user)


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/registe', methods=['GET','POST'])
def registe():
    if request.method == "GET":
        return render_template('registe.html')
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        res = ormmanage.queryUser(username)
        if res==-1:
            print("注册成功")
            ormmanage.insertUser(username=username, password=password)
            return redirect("/")
        else:
            print('注册失败')
            # return redirect('/')
            # Response.Write('<script language=javascript>alert("注册失败");</script>')
            return render_template("index.html", error="zhuceshbai")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == "POST":

        username = request.form["username"]
        res = make_response(redirect('/list'))
        res.set_cookie('name', username)
        print("登录帐号", username)
        return res


@app.route('/q')
def quit():
    res = make_response(redirect("/"))
    res.delete_cookie('name')
    return res


@app.route('/list',methods=['GET', 'POST'])
def list():

    infos = ormmanage.queryNovels()
    if infos:
        return render_template('/list.html', infos=infos)


@app.route('/detail/<id>')
def detail(id):
    detail= ormmanage.queryNovel(id)
    return render_template('/detail.html',  detail=detail)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        return render_template('add.html')
    elif request.method == "POST":
        novel = request.form['novel']
        author = request.form['author']
        desc = "https://www.qidian.com/search?kw=" + novel
        res = ormmanage.queryNovel(novel)
        if res == -1:
            print("添加成功")
            ormmanage.insertNov(novel=novel,author=author, desc=desc)
            return redirect("/list")
        else:
            print('添加失败')
            return redirect('/add')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    detail = ormmanage.queryNovel(id)
    if request.method == "GET":

        return render_template('edit.html', detail=detail)
    elif request.method == "POST":
        author = request.form['author']
        res = ormmanage.queryNovel(author)
        if res == -1:
            print("修改成功")
            ormmanage.editNov(author=author, id=detail.id)
            return render_template("list.html", detail=detail)
            # return redirect("/edit", detail=detail)
        else:
            print('修改失败')
            return redirect('/edit')


@app.route('/delete/<int:id>')
def delete(id):
    ormmanage.delNovel(id)
    return render_template('list.html')


if __name__ == "__main__":
    app.run(host="192.168.12.163", port=8888, debug=True)
