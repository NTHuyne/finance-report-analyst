# 📊 Finance Report Analyst

Ứng dụng phân tích báo cáo tài chính với giao diện Streamlit cho phép người dùng tải lên và phân tích các file tài chính ở định dạng CSV, Excel và PDF. Ứng dụng sử dụng trí tuệ nhân tạo để phân tích báo cáo và đưa ra những hiểu biết có giá trị từ dữ liệu tài chính, đồng thời tạo báo cáo HTML trực quan.

## ✨ Tính năng

- 📤 Upload file CSV, Excel (xls/xlsx) hoặc PDF
- 📋 Hiển thị nội dung file dưới dạng bảng dữ liệu hoặc văn bản
- 🤖 Phân tích tự động với AI các báo cáo tài chính
- 🔄 Tổng hợp dữ liệu từ nhiều báo cáo với khả năng tìm kiếm thông tin bổ sung
- 📝 Báo cáo chi tiết có cấu trúc với thông tin trích xuất từ các tài liệu tài chính
- 📈 Tạo báo cáo HTML trực quan với biểu đồ và đồ thị
- 🎨 Giao diện người dùng trực quan và chuyên nghiệp

## 🛠️ Công nghệ sử dụng

- **🚀 Streamlit**: Framework giao diện người dùng trực quan
- **⛓️ LangChain/LangGraph**: Xây dựng luồng công việc AI và chuỗi công cụ phân tích
- **🧠 OpenAI/Google Gemini**: Mô hình ngôn ngữ lớn để phân tích báo cáo tài chính
- **🐼 Pandas**: Xử lý dữ liệu dạng bảng từ file CSV và Excel
- **📄 PyPDF2**: Trích xuất nội dung từ file PDF
- **🔍 DuckDuckGo Search API**: Tìm kiếm thông tin bổ sung cho báo cáo tổng hợp
- **📊 Chart.js**: Tạo biểu đồ và đồ thị trực quan trong báo cáo HTML

## 📥 Cài đặt

1. 📂 Clone repository:
```bash
git clone https://github.com/yourusername/finance-report-analyst.git
cd finance-report-analyst
```

2. 📦 Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

3. ⚙️ Cấu hình:
   - Tạo file cấu hình dựa trên mẫu `settings/config.example.yml`
   - Thêm API key cho các dịch vụ AI (OpenAI hoặc Google Gemini)

## 🚀 Cách sử dụng

1. 🏃‍♂️ Chạy ứng dụng Streamlit:
```bash
streamlit run src/app.py
```

2. 🌐 Truy cập ứng dụng qua trình duyệt (mặc định tại http://localhost:8501)

3. 📤 Upload file CSV, Excel hoặc PDF

4. ✍️ Tùy chọn thêm yêu cầu phân tích cụ thể

5. 🔄 Nhấn nút "Phân tích tất cả files" để bắt đầu phân tích

6. 📊 Xem kết quả chi tiết từng file và báo cáo tổng hợp

## 🔄 Luồng phân tích

Ứng dụng xử lý các báo cáo tài chính theo quy trình LangGraph:

1. 📥 **Thu thập dữ liệu**: Upload và trích xuất nội dung từ các file
2. 🔍 **Phân tích từng báo cáo**: Sử dụng ReportAnalysisAgent để phân tích từng báo cáo riêng biệt
3. 🔄 **Tổng hợp kết quả**: Sử dụng ReportSynthesisAgent để kết hợp thông tin từ tất cả các báo cáo và tìm kiếm thông tin bổ sung
4. 📊 **Tạo báo cáo HTML**: Sử dụng HTMLGeneratorAgent để tạo báo cáo HTML trực quan với biểu đồ và đồ thị
5. 📄 **Hiển thị kết quả**: Trình bày kết quả dưới dạng báo cáo có cấu trúc và trực quan

## 📁 Cấu trúc dự án

```
finance-report-analyst/
├── README.md
├── requirements.txt
├── configs/              # Cấu hình dự án
│   ├── config.py         # Module cấu hình chính
│   └── config_loader/    # Bộ đọc cấu hình (YAML, JSON)
├── settings/             # Cài đặt và file cấu hình
│   └── config.example.yml # File cấu hình mẫu
└── src/
    ├── app.py            # Giao diện Streamlit
    ├── graph/            # Xử lý luồng công việc với LangGraph
    │   ├── state.py      # Định nghĩa trạng thái của luồng công việc
    │   └── workflow.py   # Định nghĩa luồng công việc phân tích
    ├── nodes/            # Các node xử lý AI
    │   ├── html_generator/  # Tạo báo cáo HTML
    │   │   ├── agent.py     # Agent tạo báo cáo HTML
    │   │   ├── html_template.py # Mẫu HTML với Chart.js
    │   │   └── prompts.py   # Prompt cho việc tạo HTML
    │   ├── report_analysis/ # Phân tích từng báo cáo
    │   │   ├── agent.py     # Agent phân tích báo cáo
    │   │   ├── prompts.py   # Prompt cho việc phân tích
    │   │   └── schemas.py   # Schema định nghĩa cấu trúc kết quả
    │   └── report_synthesis/ # Tổng hợp từ các báo cáo
    │       ├── agent.py     # Agent tổng hợp báo cáo
    │       └── prompts.py   # Prompt cho việc tổng hợp
    ├── tools/            # Công cụ hỗ trợ cho AI
    │   └── report_analysis_tools/ # Công cụ phân tích báo cáo
    │       └── tools.py    # Công cụ tìm kiếm web
    └── utils/            # Tiện ích
        ├── file_handler.py  # Xử lý file đơn
        ├── multi_file_handler.py  # Xử lý nhiều file
        └── save_html_file.py # Lưu báo cáo HTML
```

## 🛠️ Tùy chỉnh

Bạn có thể tùy chỉnh ứng dụng bằng cách:

- ⚙️ Chỉnh sửa file `settings/config.yml` để thay đổi mô hình AI hoặc tham số
- 🧰 Thêm công cụ mới vào thư mục `src/tools/`
- 💬 Chỉnh sửa các prompt trong thư mục `src/nodes/*/prompts.py`
- 🖌️ Tùy chỉnh mẫu HTML trong file `src/nodes/html_generator/html_template.py`
- 📈 Thêm các biểu đồ và đồ thị mới vào báo cáo HTML

## 💻 Yêu cầu hệ thống

- 🐍 Python 3.7+
- 🌐 Kết nối internet (để sử dụng API của OpenAI hoặc Google và tìm kiếm thông tin bổ sung)
- 📚 Các thư viện trong requirements.txt

## 👥 Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng mở issue hoặc pull request nếu bạn muốn cải thiện dự án.

## 📝 Giấy phép

📌 Phiên bản 1.0.0 | © 2025 | 💼 Developed by Finance Analytics Team
