import pandas as pd
import streamlit as st

from views.add_data import add_data  # type: ignore
from views.check_metrics import check_metrics  # type: ignore
from views.disp_data import disp_data  # type: ignore
from views.modify_and_calc import modify_and_calc  # type: ignore
from views.search import search  # type: ignore

# データの取得
df = pd.read_csv("./assets/data.csv", encoding="utf-8")

# ページ全般の設定
st.set_page_config(layout="wide")

# ヘッダー
st.header("Sample App 1", divider="gray")

# サイドバー: 検索条件入力欄
search(st.sidebar)

# タブ
# 選んだアクションに従ってアクションの表示と処理の呼び出す
tabs = st.tabs(["Add Data", "Modify Data & Calculate", "Check Metrics"])
with tabs[0]:
    disp_data(st, df, 230)
    add_data(st)

with tabs[1]:
    disp_data(st, df, 570)
    modify_and_calc(st)

with tabs[2]:
    disp_data(st, df, 230)
    check_metrics(st, df)
