from flask import Flask, render_template
import webbrowser
from threading import Timer
import os

# 初始化Flask应用
app = Flask(__name__)

# 定义路由：访问根目录时显示爱心页面
@app.route('/')
def show_heart():
    # 渲染templates目录下的heart.html文件
    #return render_template('index.html')
    return render_template('heart.html')

# 自动打开浏览器
def open_browser():
    # 确保在应用启动后再打开浏览器
    webbrowser.open_new('http://127.0.0.1:5000/')

# 主函数
if __name__ == '__main__':
    # 启动服务器前1秒打开浏览器
    Timer(1, open_browser).start()
    # 启动Flask开发服务器，允许外部访问
    app.run(debug=True, use_reloader=False)

