from flask import Flask, render_template

# 关键：指定 templates 文件夹的相对路径（相对于 222.py 所在的 api 文件夹）
app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route('/')
def show_heart():
    return render_template('heart.html'), 200, {'Content-Type': 'text/html; charset=utf-8'}

# Vercel 必须的 WSGI 入口变量
wsgi_app = app.wsgi_app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, use_reloader=False, debug=False)