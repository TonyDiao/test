from flask import Flask, render_template, jsonify
from jieba.analyse import extract_tags
import string
import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/time')
def get_time():
    time_str = utils.get_time()
    return time_str


@app.route("/center1")
def get_c1_data():
    data = utils.get_c1_data()
    content = {
        "confirm": str(data[0]),
        "suspect": str(data[1]),
        "heal": str(data[2]),
        "dead": str(data[3])
    }
    return jsonify(content)


@app.route('/center2')
def get_c2_data():
    tups = utils.get_c2_data()
    res = []
    for tup in tups:
        res.append({'name': tup[0], 'value': int(tup[1])})
    return jsonify({'data': res})


@app.route('/left1')
def get_l1_data():
    data = utils.get_l1_data()
    days, confirms, suspects, heals, deads = [], [], [], [], []
    for day, confirm, suspect, heal, dead in data[7:]:
        days.append(day.strftime("%m-%d"))
        confirms.append(confirm)
        suspects.append(suspect)
        heals.append(heal)
        deads.append(dead)
    return jsonify({'day': days, 'confirm': confirms, 'suspect': suspects, 'heal': heals, 'dead': deads})


@app.route('/left2')
def get_l2_data():
    data = utils.get_l2_data()
    days, confirm_adds, suspect_adds = [], [], []
    for day, confirm_add, suspect_add in data[7:]:
        days.append(day.strftime("%m-%d"))
        confirm_adds.append(confirm_add)
        suspect_adds.append(suspect_add)

    return jsonify({'day': days, 'confirm_add': confirm_adds, 'suspect_add': suspect_adds})


@app.route('/right1')
def get_r1_data():
    data = utils.get_r1_data()
    citys = []
    confirms = []
    for city, confirm in data:
        citys.append(city)
        confirms.append(int(confirm))
    return jsonify({'city': citys, 'confirm': confirms})


@app.route('/right2')
def get_r2_data():
    data = utils.get_r2_data()
    contents = []
    for i in data:
        k = i[0].rstrip(string.digits)  # 移除热搜词数字
        v = i[0][len(k):]  # 获取数字
        ks = extract_tags(k)
        for j in ks:
            if not j.isdigit():
                contents.append({'name': j, 'value': v})

    return jsonify({'kws': contents})


if __name__ == '__main__':
    app.run(debug=True)
