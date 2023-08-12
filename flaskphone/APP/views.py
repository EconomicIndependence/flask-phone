# views.py：路由 + 视图函数
from flask import Blueprint, render_template, request, redirect, url_for
from .models import *
from phone import Phone

# 蓝图blueprint
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    return render_template('phone.html')


@blue.route('/process_phone', methods=['POST'])
def process_phone():
    phone = Phone()
    phone_num = request.form.get('phone')
    phone_text = phone.find(phone_num)
    phone_json = phone.human_phone_info(phone_text)
    # 重定向到一个处理数据的页面，这里假设你有一个名为"phone_result"的路由
    return redirect(url_for('user.phone_result', phone=phone_json))


@blue.route('/phone_result/<phone>')
def phone_result(phone):
    return f"该电话号码的信息为：{phone}"



