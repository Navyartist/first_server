// 현재시각 만들기
// 날짜, 시간

function updateDate() {
    // 지금 시각을 표시할 객체 생성
    const today = new Date();
    
    // 1. 날짜 파트 (2025년 12월 23일)
    const year = today.getFullYear();
    const month = today.getMonth() + 1;
    const date = today.getDate();
    
    // 2. 시간 파트 (시:분:초)
    // padStart(2, '0')는 숫자가 한 자리일 때 앞에 '0'을 붙여서 '09'처럼 보이게 해줍니다.
    const hours = String(today.getHours()).padStart(2, '0');
    const minutes = String(today.getMinutes()).padStart(2, '0');
    const seconds = String(today.getSeconds()).padStart(2, '0');

    // 3. 날짜랑 시간 합쳐서 하나의 텍스트로 만들기
    const fullText = `${year}년 ${month}월 ${date}일 ${hours}:${minutes}:${seconds}`;

    // 4. 시간 박스 1개
    let box = document.querySelector('.my-box'); //? querySelector: 태그 검색자
    //? 전체 문서(document, 지금 열고있는 웹페이지 문서)에서 클래스 이름이 my-box인 객체(html 요소)를 가져와 box 변수에 담음
    
    if (!box) {
        // 박스가 처음 생성될 때, 혹은 오류로 현재 생성된 시간 박스가 없을 때 위의 (let)box를 집어넣어라
        document.body.insertAdjacentHTML('beforeend', `<div class="my-box">${fullText}</div>`);
    } else {
        // 박스가 있음
        // 박스의 내용을 새로 업데이트 (갱신용)
        box.innerText = fullText;
    }
}

// 1초마다 실행
setInterval(updateDate, 1000);
updateDate(); // 실행하자마자 첫 화면을 보여주기 위해 호출

// #