import asyncio
import streamlit as st
import pandas as pd
import sys
import os
from datetime import datetime

# Thêm đường dẫn hiện tại vào sys.path để có thể import các module từ thư mục hiện tại
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils.multi_file_handler import MultiFileHandler
from src.utils.file_handler import extract_content
from graph.workflow import MultiFileWorkflow

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Finance Report Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def local_css():
    """Thêm CSS tùy chỉnh để tăng tính chuyên nghiệp của giao diện"""
    st.markdown("""
    <style>
        /* Màu sắc chủ đạo - Tài chính */
        :root {
            --primary-color: #1a3a5f;         /* Xanh dương đậm */
            --secondary-color: #4CAF50;       /* Xanh lá - màu tiền */
            --accent-color: #FFC107;          /* Vàng - màu vàng kim */
            --text-color: #333333;            /* Màu chữ chính */
            --background-color: #f7f9fc;      /* Nền sáng chuyên nghiệp */
            --card-bg-color: #ffffff;         /* Màu nền card */
            --border-radius: 8px;             /* Bo tròn góc nhẹ */
            --box-shadow: 0 4px 12px rgba(0,0,0,0.1); /* Đổ bóng tinh tế */
        }
        
        /* Resetters and global styles */
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: var(--primary-color);
        }
        
        /* Header styling */
        .header-container {
            background: linear-gradient(135deg, var(--primary-color), #0f2a49);
            padding: 1.5rem;
            border-radius: var(--border-radius);
            color: white;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 2rem;
            box-shadow: var(--box-shadow);
        }
        
        .logo-title-container {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .logo-image {
            width: 50px;
            height: 50px;
        }
        
        .app-title {
            font-size: 1.8rem;
            font-weight: 600;
            margin: 0;
        }
        
        .app-subtitle {
            font-size: 1rem;
            opacity: 0.8;
            margin-top: 0.5rem;
        }
        
        /* Card styling */
        .custom-card {
            background-color: var(--card-bg-color);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: var(--box-shadow);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .custom-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.15);
        }
        
        /* Button styling */
        .stButton > button {
            background-color: var(--primary-color) !important;
            color: white !important;
            border: none !important;
            border-radius: var(--border-radius) !important;
            padding: 0.5rem 1rem !important;
            font-weight: 500 !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            background-color: #0f2845 !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
            transform: translateY(-2px) !important;
        }
        
        /* File upload area */
        .upload-container {
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .upload-info {
            font-size: 0.9rem; 
            color: #666;
            margin-bottom: 0.5rem;
        }
        
        /* File item styling */
        .file-item-container {
            background-color: var(--card-bg-color);
            border: 1px solid #e0e0e0;
            border-left: 4px solid var(--secondary-color);
            border-radius: var(--border-radius);
            padding: 1rem;
            margin: 0.75rem 0;
            transition: all 0.2s ease;
        }
        
        .file-item-container:hover {
            border-left-color: var(--accent-color);
            box-shadow: var(--box-shadow);
        }
        
        .file-item-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .file-item-title {
            font-weight: 500;
            color: var(--primary-color);
        }
        
        .file-item-meta {
            font-size: 0.85rem;
            color: #666;
            margin-top: 0.25rem;
        }
        
        /* Results section styling */
        .results-section {
            margin-top: 2rem;
        }
        
        .result-header {
            color: var(--primary-color);
            border-bottom: 2px solid var(--secondary-color);
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            font-size: 1.5rem;
            font-weight: 600;
        }
        
        .section-intro {
            color: #555;
            font-size: 0.95rem;
            margin-bottom: 1rem;
        }
        
        /* Result card styling */
        .result-card {
            background-color: var(--card-bg-color);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--box-shadow);
            border-left: 4px solid var(--secondary-color);
            transition: all 0.3s ease;
        }
        
        .result-card:hover {
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }
        
        .result-title {
            color: var(--primary-color);
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }
        
        /* Progress bar */
        .stProgress > div > div {
            background-color: var(--secondary-color) !important;
        }
        
        /* Sidebar */
        .css-18e3th9 {
            padding-top: 0;
        }
        
        section[data-testid="stSidebar"] {
            background-color: var(--background-color);
            border-right: 1px solid #e0e0e0;
        }
        
        section[data-testid="stSidebar"] > div {
            padding-top: 5rem;
            background-image: linear-gradient(135deg, var(--primary-color), #0f2a49);
            background-size: 100% 4rem;
            background-repeat: no-repeat;
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 4rem;
            white-space: pre-wrap;
            border-radius: var(--border-radius);
            background-color: var(--background-color);
            border: 1px solid #e0e0e0;
            color: var(--text-color);
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary-color) !important;
            color: white !important;
            border: 1px solid var(--primary-color) !important;
        }
        
        /* File preview */
        .preview-header {
            font-weight: 600;
            font-size: 1rem;
            color: var(--primary-color);
            margin-bottom: 0.5rem;
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 0.5rem;
        }
        
        /* Date display */
        .date-display {
            color: #666;
            font-size: 0.9rem;
            text-align: right;
            margin-top: 0.5rem;
        }
        
        /* Footer */
        .footer {
            margin-top: 3rem;
            text-align: center;
            color: #666;
            font-size: 0.85rem;
            padding-top: 1rem;
            border-top: 1px solid #e0e0e0;
        }
        
        /* Synthesis report styling */
        .synthesis-report h1 {
            color: var(--primary-color);
            font-size: 1.8rem;
            border-bottom: 2px solid var(--secondary-color);
            padding-bottom: 0.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }

        .synthesis-report h2 {
            color: var(--primary-color);
            font-size: 1.5rem;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }

        .synthesis-report h3 {
            color: var(--primary-color);
            font-size: 1.3rem;
            margin-top: 1.2rem;
            margin-bottom: 0.8rem;
        }

        .synthesis-report ul, .synthesis-report ol {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
        }
        
        /* Synthesis section cards */
        .synthesis-section-card {
            background-color: var(--card-bg-color);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--box-shadow);
            border-left: 4px solid var(--primary-color);
        }
    </style>
    """, unsafe_allow_html=True)

def header_with_logo():
    """Hiển thị header với logo và tiêu đề"""
    
    # Hiển thị giờ hiện tại
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Render header với logo và tiêu đề
    st.markdown(f'''
    <div class="header-container">
        <div class="logo-title-container">
            <h1 class="app-title">Finance Report Analyst</h1>
            <div class="app-subtitle">Phân tích báo cáo tài chính chuyên nghiệp</div>
        </div>
        <div class="date-display">{current_time}</div>
    </div>
    ''', unsafe_allow_html=True)

def update_menu():
    """Cập nhật menu active trong session state"""
    st.session_state.active_menu = st.session_state.menu_choice

def sidebar_navigation():
    """Hiển thị sidebar điều hướng"""
    # Khởi tạo active_menu nếu chưa có
    if 'active_menu' not in st.session_state:
        st.session_state.active_menu = "📤 Upload & Phân tích"
        
    with st.sidebar:
        st.markdown(
            "<div style='height: 4rem;'></div>",
            unsafe_allow_html=True
        )
        
        st.markdown("### 📊 Finance Report Analyst")
        st.markdown("---")
        
        # Menu tabs - chỉ còn 2 tab
        st.markdown("#### 📋 Menu")
        menu = st.radio(
            "Chọn chức năng:",
            ["📤 Upload & Phân tích", "📈 Kết quả"],
            index=0 if st.session_state.active_menu == "📤 Upload & Phân tích" else 1,
            key="menu_choice",
            on_change=update_menu
        )
        
        st.markdown("---")
        
        # Thông tin về chức năng
        with st.expander("ℹ️ Thông tin"):
            st.markdown("""
            **Finance Report Analyst** giúp phân tích báo cáo tài chính từ nhiều định dạng file.
            
            **Hỗ trợ các định dạng:**
            - CSV
            - Excel (xls, xlsx)
            - PDF
            
            **Phiên bản:** 1.0.0
            """)
        
        # Góc trợ giúp
        with st.expander("❓ Trợ giúp"):
            st.markdown("""
            **Cách sử dụng:**
            1. Tải lên các file tài chính cần phân tích
            2. Nhập yêu cầu phân tích
            3. Nhấn nút "Phân tích"
            4. Xem kết quả chi tiết từng file
            
            Có thể phân tích nhiều file cùng lúc.
            """)
    
    return st.session_state.active_menu

def enhance_upload_section():
    """Hiển thị phần upload file cải tiến"""
    st.markdown("<h2>Tải lên báo cáo tài chính</h2>", unsafe_allow_html=True)
    
    # Thông tin về định dạng file hỗ trợ
    st.markdown("""
    <div class="upload-container">
        <div class="upload-info">
            <span style="margin-right: 15px;"><i class="fas fa-file-excel"></i> Excel (xlsx, xls)</span>
            <span style="margin-right: 15px;"><i class="fas fa-file-csv"></i> CSV</span>
            <span><i class="fas fa-file-pdf"></i> PDF</span>
        </div>
    </div>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """, unsafe_allow_html=True)
    
    # Widget upload file
    uploaded_files = st.file_uploader(
        "Kéo thả file vào đây hoặc nhấp để chọn file",
        type=["csv", "xlsx", "xls", "pdf"],
        accept_multiple_files=True,
        key="file_uploader"
    )
    
    return uploaded_files

def display_file_info(uploaded_files, multi_file_handler):
    """Hiển thị thông tin các file đã tải lên"""
    if not uploaded_files:
        return
    
    # Xóa files đã tải lên trước đó
    multi_file_handler.clear()
    
    # Header cho phần file
    st.markdown("<h3>Files đã tải lên</h3>", unsafe_allow_html=True)
    
    # Hiển thị từng file
    for uploaded_file in uploaded_files:
        # Xác định icon và màu dựa trên loại file
        if uploaded_file.name.endswith('.pdf'):
            icon_class = "fas fa-file-pdf"
            icon_color = "#FF5252"
        elif uploaded_file.name.endswith('.csv'):
            icon_class = "fas fa-file-csv" 
            icon_color = "#2196F3"
        else:  # Excel
            icon_class = "fas fa-file-excel"
            icon_color = "#4CAF50"
        
        # Thêm file vào handler
        file_id = multi_file_handler.add_file(uploaded_file, uploaded_file.name)
        
        # Tính kích thước file (KB/MB)
        size_kb = uploaded_file.size / 1024
        size_text = f"{size_kb:.1f} KB" if size_kb < 1024 else f"{size_kb/1024:.2f} MB"
        
        # Hiển thị thông tin file
        with st.container():
            st.markdown(f"""
            <div class="file-item-container">
                <div class="file-item-header">
                    <div>
                        <i class="{icon_class}" style="color: {icon_color}; margin-right: 8px;"></i>
                        <span class="file-item-title">{uploaded_file.name}</span>
                    </div>
                </div>
                <div class="file-item-meta">
                    <span>{uploaded_file.type} • {size_text}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Hiển thị xem trước nội dung trong expander
            with st.expander("Xem trước nội dung"):
                display_file_preview(uploaded_file)

def display_file_preview(uploaded_file):
    """Hiển thị xem trước nội dung file"""
    try:
        content = extract_content(uploaded_file, uploaded_file.name)
        
        if uploaded_file.name.endswith('.pdf'):
            st.markdown(f"<div class='preview-header'><i class='fas fa-file-pdf'></i> Tài liệu PDF</div>", unsafe_allow_html=True)
            preview_content = content[:5000] + ("..." if len(content) > 5000 else "")
            st.text_area("Nội dung PDF", value=preview_content, height=250)
            st.info(f"Hiển thị {min(5000, len(content))} ký tự đầu tiên (tổng {len(content)} ký tự).")
        else:
            st.markdown(f"<div class='preview-header'><i class='fas fa-table'></i> Dữ liệu bảng</div>", unsafe_allow_html=True)
            
            if isinstance(content, list) and len(content) > 1:
                headers = content[0]
                data = content[1:min(len(content), 11)]  # Giới hạn 10 dòng dữ liệu
                
                # Tạo DataFrame từ dữ liệu
                df = pd.DataFrame(data, columns=headers)
                st.dataframe(df, use_container_width=True)
                
                # Hiển thị thông tin về dữ liệu
                st.info(f"Hiển thị {len(data)} trong tổng số {len(content)-1} dòng dữ liệu.")
            else:
                # Xử lý trường hợp không phải dạng bảng hoặc dữ liệu không đủ
                st.dataframe(pd.DataFrame(content), use_container_width=True)
    except Exception as e:
        st.error(f"Không thể hiển thị xem trước: {str(e)}")

def display_synthesis_report(synthesis_result):
    """Hiển thị toàn bộ báo cáo tổng hợp"""
    if not synthesis_result:
        st.info("📋 Chưa có kết quả tổng hợp. Hãy thử phân tích lại các báo cáo.")
        return
    
    # Hiển thị toàn bộ báo cáo tổng hợp
    st.markdown('<div class="synthesis-report">', unsafe_allow_html=True)
    st.markdown(synthesis_result)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Thêm nút để xuất báo cáo tổng hợp
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📥 Xuất báo cáo tổng hợp PDF", use_container_width=True):
            st.info("Đang chuẩn bị báo cáo PDF... Tính năng đang được phát triển.")

def display_analysis_results(result):
    """Hiển thị kết quả phân tích dưới dạng card view chuyên nghiệp"""
    if not result or not result.get("files", None):
        st.warning("Không có kết quả phân tích để hiển thị.")
        return
    
    st.markdown("<h2 class='result-header'>Kết Quả Phân Tích</h2>", unsafe_allow_html=True)
    
    # Tabs cho các cách hiển thị khác nhau
    tab_chi_tiet, tab_so_sanh, tab_tom_tat = st.tabs([
        "📄 Chi tiết từng báo cáo", 
        "📊 Báo cáo trực quan", 
        "📋 Tóm tắt tổng hợp"
    ])
    
    with tab_chi_tiet:
        st.markdown("<div class='section-intro'>Chi tiết kết quả phân tích của từng báo cáo tài chính.</div>", unsafe_allow_html=True)
        
        # Hiển thị kết quả phân tích từng file
        for i, file in enumerate(result.get("files", [])):
            if file.get("analysis", None):
                # Xác định icon dựa trên loại file
                if file['file_name'].endswith('.pdf'):
                    file_icon = "fas fa-file-pdf"
                    file_color = "#FF5252"
                elif file['file_name'].endswith('.csv'):
                    file_icon = "fas fa-file-csv"
                    file_color = "#2196F3"
                else:  # Excel
                    file_icon = "fas fa-file-excel"
                    file_color = "#4CAF50"
                
                # Hiển thị thông tin file
                st.markdown(f"""
                <div class="result-card">
                    <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                        <i class="{file_icon}" style="font-size: 24px; margin-right: 15px; color: {file_color};"></i>
                        <div style="font-weight: 600; font-size: 1.2rem;">{file['file_name']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Tabs bên trong card
                file_analysis = file["analysis"]
                inner_tab1, inner_tab2 = st.tabs(["📝 Tóm tắt", "📊 Chi tiết phân tích"])
                
                with inner_tab1:
                    st.markdown(f"<div class='result-title'>Tiêu đề báo cáo</div>", unsafe_allow_html=True)
                    st.markdown(file_analysis.heading)
                    
                    st.markdown(f"<div class='result-title'>Tóm tắt nội dung</div>", unsafe_allow_html=True)
                    st.markdown(file_analysis.summary)
                
                with inner_tab2:
                    st.markdown(f"<div class='result-title'>Chi tiết phân tích</div>", unsafe_allow_html=True)
                    st.markdown(file_analysis.analysis_detail)
                
                st.markdown("<hr>", unsafe_allow_html=True)
            else:
                display_error_card(i, file)
    
    with tab_so_sanh:
        st.markdown("<div class='section-intro'>Phân tích so sánh giữa các báo cáo tài chính.</div>", unsafe_allow_html=True)
        st.info("📈 Tính năng đang được phát triển. Sẽ sớm ra mắt trong phiên bản tiếp theo!")
    
    with tab_tom_tat:
        st.markdown("<div class='section-intro'>Báo cáo tổng hợp từ tất cả các kết quả phân tích.</div>", unsafe_allow_html=True)
        
        # Kiểm tra kết quả tổng hợp
        if result.get("synthesis_result"):
            display_synthesis_report(result["synthesis_result"])
        else:
            st.info("📋 Chưa có báo cáo tổng hợp. Vui lòng chạy lại phân tích để tạo báo cáo tổng hợp.")

def display_error_card(index, file):
    """Hiển thị card lỗi khi không thể phân tích file"""
    file_name = file.get('file_name', f'File {index+1}')
    
    st.markdown(f"""
    <div class="custom-card" style="border-left: 4px solid #FF5252;">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <i class="fas fa-exclamation-circle" style="font-size: 24px; margin-right: 15px; color: #FF5252;"></i>
            <div style="font-weight: 600; font-size: 1.2rem;">{file_name}</div>
        </div>
        <div style="color: #666;">
            Không thể phân tích file này. Vui lòng kiểm tra định dạng và thử lại.
        </div>
    </div>
    """, unsafe_allow_html=True)


def display_footer():
    """Hiển thị footer"""
    st.markdown("""
    <div class="footer">
        <p>Finance Report Analyst v1.0.0 | © 2025 | Developed by Finance Analytics Team</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Hàm chính của ứng dụng"""
    # Thêm CSS tùy chỉnh
    local_css()
    
    # Hiển thị header
    header_with_logo()
    
    # Hiển thị sidebar navigation
    active_menu = sidebar_navigation()
    
    # Khởi tạo session state
    if 'multi_file_handler' not in st.session_state:
        st.session_state.multi_file_handler = MultiFileHandler()
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = {}
    
    # Xử lý theo menu đã chọn - chỉ còn 2 tab
    if active_menu == "📤 Upload & Phân tích":
        # Hiển thị phần tải lên file
        uploaded_files = enhance_upload_section()
        
        # Hiển thị thông tin file đã tải lên
        if uploaded_files:
            display_file_info(uploaded_files, st.session_state.multi_file_handler)
        
        # Yêu cầu phân tích
        st.markdown("<h3>Yêu cầu phân tích</h3>", unsafe_allow_html=True)
        user_input = st.text_area(
            "Nhập yêu cầu phân tích cụ thể (tuỳ chọn):",
            placeholder="Ví dụ: Phân tích tăng trưởng doanh thu theo quý và so sánh với cùng kỳ năm trước...",
            height=100
        )
        
        # Nút để bắt đầu phân tích
        analyze_col1, analyze_col2 = st.columns([3, 1])
        with analyze_col2:
            analyze_button = st.button("🔍 Phân tích tất cả files", use_container_width=True)
        
        if analyze_button:
            files = st.session_state.multi_file_handler.get_files()
            
            if not files:
                st.error("⚠️ Vui lòng tải lên ít nhất một file để phân tích")
            else:
                # Tạo workflow
                workflow = MultiFileWorkflow().compile()
                
                with st.spinner(f"Đang phân tích {len(files)} file..."):
                    # Hiển thị thanh tiến trình
                    progress_text = st.empty()
                    progress_bar = st.progress(0)
                    
                    # Chúng ta cần theo dõi tiến trình phân tích
                    total_files = len(files)
                    
                    # Chuẩn bị dữ liệu đầu vào cho workflow
                    input_state = {
                        "files": files,
                        "current_file_index": 0,
                    }
                    
                    # Hiển thị bắt đầu phân tích
                    progress_text.text(f"Đang bắt đầu phân tích {total_files} file...")
                    progress_bar.progress(0)
                    
                    result = None
                    # Định nghĩa hàm async để chạy workflow
                    async def run_analysis(wf, state):
                        return await wf.ainvoke(state)
                    
                    # Chạy workflow
                    try:
                        # Execute the workflow
                        result = asyncio.run(run_analysis(workflow, input_state))
                        
                        # Lưu kết quả
                        st.session_state.analysis_results = result
                        
                        # Cập nhật tiến trình hoàn thành
                        progress_bar.progress(1.0)
                        progress_text.text(f"✅ Đã hoàn thành phân tích {total_files} file!")
                        
                        # Hiển thị thông báo thành công
                        st.success(f"✅ Đã hoàn thành phân tích {len(files)} file tài chính!")
                        
                        # Hiển thị kết quả
                        display_analysis_results(result)
                        
                    except Exception as e:
                        st.error(f"❌ Lỗi khi phân tích: {str(e)}")
                        st.write("Chi tiết lỗi:", e)
    
    elif active_menu == "📈 Kết quả":
        # Hiển thị kết quả phân tích đã lưu trong session
        if st.session_state.analysis_results:
            display_analysis_results(st.session_state.analysis_results)
        else:
            st.info("👆 Bạn chưa thực hiện phân tích nào. Vui lòng chuyển đến tab 'Upload & Phân tích' để bắt đầu.")
            
            # Nút chuyển đến tab phân tích - đã sửa để không dùng experimental_rerun
            if st.button("🔍 Đi đến phần Phân tích"):
                st.session_state.active_menu = "📤 Upload & Phân tích"
    
    # Hiển thị footer
    display_footer()

# Chạy ứng dụng
if __name__ == "__main__":
    main()
