import streamlit as st
import re
from datetime import datetime, timedelta

# 제품별 유통기한(월) 데이터베이스 예시
product_db = {
    "아삭 오이 피클": 6,
    "참치 캔": 36,
    "즉석밥": 12,
    "라면": 12,
    "케첩": 12,
    "마요네즈": 6,
    "카레": 18,
    "스파게티 소스": 24,
    # 원하는 제품명을 추가하세요.
}

def calc_target_date(manufacture_date: str, months: int) -> str:
    """
    제조일자(`yyyy.mm.dd`)와 유통/소비기한(월)을 받아 
    목표일부인(= 제조일자 + months) 반환.
    """
    try:
        dt = datetime.strptime(manufacture_date.strip(), '%Y.%m.%d')
    except ValueError:
        return "형식이 올바르지 않습니다. (예: 2023.08.24)"
    # months만큼 더함
    year = dt.year + (dt.month - 1 + months) // 12
    month = (dt.month - 1 + months) % 12 + 1
    day = dt.day
    # 말일까지 포함하려면 day-1 처리 등 추가가능
    try:
        expiry = datetime(year, month, day)
    except ValueError:
        # 2월 30일 같은 day overflow 처리
        while True:
            try:
                expiry = datetime(year, month, day)
                break
            except ValueError:
                day -= 1
    return expiry.strftime('%Y.%m.%d')

st.title("목표일부인 계산기")

# 입력 폼
with st.form(key="input_form"):
    product_name = st.selectbox("제품명 선택 또는 입력", options=list(product_db.keys()))
    manufacture_date = st.text_input("제조일자 입력 (예: 2023.08.24)")
    submitted = st.form_submit_button("목표일부인 계산")

if submitted:
    if not product_name or not manufacture_date:
        st.error("제품명과 제조일자를 모두 입력하세요.")
    else:
        months = product_db.get(product_name)
        if not months:
            st.error("제품의 보관기간 정보가 없습니다.")
        else:
            target_date = calc_target_date(manufacture_date, months)
            st.success(f"목표일부인: {target_date}")

# 참고: OCR, 이미지 처리, 그 외 기능은 완전히 제거됨
