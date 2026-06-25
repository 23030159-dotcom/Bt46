import streamlit as st

st.title("Ứng dụng xét duyệt khoản vay đề tài 7 Hoàng Vũ Tuấn Anh")

# Nhập dữ liệu
STV = st.number_input("Nhập số tiền muốn vay (triệu đồng)", min_value=0.0)
TGV = st.number_input("Nhập thời gian vay (số năm)", min_value=0.1)
LSV = st.number_input("Nhập lãi suất cho vay (số thập phân)", min_value=0.0)
TN = st.number_input("Nhập thu nhập hàng tháng (triệu đồng/tháng)", min_value=0.0)
SNTGD = st.number_input("Nhập số người trong gia đình", min_value=1.0, step=1.0)

CPSH = 5  # Chi phí sinh hoạt cố định

PTMC = st.number_input(
    "Nhập số tiền phải trả cho khoản vay cũ (triệu đồng)",
    min_value=0.0
)

GTTSDB = st.number_input(
    "Nhập giá trị tài sản đảm bảo (triệu đồng)",
    min_value=0.1
)

STKH = st.number_input(
    "Nhập số tuổi của khách hàng",
    min_value=0,
    max_value=120,
    step=1
)

# Nút tính toán
if st.button("Xét duyệt khoản vay"):

    PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))
    DTI = (PTMC + PTMM) / (TN - SNTGD * CPSH)
    LTV = STV / GTTSDB

    st.write(f"### Chỉ số DTI: {DTI * 100:.2f}%")
    st.write(f"### Chỉ số LTV: {LTV * 100:.2f}%")

    if DTI <= 0.7 and LTV <= 0.7 and 18 <= STKH <= 70:
        st.success("✅ ĐƯỢC CHO VAY")
    else:
        st.error("❌ KHÔNG ĐƯỢC CHO VAY")
