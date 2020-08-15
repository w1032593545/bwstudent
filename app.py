from flask import Flask, render_template, request, url_for, redirect
from dbs import db
from sqlalchemy import or_
from models import *
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    informations = Student.query.all()
    return render_template('index.html', informations=informations)


@app.route('/addOrModify/', methods=['GET', 'POST'])
def addOrModify():
    if request.method == 'POST':
        get_name = request.form.get('name')
        get_english = request.form.get('english')
        get_python = request.form.get('python')
        get_c = request.form.get('c')
        if get_name and get_english and get_python and get_c:
            score = int(get_english) + int(get_python) + int(get_c)
            data = Student(name=get_name, english=get_english, python=get_python, c=get_c, score=score)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('AddOrModify.html', err='*请填写完整')
    return render_template('AddOrModify.html')


@app.route('/dels/', methods=['GET', 'POST'])
def dels():
    del_id = request.args.get('del')
    if del_id:
        Student.query.filter(Student.id == del_id).delete()
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/modify/', methods=["GET", "POST"])
def modify():
    modify_id = request.args.get('modify')
    if modify_id:
        data = Student.query.filter(Student.id == modify_id)
        if request.method == 'POST':
            get_name = request.form.get('name')
            get_english = request.form.get('english')
            get_python = request.form.get('python')
            get_c = request.form.get('c')
            if get_name and get_english and get_python and get_c:
                score = int(get_english) + int(get_python) + int(get_c)
                data.update({'name': get_name, 'english': get_english, 'python': get_python, 'c': get_c, 'score':score})
                db.session.commit()
                return redirect(url_for('index'))
            else:
                return render_template('AddOrModify.html', err='*请填写完整')
        return render_template('AddOrModify.html', data=data)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        get_text = request.form.get('text')
        datas = Student.query.filter(or_(Student.name.like('%' + get_text + '%'), Student.id.like(get_text))).all()
        if datas:
            return render_template('index.html', datas=datas)
        else:
            return render_template('index.html', err='查无此人~')
    return render_template('index.html')


@app.route('/order/', methods=['GET', 'POST'])
def order():
    get_order = request.args.get('order')
    orders = Student.query.order_by(db.desc(get_order))
    d = Student.query.all()
    return render_template('index.html', orders=orders, d=d)


if __name__ == '__main__':
    app.run()
