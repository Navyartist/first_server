from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 파이썬에서 만든 데이터
    user_name = "Gemini"
    status = "연결 성공!asdf"
    
    # render_template이 index.html을 찾아 데이터를 넣어줍니다.
    return render_template('index.html', name=user_name, msg=status)

if __name__ == '__main__':
    app.run(debug=True)