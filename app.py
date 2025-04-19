from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/')
def hello_index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('auth/login.html')


@app.route('/register')
def register():
    return render_template('auth/register.html')


@app.route('/data_info', methods=['POST'])
def data_info():
    ## 登录后获取用户名，密码，验证码，之后校验，一致则登录，并记录信息
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    captcha = request.form.get('captcha')
    print(f'username:{username} password:{password} captcha:{captcha}')

    ## 登录成功后
    return render_template('data_info.html')


if __name__ == '__main__':
    app.run()
