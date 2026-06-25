import streamlit as st
import pandas as pd

st.set_page_config(page_title="Thẩm định vay vốn KHCN", layout="centered")
st.title("🏦 Công cụ thẩm định vay vốn cá nhân - đề tài 8 Hoàng Vũ Tuấn Anh")

with st.form("form_vay"):
    ten = st.text_input("Họ và tên khách hàng")
    thu_nhap = st.number_input("Thu nhập hàng tháng (VNĐ)", min_value=0, step=500_000)
    so_tien_vay = st.number_input("Số tiền vay (VNĐ)", min_value=0, step=1_000_000)
    thoi_han = st.number_input("Thời hạn vay (tháng)", min_value=1, max_value=360)
    lai_suat = st.number_input("Lãi suất/năm (%)", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Tính toán")

if submitted:
    lai_thang = lai_suat / 100 / 12
    if lai_thang > 0:
        tra_hang_thang = so_tien_vay * lai_thang / (1 - (1 + lai_thang) ** (-thoi_han))
    else:
        tra_hang_thang = so_tien_vay / thoi_han

    ty_le_tra_no = tra_hang_thang / thu_nhap * 100 if thu_nhap > 0 else 0

    st.subheader("📊 Kết quả thẩm định")
    col1, col2 = st.columns(2)
    col1.metric("Trả hàng tháng", f"{tra_hang_thang:,.0f} đ")
    col2.metric("Tỷ lệ trả nợ/thu nhập", f"{ty_le_tra_no:.1f}%")

    if ty_le_tra_no <= 50:
        st.success("✅ Đủ điều kiện vay")
    else:
        st.error("❌ Tỷ lệ trả nợ vượt 50% thu nhập — cần xem xét lại")
