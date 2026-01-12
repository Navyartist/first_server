# 아주 간단한 플라스크 서버 구현하기 (서버-웹 메시지 전송 집중)
from flask import Flask, render_template

app = Flask(__name__)

class User():
    def __init__(self, name, status):
        self.name = name
        self.status = status

user_list =[]
while True:
    name = input('user name 입력 (그만하려면 q): ')
    if name.lower() == 'q':
        break #? 실행시 반복 빠져나가기가 제대로 안 먹음
    status = input('status 입력: ')
    user_list.append(User(name, status))

@app.route('/')
def home():
    # 파이썬에서 만든 데이터
    if user_list:
        user = user_list[0]
        return render_template('index.html', name=user.name, msg=user.status)
    return "등록된 사용자가 없습니다."
    # render_template이 index.html을 찾아 데이터를 넣어줍니다.
    

if __name__ == '__main__':
    app.run(debug=True)

    #! 다음 단계: 웹페이지에 '다음' 버튼 추가
    #! 버튼 클릭 시, 내부 리스트에 저장된 유저 정보를 바꾸어 출력함(조회)