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

def header():
    """Hiển thị header đơn giản"""
    st.title("📊 Finance Report Analyst")
    st.caption("Phân tích báo cáo tài chính chuyên nghiệp")
    
    # Hiển thị giờ hiện tại
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    st.text(f"Thời gian hiện tại: {current_time}")
    
    # Phân cách header và nội dung
    st.markdown("---")

def update_menu():
    """Cập nhật menu active trong session state"""
    st.session_state.active_menu = st.session_state.menu_choice

def update_model_selection():
    """Cập nhật model được chọn trong session state và xóa các state hiện tại"""
    import yaml
    import os
    from configs.config import settings
    
    # Cập nhật model trong session state
    st.session_state.selected_model = st.session_state.model_choice
    
    # Đọc config hiện tại
    config_path = "settings/config.yml"
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    # Cập nhật model trong config
    config['llm_params']['model'] = st.session_state.selected_model
    
    # Lưu config mới
    with open(config_path, 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False, allow_unicode=True)
    
    # Cập nhật settings runtime
    settings.CONF['llm_params']['model'] = st.session_state.selected_model
    
    # Xóa các state hiện tại
    if 'multi_file_handler' in st.session_state:
        st.session_state.multi_file_handler.clear()
    
    if 'analysis_results' in st.session_state:
        st.session_state.analysis_results = {}

def sidebar_navigation():
    """Hiển thị sidebar điều hướng đơn giản"""
    # Khởi tạo active_menu nếu chưa có
    if 'active_menu' not in st.session_state:
        st.session_state.active_menu = "📤 Upload & Phân tích"
    
    # Khởi tạo selected_model nếu chưa có
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = ""
        
    with st.sidebar:
        st.header("📊 Finance Report Analyst")
        st.markdown("---")
        
        # Thêm phần lựa chọn model
        st.subheader("🤖 Lựa chọn Model")
        model_options = [
            "gpt-4o-mini",
            "gpt-4o",
            "gpt-4.1",
            "llama-3.3",
            "qwen3-30b-a3b",
            "llama-4-scout",
            "gemini-2.5-flash-preview-04-17",
            "claude-3-7-sonnet-20250219"
        ]
        
        # Hiển thị dropdown để chọn model
        st.selectbox(
            "Chọn model:",
            model_options,
            key="model_choice",
            index=0 if st.session_state.selected_model == "" else model_options.index(st.session_state.selected_model)
        )
        
        # Nút xác nhận lựa chọn model
        if st.button("✅ Xác nhận chọn model", key="confirm_model", use_container_width=True):
            update_model_selection()
            st.success(f"Đã chọn model: {st.session_state.selected_model}. Các kết quả phân tích trước đây đã được xóa.")
        
        # Hiển thị model đang được sử dụng
        if st.session_state.selected_model:
            st.info(f"Model đang sử dụng: {st.session_state.selected_model}")
        
        st.markdown("---")
        
        # Menu tabs - chỉ còn 2 tab
        st.subheader("📋 Menu")
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

def upload_section():
    """Hiển thị phần upload file đơn giản"""
    st.header("Tải lên báo cáo tài chính")
    
    # Thông tin về định dạng file hỗ trợ
    st.info("Hỗ trợ định dạng: Excel (xlsx, xls), CSV, PDF")
    
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
    st.header("Files đã tải lên")
    
    # Hiển thị từng file
    for uploaded_file in uploaded_files:
        # Xác định icon dựa trên loại file
        if uploaded_file.name.endswith('.pdf'):
            file_icon = "📄"
        elif uploaded_file.name.endswith('.csv'):
            file_icon = "📊"
        else:  # Excel
            file_icon = "📑"
        
        # Thêm file vào handler
        file_id = multi_file_handler.add_file(uploaded_file, uploaded_file.name)
        
        # Tính kích thước file (KB/MB)
        size_kb = uploaded_file.size / 1024
        size_text = f"{size_kb:.1f} KB" if size_kb < 1024 else f"{size_kb/1024:.2f} MB"
        
        # Hiển thị thông tin file
        with st.container():
            st.markdown(f"{file_icon} **{uploaded_file.name}** ({uploaded_file.type} • {size_text})")
            
            # Hiển thị xem trước nội dung trong expander
            with st.expander("Xem trước nội dung"):
                display_file_preview(uploaded_file)

def display_file_preview(uploaded_file):
    """Hiển thị xem trước nội dung file"""
    try:
        content = extract_content(uploaded_file, uploaded_file.name)
        
        if uploaded_file.name.endswith('.pdf'):
            st.subheader("Tài liệu PDF")
            preview_content = content[:5000] + ("..." if len(content) > 5000 else "")
            st.text_area("Nội dung PDF", value=preview_content, height=250)
            st.info(f"Hiển thị {min(5000, len(content))} ký tự đầu tiên (tổng {len(content)} ký tự).")
        else:
            st.subheader("Dữ liệu bảng")
            
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
    st.markdown(synthesis_result)
    
    # Thêm nút để xuất báo cáo tổng hợp
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📥 Xuất báo cáo tổng hợp PDF", use_container_width=True):
            st.info("Đang chuẩn bị báo cáo PDF... Tính năng đang được phát triển.")

def display_analysis_results(result):
    """Hiển thị kết quả phân tích sử dụng thành phần Streamlit mặc định"""
    if not result or not result.get("files", None):
        st.warning("Không có kết quả phân tích để hiển thị.")
        return
    
    st.header("Kết Quả Phân Tích")
    
    # Tabs cho các cách hiển thị khác nhau
    tab_chi_tiet, tab_so_sanh, tab_tom_tat = st.tabs([
        "📄 Chi tiết từng báo cáo", 
        "📊 Báo cáo trực quan", 
        "📋 Tóm tắt tổng hợp"
    ])
    
    with tab_chi_tiet:
        st.info("Chi tiết kết quả phân tích của từng báo cáo tài chính.")
        
        # Hiển thị kết quả phân tích từng file
        for i, file in enumerate(result.get("files", [])):
            if file.get("analysis", None):
                # Xác định icon dựa trên loại file
                if file['file_name'].endswith('.pdf'):
                    file_icon = "📄"
                elif file['file_name'].endswith('.csv'):
                    file_icon = "📊"
                else:  # Excel
                    file_icon = "📑"
                
                # Hiển thị thông tin file
                st.subheader(f"{file_icon} {file['file_name']}")
                
                # Tabs bên trong
                file_analysis = file["analysis"]
                inner_tab1, inner_tab2 = st.tabs(["📝 Tóm tắt", "📊 Chi tiết phân tích"])
                
                with inner_tab1:
                    st.subheader("Tiêu đề báo cáo")
                    st.markdown(file_analysis.heading)
                    
                    st.subheader("Tóm tắt nội dung")
                    st.markdown(file_analysis.summary)
                
                with inner_tab2:
                    st.subheader("Chi tiết phân tích")
                    st.markdown(file_analysis.analysis_detail)
                
                st.markdown("---")
            else:
                display_error_card(i, file)
    
    with tab_so_sanh:
        st.components.v1.html(result.get("html_report"), height=600, scrolling=True)
    
    with tab_tom_tat:
        st.info("Báo cáo tổng hợp từ tất cả các kết quả phân tích.")
        
        # Kiểm tra kết quả tổng hợp
        if result.get("synthesis_result"):
            display_synthesis_report(result["synthesis_result"])
        else:
            st.info("📋 Chưa có báo cáo tổng hợp. Vui lòng chạy lại phân tích để tạo báo cáo tổng hợp.")

def display_error_card(index, file):
    """Hiển thị thông tin lỗi khi không thể phân tích file"""
    file_name = file.get('file_name', f'File {index+1}')
    
    st.error(f"⚠️ {file_name}: Không thể phân tích file này. Vui lòng kiểm tra định dạng và thử lại.")

def main():
    """Hàm chính của ứng dụng"""
    # Hiển thị header
    header()
    
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
        uploaded_files = upload_section()
        
        # Hiển thị thông tin file đã tải lên
        if uploaded_files:
            display_file_info(uploaded_files, st.session_state.multi_file_handler)
        
        # Yêu cầu phân tích
        st.header("Yêu cầu phân tích")
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
                        "requirement": user_input
                    }
                    
                    # Thêm thông tin về model được chọn (nếu có)
                    if st.session_state.selected_model:
                        st.info(f"Đang sử dụng model: {st.session_state.selected_model}")
                    
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
            
            # Nút chuyển đến tab phân tích
            if st.button("🔍 Đi đến phần Phân tích"):
                st.session_state.active_menu = "📤 Upload & Phân tích"
    
    # Hiển thị footer đơn giản
    st.markdown("---")
    st.caption("Finance Report Analyst v1.0.0 | © 2025 | Developed by Finance Analytics Team")

# Chạy ứng dụng
if __name__ == "__main__":
    main()
