import streamlit as st
from datetime import date
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="D-Day Counter", page_icon="🎯")

if 'balloon_played' not in st.session_state:
    st.session_state.balloon_played = False
if 'date_selected' not in st.session_state:
    st.session_state.date_selected = False

def on_date_change():
    st.session_state.date_selected = True
    st.session_state.pop("d-day-refresh", None)

if not (st.session_state.date_selected and st.session_state.balloon_played):
    st_autorefresh(interval=60_000, key="d-day-refresh")

st.title("D-Day Counter")

event_name = st.text_input("이벤트 이름을 입력하세요:", value="D-Day")
target_date = st.date_input(
    "목표 날짜를 선택하세요:",
    value=date.today(),
    on_change=on_date_change,
)

today = date.today()
delta = (target_date - today).days

if st.session_state.date_selected:
    if delta > 0:
        st.success(f"{event_name}까지 D-{delta}일 남았습니다!")
    elif delta == 0:
        if not st.session_state.balloon_played:
            st.balloons()
            st.session_state.balloon_played = True
        st.success(f"오늘은 {event_name}입니다! 축하해요! 🎉")
    else:
        st.info(f"{event_name}으로부터 {-delta}일이 지났습니다 (D+{-delta}).")
