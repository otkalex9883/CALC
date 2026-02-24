import streamlit as st
import datetime
import locale
import streamlit.components.v1 as components

try:
    locale.setlocale(locale.LC_TIME, "ko_KR.UTF-8")
except locale.Error:
    pass

product_db = {
    "LIGHT&JOY_당을줄인 김천자두쨈 290G": 12,
    "LIGHT&JOY_당을줄인 논산딸기쨈 290G": 12,
    "LIGHT&JOY_당을줄인 논산딸기쨈 480G": 12,
    "LIGHT&JOY_당을줄인 청송사과쨈 290G": 12,
    "간장찜닭양념 240G": 18,
    "간장찜닭양념 480G": 18,
    "갈비양념(호주) 240G": 18,
    "검시럽(롯데리아) 11G": 9,
    "닭볶음탕양념 235G": 18,
    "닭볶음탕양념 470G": 18,
    "돼지갈비양념 240G": 18,
    "돼지갈비양념 480G": 18,
    "돼지갈비양념(미국) 480G": 18,
    "돼지불고기양념 245G": 18,
    "돼지불고기양념 500G": 18,
    "돼지불고기양념(미국) 500G": 18,
    "딸기버터쨈 280G": 10,
    "딸기잼(스타벅스) 12G": 6,
    "딸기잼(에그드랍) 12G": 6,
    "딸기쨈 10KG": 4,
    "딸기쨈 300G": 24,
    "딸기쨈 500G": 24,
    "딸기쨈 850G": 24,
    "딸기쨈(엔제리너스커피) 12G": 6,
    "딸기쨈디스펜팩(KFC) 12G": 6,
    "딸기토핑(맥도날드) 1KG": 6,
    "맛있는딸기쨈830g": 24,
    "맥도날드_스위트앤사워소스(대만R) 28G": "d120",
    "메이플시럽(제이앤이) 1KG": 12,
    "믹스피클(제너시스) 3KG": 3,
    "믹스피클(프레시지) 3KG": 4,
    "불고기양념(호주) 240G": 18,
    "블루베리쨈 300G": 24,
    "블루베리쨈 500G": 24,
    "사과쨈 300G": 24,
    "사과쨈 500G": 24,
    "소갈비양념 240G": 18,
    "소갈비양념 480G": 18,
    "소불고기양념 240G": 18,
    "소불고기양념 480G": 18,
    "스위트앤젤_밀감(18입) 90G": 6,
    "스위트앤젤_복숭아(18입) 90G": 6,
    "스위트앤젤_파인(18입) 90G": 6,
    "스위트오이피클 3KG": 12,
    "아삭 오이 피클 240G": 6,
    "아삭 오이 피클 420G": 6,
    "아삭 오이&무 피클 240G": 6,
    "아삭 오이&무 피클 420G": 6,
    "앙버터쨈 280G": 10,
    "오늘의샐러드_코울슬로 100G": 1,
    "오늘의샐러드_콘샐러드 100G": 1,
    "오뚜기딸기쨈(디스펜팩)(240개입) 12G": 6,
    "오뚜기딸기쨈(디스펜팩)(480개입) 12G": 6,
    "오뚜기일회용딸기쨈 12G": 6,
    "오쉐프_떠먹는샤인머스캣(18입) 90G": 6,
    "오쉐프_떠먹는애플망고 90G": 6,
    "오쉐프_메이플시럽(디스펜팩) 11G": 6,
    "오쉐프_슬라이스오이피클 3KG": 6,
    "오쉐프_오미자믹스피클 3KG": 6,
    "오쉐프_초코소스(디스펜팩) 12G": 6,
    "제주담음_제주청귤마말레이드_280G": 12,
    "제주담음_제주한라봉마말레이드_300G_S": 24,
    "코울슬로(맥도날드) 100G": 1,
    "코울슬로(파파존스) 100G": 1,
    "코울슬로(프랭크버거) 100G": 1,
    "코울슬로(피자헛) 100G": 1,
    "콘샐러드(맘스터치) 100G": 1,
    "콘샐러드(파파존스) 100G": 1,
    "콘샐러드(프랭크버거) 100G": 1,
    "콘샐러드(피자헛) 100G": 1,
    "포도쨈 300G": 24,
    "포도쨈 500G": 24,
    "프레스코_파스타소스 토마토 600G": 12,
    "한컵코울슬로 100G": 1,
    "한컵콘샐러드 100G": 1,
    "후레쉬오이피클(쏘렌토) 3KG": 3,
    "후루츠쨈 300G": 24,
    "후루츠쨈 500G": 24,
    "후루츠쨈 850G": 24
    ####여기까지2팀####  
}

st.markdown(
    """
    <style>
    .main {background-color: #fff;}
    div.stTextInput > label {font-weight: bold;}
    input[data-testid="stTextInput"] {background-color: #eee;}
    .title {font-size:36px; font-weight:bold;}

    .scroll-list {
        max-height: 180px;
        overflow-y: auto;
        border:1px solid #ddd;
        padding:5px;
        margin-bottom:5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">일부인 계산기</div>', unsafe_allow_html=True)
st.write("")

KST = datetime.timezone(datetime.timedelta(hours=9))
today_kst = datetime.datetime.now(KST).date()

st.session_state.setdefault("product_input", "")
st.session_state.setdefault("auto_complete_show", False)
st.session_state.setdefault("selected_product_name", "")
st.session_state.setdefault("date_input", today_kst)

def parse_shelf_life(value):
    if isinstance(value, int):
        return ("month", value)
    if isinstance(value, str):
        v = value.strip()
        if len(v) >= 2 and v[0].lower() == "d":
            num = v[1:].strip()
            if num.isdigit():
                return ("day", int(num))
        if v.isdigit():
            return ("month", int(v))
    raise ValueError(f"소비기한 형식 오류: {value!r} (예: 120 또는 'd120')")

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def get_last_day(year: int, month: int) -> int:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    return 29 if is_leap_year(year) else 28

def get_target_date(start_date: datetime.date, months: int) -> datetime.date:
    y, m, d = start_date.year, start_date.month, start_date.day
    new_month = m + months
    new_year = y + (new_month - 1) // 12
    new_month = ((new_month - 1) % 12) + 1
    last_day = get_last_day(new_year, new_month)
    if d <= last_day:
        if d == 1:
            return datetime.date(new_year, new_month, 1)
        return datetime.date(new_year, new_month, d - 1)
    return datetime.date(new_year, new_month, last_day)

def get_target_date_by_days(start_date: datetime.date, days: int) -> datetime.date:
    if days <= 0:
        raise ValueError(f"일 단위 소비기한은 1 이상이어야 합니다: d{days}")
    return start_date + datetime.timedelta(days=days - 1)

# -----------------------------
# Product input + autocomplete
# -----------------------------
st.write("제품명을 입력하세요")

def on_change_input():
    st.session_state.auto_complete_show = True
    st.session_state.selected_product_name = ""

st.text_input(
    label="제품명",
    value=st.session_state.product_input,
    key="product_input",
    on_change=on_change_input,
    label_visibility="collapsed",
)

input_value = st.session_state.product_input
matching_products = [
    name for name in product_db.keys()
    if input_value.strip() and input_value.strip() in name
]

def select_product(name: str):
    st.session_state.product_input = name
    st.session_state.selected_product_name = name
    st.session_state.auto_complete_show = False

if input_value.strip() and st.session_state.auto_complete_show:
    st.write("입력한 내용과 일치하는 제품명:")
    st.markdown('<div class="scroll-list">', unsafe_allow_html=True)
    for name in matching_products:
        col1, col2 = st.columns([8, 1])
        col1.button(name, key=f"btn_{name}", on_click=select_product, args=(name,), use_container_width=True)
        col2.write("")
    st.markdown("</div>", unsafe_allow_html=True)
elif not input_value.strip():
    st.session_state.selected_product_name = ""
    st.session_state.auto_complete_show = False

# -----------------------------
# Date: single source of truth via query param mfg
#   - Both input and calendar write to mfg
#   - Python reads mfg and updates session_state.date_input
# -----------------------------
st.write("제조일자")

qp_key_date = "mfg"
qp_key_cal = "cal"

if qp_key_date in st.query_params:
    try:
        st.session_state.date_input = datetime.date.fromisoformat(st.query_params[qp_key_date])
    except Exception:
        pass
else:
    # initialize query once
    st.query_params[qp_key_date] = st.session_state.date_input.isoformat()

default_iso = st.session_state.date_input.isoformat()
cal_open = (qp_key_cal in st.query_params) and (str(st.query_params[qp_key_cal]) == "1")

# (1) Custom date INPUT (components) - fully controlled
date_input_html = f"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/ko.js"></script>

<style>
  body {{ margin:0; padding:0; background:transparent; }}
  input {{
    width: 100%;
    box-sizing: border-box;
    padding: 10px 12px;
    border-radius: 8px;
    border: 1px solid #33383f;
    background: rgba(255,255,255,0.06);
    color: white;
    outline: none;
    font-size: 16px;
  }}
  input:focus {{
    border-color: #ff4b4b;
  }}
</style>

<input id="top_date" placeholder="YYYY.MM.DD" />

<script>
(function() {{
  const input = document.getElementById("top_date");

  function setQuery(params) {{
    const url = new URL(window.parent.location.href);
    Object.keys(params).forEach((k) => {{
      const v = params[k];
      if (v === null || v === undefined) url.searchParams.delete(k);
      else url.searchParams.set(k, v);
    }});
    window.parent.history.replaceState({{}}, "", url.toString());
    window.parent.dispatchEvent(new Event("popstate"));
  }}

  // keep value synced from query on each rerender
  input.value = "{st.session_state.date_input.strftime('%Y.%m.%d')}";

  // open calendar expander when focused
  input.addEventListener("focus", () => setQuery({{ "{qp_key_cal}": "1" }}));
  input.addEventListener("click",  () => setQuery({{ "{qp_key_cal}": "1" }}));

  // accept manual typing: on blur, parse and write to query
  input.addEventListener("blur", () => {{
    const raw = (input.value || "").trim();
    if (!raw) return;

    // normalize to YYYY-MM-DD
    let iso = null;

    // YYYY.MM.DD / YYYY-MM-DD / YYYY/MM/DD
    const sepMatch = raw.match(/^(\d{{4}})[.\/-](\d{{1,2}})[.\/-](\d{{1,2}})$/);
    if (sepMatch) {{
      const y = sepMatch[1];
      const m = String(parseInt(sepMatch[2], 10)).padStart(2, "0");
      const d = String(parseInt(sepMatch[3], 10)).padStart(2, "0");
      iso = `${{y}}-${{m}}-${{d}}`;
    }}

    // YYYYMMDD
    const ymdMatch = raw.match(/^(\d{{4}})(\d{{2}})(\d{{2}})$/);
    if (!iso && ymdMatch) {{
      iso = `${{ymdMatch[1]}}-${{ymdMatch[2]}}-${{ymdMatch[3]}}`;
    }}

    if (iso) {{
      setQuery({{ "{qp_key_date}": iso, "{qp_key_cal}": "1" }});
    }}
  }});
}})();
</script>
"""
components.html(date_input_html, height=56)

# (2) Calendar (components) - inline calendar ONLY (remove useless white input)
with st.expander("달력", expanded=cal_open):
    cal_html = f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
    <script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
    <script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/ko.js"></script>

    <style>
      body {{ margin:0; padding:0; background:transparent; }}
      #inline_holder {{ margin-top: 6px; }}
      /* hide the useless white input entirely */
      #hidden_input {{
        position: absolute;
        left: -9999px;
        top: -9999px;
        width: 1px;
        height: 1px;
        opacity: 0;
        pointer-events: none;
      }}
      .flatpickr-calendar {{ z-index: 999999 !important; }}
    </style>

    <input id="hidden_input" />
    <div id="inline_holder"></div>

    <script>
    (function() {{
      const hiddenInput = document.getElementById("hidden_input");
      const holder = document.getElementById("inline_holder");

      function setQuery(params) {{
        const url = new URL(window.parent.location.href);
        Object.keys(params).forEach((k) => {{
          const v = params[k];
          if (v === null || v === undefined) url.searchParams.delete(k);
          else url.searchParams.set(k, v);
        }});
        window.parent.history.replaceState({{}}, "", url.toString());
        window.parent.dispatchEvent(new Event("popstate"));
      }}

      flatpickr(hiddenInput, {{
        locale: "ko",
        dateFormat: "Y.m.d",
        defaultDate: "{default_iso}",
        inline: true,
        appendTo: holder,
        disableMobile: true,
        onChange: function(selectedDates) {{
          const d = selectedDates[0];
          const yyyy = d.getFullYear();
          const mm = String(d.getMonth() + 1).padStart(2, "0");
          const dd = String(d.getDate()).padStart(2, "0");
          const iso = `${{yyyy}}-${{mm}}-${{dd}}`;

          // calendar selection -> update query -> rerun -> top input rerenders with new value
          setQuery({{
            "{qp_key_date}": iso,
            "{qp_key_cal}": null
          }});
        }}
      }});
    }})();
    </script>
    """
    components.html(cal_html, height=360)

# -----------------------------
# Buttons (새로고침 제거, 확인 버튼 단독 전체폭)
# -----------------------------
confirm = st.button("확인", key="confirm", use_container_width=True)

# -----------------------------
# Confirm action
# -----------------------------
if confirm:
    pname = st.session_state.product_input.strip()
    dt = st.session_state.date_input

    if pname not in product_db:
        st.warning("제품명을 정확하게 입력하거나 목록에서 선택하세요.")
    else:
        try:
            unit, amount = parse_shelf_life(product_db[pname])
            if unit == "day":
                target_date = get_target_date_by_days(dt, amount)
                st.success(f"목표일부인: {target_date.strftime('%Y.%m.%d')}", icon="✅")
                st.write(f"제품명: {pname}")
                st.write(f"제조일자: {dt.strftime('%Y.%m.%d')}")
                st.write(f"소비기한(일): {amount}")
            else:
                target_date = get_target_date(dt, amount)
                st.success(f"목표일부인: {target_date.strftime('%Y.%m.%d')}", icon="✅")
                st.write(f"제품명: {pname}")
                st.write(f"제조일자: {dt.strftime('%Y.%m.%d')}")
                st.write(f"소비기한(개월): {amount}")
        except Exception as e:
            st.warning(str(e))
