html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo cáo Tài chính 2023 - Việt Trường Thành</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#1d4ed8',
                        secondary: '#2563eb',
                        accent: '#3b82f6',
                        dark: '#1e293b',
                        light: '#f8fafc',
                        success: '#10b981',
                        warning: '#f59e0b',
                        danger: '#ef4444'
                    }
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700&display=swap');
        
        body {
            font-family: 'Be Vietnam Pro', sans-serif;
            line-height: 1.6;
        }
        
        .financial-card {
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        
        .financial-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
        
        .progress-bar {
            height: 8px;
            border-radius: 4px;
            background-color: #e2e8f0;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 1s ease-in-out;
        }
        
        .chart-container {
            position: relative;
            height: 300px;
        }
        
        .tooltip {
            position: absolute;
            padding: 8px;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            border-radius: 4px;
            pointer-events: none;
            font-size: 12px;
            z-index: 10;
        }
        
        .analysis-text {
            text-align: justify;
            hyphens: auto;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <div class="container mx-auto px-4 py-8 max-w-6xl">
        <!-- Header -->
        <header class="bg-white rounded-xl shadow-md p-6 mb-8 border-l-8 border-primary">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center">
                <div>
                    <h1 class="text-3xl font-bold text-dark mb-2">BÁO CÁO PHÂN TÍCH TÀI CHÍNH CHUYÊN SÂU</h1>
                    <h2 class="text-2xl font-semibold text-primary">CÔNG TY TNHH THIẾT BỊ ĐIỆN VIỆT TRƯỜNG THÀNH</h2>
                    <p class="text-gray-600 mt-2">Năm báo cáo: 2023 | Ngày lập: 29/04/2025 | Phiên bản: 1.0</p>
                </div>
                <div class="mt-4 md:mt-0 bg-blue-50 p-3 rounded-lg border border-blue-100">
                    <div class="flex items-center">
                        <i class="fas fa-info-circle text-blue-500 mr-2"></i>
                        <span class="text-sm font-medium">Mã số thuế: 0110239048</span>
                    </div>
                    <div class="flex items-center mt-1">
                        <i class="fas fa-map-marker-alt text-blue-500 mr-2"></i>
                        <span class="text-sm">Số 29 Phố Lý Thường Kiệt, Hà Đông, Hà Nội</span>
                    </div>
                </div>
            </div>
        </header>

        <!-- Executive Summary -->
        <section class="mb-12">
            <div class="bg-gradient-to-r from-primary to-secondary text-white rounded-xl p-6 shadow-lg">
                <h3 class="text-xl font-bold mb-4 flex items-center">
                    <i class="fas fa-star mr-2"></i> TÓM TẮT KẾT QUẢ CHÍNH
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="bg-white bg-opacity-20 p-4 rounded-lg border border-white border-opacity-30">
                        <div class="flex items-center justify-between">
                            <h4 class="font-medium">Tổng tài sản</h4>
                            <i class="fas fa-wallet text-xl opacity-80"></i>
                        </div>
                        <p class="text-2xl font-bold mt-2">7.252 tỷ VNĐ</p>
                        <p class="text-sm opacity-80">Tăng từ 0 đầu năm</p>
                    </div>
                    <div class="bg-white bg-opacity-20 p-4 rounded-lg border border-white border-opacity-30">
                        <div class="flex items-center justify-between">
                            <h4 class="font-medium">Doanh thu thuần</h4>
                            <i class="fas fa-chart-line text-xl opacity-80"></i>
                        </div>
                        <p class="text-2xl font-bold mt-2">14.149 tỷ VNĐ</p>
                        <p class="text-sm opacity-80">Năm đầu hoạt động</p>
                    </div>
                    <div class="bg-white bg-opacity-20 p-4 rounded-lg border border-white border-opacity-30">
                        <div class="flex items-center justify-between">
                            <h4 class="font-medium">Lợi nhuận sau thuế</h4>
                            <i class="fas fa-coins text-xl opacity-80"></i>
                        </div>
                        <p class="text-2xl font-bold mt-2">79,8 triệu VNĐ</p>
                        <p class="text-sm opacity-80">Biên lợi nhuận: 0.56%</p>
                    </div>
                </div>
                <div class="mt-4 text-sm opacity-90">
                    <p>Báo cáo này cung cấp phân tích toàn diện về tình hình tài chính và kết quả hoạt động kinh doanh năm 2023 của Công ty TNHH Thiết bị Điện Việt Trường Thành, bao gồm đánh giá cấu trúc tài chính, hiệu quả hoạt động, các chỉ số tài chính then chốt cùng với nhận định và khuyến nghị chiến lược.</p>
                </div>
            </div>
        </section>

        <!-- Financial Highlights -->
        <section class="mb-12">
            <h3 class="text-2xl font-bold mb-6 text-dark border-b pb-2 flex items-center">
                <i class="fas fa-chart-pie mr-2 text-primary"></i> PHÂN TÍCH CƠ CẤU TÀI CHÍNH
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <!-- Asset Structure -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-blue-500">
                    <h4 class="font-bold text-lg mb-4 flex items-center">
                        <i class="fas fa-sitemap mr-2 text-blue-500"></i> Cơ cấu tài sản
                    </h4>
                    <div class="chart-container" id="assetChart">
                        <canvas id="assetPieChart"></canvas>
                    </div>
                    <div class="mt-4 space-y-2">
                        <div class="flex justify-between">
                            <span class="text-sm font-medium">Tiền & tương đương</span>
                            <span class="text-sm font-bold">15.8% (1.144 tỷ VNĐ)</span>
                        </div>
                        <div class="progress-bar mt-1">
                            <div class="progress-fill bg-blue-400" style="width: 15.8%"></div>
                        </div>
                        
                        <div class="flex justify-between mt-3">
                            <span class="text-sm font-medium">Các khoản phải thu</span>
                            <span class="text-sm font-bold">79.1% (5.734 tỷ VNĐ)</span>
                        </div>
                        <div class="progress-bar mt-1">
                            <div class="progress-fill bg-blue-600" style="width: 79.1%"></div>
                        </div>
                        
                        <div class="flex justify-between mt-3">
                            <span class="text-sm font-medium">Hàng tồn kho</span>
                            <span class="text-sm font-bold">4.0% (292 triệu VNĐ)</span>
                        </div>
                        <div class="progress-bar mt-1">
                            <div class="progress-fill bg-blue-300" style="width: 4%"></div>
                        </div>
                    </div>
                </div>
                
                <!-- Capital Structure -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-green-500">
                    <h4 class="font-bold text-lg mb-4 flex items-center">
                        <i class="fas fa-balance-scale mr-2 text-green-500"></i> Cơ cấu nguồn vốn
                    </h4>
                    <div class="chart-container" id="capitalChart">
                        <canvas id="capitalPieChart"></canvas>
                    </div>
                    <div class="mt-4 space-y-2">
                        <div class="flex justify-between">
                            <span class="text-sm font-medium">Nợ phải trả</span>
                            <span class="text-sm font-bold">57.5% (4.172 tỷ VNĐ)</span>
                        </div>
                        <div class="progress-bar mt-1">
                            <div class="progress-fill bg-green-500" style="width: 57.5%"></div>
                        </div>
                        
                        <div class="flex justify-between mt-3">
                            <span class="text-sm font-medium">Vốn chủ sở hữu</span>
                            <span class="text-sm font-bold">42.5% (3.080 tỷ VNĐ)</span>
                        </div>
                        <div class="progress-bar mt-1">
                            <div class="progress-fill bg-green-700" style="width: 42.5%"></div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- New Charts: Receivables and Payables Analysis -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <!-- Receivables Analysis -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-indigo-500">
                    <h4 class="font-bold text-lg mb-4 flex items-center">
                        <i class="fas fa-hand-holding-usd mr-2 text-indigo-500"></i> Phân tích khoản phải thu
                    </h4>
                    <div class="chart-container">
                        <canvas id="receivablesChart"></canvas>
                    </div>
                    <div class="mt-4 text-sm text-gray-600 analysis-text">
                        <p>Khoản phải thu khách hàng chiếm tới 71.3% tổng tài sản ngắn hạn, với số dư cuối kỳ 4.106 tỷ VNĐ. Vòng quay khoản phải thu đạt 6.89 lần/năm, tương đương kỳ thu tiền trung bình 53 ngày. Điều này phản ánh chính sách bán chịu kéo dài và cần được quản lý chặt chẽ để giảm thiểu rủi ro nợ khó đòi.</p>
                    </div>
                </div>
                
                <!-- Payables Analysis -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-purple-500">
                    <h4 class="font-bold text-lg mb-4 flex items-center">
                        <i class="fas fa-file-invoice-dollar mr-2 text-purple-500"></i> Phân tích khoản phải trả
                    </h4>
                    <div class="chart-container">
                        <canvas id="payablesChart"></canvas>
                    </div>
                    <div class="mt-4 text-sm text-gray-600 analysis-text">
                        <p>Phải trả người bán chiếm 95.5% tổng nợ phải trả với số dư 3.986 tỷ VNĐ. Vòng quay khoản phải trả đạt 6.94 lần/năm, tương đương kỳ trả tiền trung bình 53 ngày. Công ty đang tận dụng hiệu quả nguồn tài trợ từ nhà cung cấp, nhưng cần cân nhắc rủi ro khi phụ thuộc quá lớn vào nguồn này.</p>
                    </div>
                </div>
            </div>
            
            <!-- Profitability Trend Chart -->
            <div class="financial-card bg-white rounded-xl shadow-md p-6 mb-8 border-t-4 border-yellow-500">
                <h4 class="font-bold text-lg mb-4 flex items-center">
                    <i class="fas fa-chart-line mr-2 text-yellow-500"></i> Xu hướng biên lợi nhuận
                </h4>
                <div class="chart-container">
                    <canvas id="profitabilityChart"></canvas>
                </div>
                <div class="mt-4 text-sm text-gray-600 analysis-text">
                    <p>Biên lợi nhuận gộp đạt 2.23% và biên lợi nhuận ròng chỉ 0.56%, phản ánh áp lực cạnh tranh lớn trong ngành. Chi phí quản lý kinh doanh (340.9 triệu VNĐ) vượt quá lợi nhuận gộp (315.5 triệu VNĐ), cho thấy nhu cầu cấp thiết phải tối ưu hóa cơ cấu chi phí. Doanh thu tài chính (125.1 triệu VNĐ) đóng vai trò quan trọng trong việc bù đắp chi phí quản lý.</p>
                </div>
            </div>
            
            <!-- Financial Ratios -->
            <div class="financial-card bg-white rounded-xl shadow-md p-6 mt-6 border-t-4 border-red-500">
                <h4 class="font-bold text-lg mb-4 flex items-center">
                    <i class="fas fa-percentage mr-2 text-red-500"></i> Chỉ số tài chính then chốt
                </h4>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div class="bg-blue-50 p-4 rounded-lg border border-blue-100">
                        <div class="flex justify-between items-center">
                            <h5 class="font-medium text-blue-800">Thanh toán hiện hành</h5>
                            <span class="bg-blue-100 text-blue-800 px-2 py-1 rounded text-sm font-bold">1.74x</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-1">Tài sản ngắn hạn / Nợ ngắn hạn</p>
                        <p class="text-xs text-blue-600 mt-1">Đạt mức an toàn (>1.5x)</p>
                    </div>
                    <div class="bg-purple-50 p-4 rounded-lg border border-purple-100">
                        <div class="flex justify-between items-center">
                            <h5 class="font-medium text-purple-800">Vòng quay khoản phải thu</h5>
                            <span class="bg-purple-100 text-purple-800 px-2 py-1 rounded text-sm font-bold">6.89x</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-1">Doanh thu / Phải thu bình quân</p>
                        <p class="text-xs text-purple-600 mt-1">Kỳ thu tiền TB: 53 ngày</p>
                    </div>
                    <div class="bg-green-50 p-4 rounded-lg border border-green-100">
                        <div class="flex justify-between items-center">
                            <h5 class="font-medium text-green-800">Vòng quay hàng tồn kho</h5>
                            <span class="bg-green-100 text-green-800 px-2 py-1 rounded text-sm font-bold">94.67x</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-1">Giá vốn / Tồn kho bình quân</p>
                        <p class="text-xs text-green-600 mt-1">Hiệu quả quản lý tồn kho</p>
                    </div>
                    <div class="bg-yellow-50 p-4 rounded-lg border border-yellow-100">
                        <div class="flex justify-between items-center">
                            <h5 class="font-medium text-yellow-800">Biên lợi nhuận gộp</h5>
                            <span class="bg-yellow-100 text-yellow-800 px-2 py-1 rounded text-sm font-bold">2.23%</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-1">Lợi nhuận gộp / Doanh thu</p>
                        <p class="text-xs text-yellow-600 mt-1">Thấp hơn mức trung bình ngành</p>
                    </div>
                    <div class="bg-red-50 p-4 rounded-lg border border-red-100">
                        <div class="flex justify-between items-center">
                            <h5 class="font-medium text-red-800">Biên lợi nhuận ròng</h5>
                            <span class="bg-red-100 text-red-800 px-2 py-1 rounded text-sm font-bold">0.56%</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-1">Lợi nhuận sau thuế / Doanh thu</p>
                        <p class="text-xs text-red-600 mt-1">Cần cải thiện</p>
                    </div>
                    <div class="bg-indigo-50 p-4 rounded-lg border border-indigo-100">
                        <div class="flex justify-between items-center">
                            <h5 class="font-medium text-indigo-800">ROE</h5>
                            <span class="bg-indigo-100 text-indigo-800 px-2 py-1 rounded text-sm font-bold">5.18%</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-1">Lợi nhuận sau thuế / Vốn chủ sở hữu</p>
                        <p class="text-xs text-indigo-600 mt-1">Thấp hơn lãi suất ngân hàng</p>
                    </div>
                </div>
                <div class="mt-4 text-sm text-gray-600 analysis-text">
                    <p>Các chỉ số tài chính cho thấy Công ty có khả năng thanh toán ngắn hạn tốt (Current ratio 1.74x) và hiệu quả quản lý hàng tồn kho (Vòng quay 94.67x). Tuy nhiên, hiệu quả sinh lời còn thấp (ROE 5.18%, thấp hơn lãi suất ngân hàng) và phụ thuộc nhiều vào doanh thu tài chính để bù đắp chi phí quản lý. Kỳ thu tiền và trả tiền tương đương nhau (53 ngày) cho thấy chiến lược quản lý vốn lưu động phụ thuộc vào tín dụng thương mại.</p>
                </div>
            </div>
        </section>

        <!-- Detailed Analysis -->
        <section class="mb-12">
            <h3 class="text-2xl font-bold mb-6 text-dark border-b pb-2 flex items-center">
                <i class="fas fa-search-dollar mr-2 text-primary"></i> PHÂN TÍCH CHUYÊN SÂU
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Balance Sheet Analysis -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6">
                    <h4 class="font-bold text-lg mb-4 flex items-center text-blue-600">
                        <i class="fas fa-file-invoice-dollar mr-2"></i> Phân tích Bảng cân đối kế toán
                    </h4>
                    <div class="space-y-4 analysis-text">
                        <div>
                            <h5 class="font-medium flex items-center">
                                <i class="fas fa-caret-right text-blue-400 mr-1"></i> Cơ cấu tài sản ngắn hạn chiếm ưu thế
                            </h5>
                            <p class="text-sm text-gray-600 mt-1 pl-5">Tài sản của Công ty chủ yếu tập trung vào tài sản ngắn hạn (100%), trong đó các khoản phải thu chiếm tỷ trọng áp đảo (79.1% tổng tài sản). Việc không có tài sản cố định đáng kể phản ánh mô hình kinh doanh phân phối thuần túy, không đòi hỏi đầu tư lớn vào nhà xưởng, máy móc. Điều này giúp Công ty linh hoạt nhưng cũng hạn chế khả năng tạo ra lợi thế cạnh tranh dài hạn.</p>
                        </div>
                        <div>
                            <h5 class="font-medium flex items-center">
                                <i class="fas fa-caret-right text-blue-400 mr-1"></i> Khoản phải thu khách hàng ở mức cao
                            </h5>
                            <p class="text-sm text-gray-600 mt-1 pl-5">Với số dư 4.106 tỷ VNĐ (chiếm 71.3% tài sản ngắn hạn), khoản phải thu khách hàng ở mức đáng báo động. Kỳ thu tiền trung bình 53 ngày cho thấy chính sách bán chịu kéo dài, có thể do áp lực cạnh tranh hoặc chính sách tín dụng chưa hợp lý. Công ty cần rà soát chất lượng các khoản phải thu và xây dựng chính sách quản lý công nợ chặt chẽ hơn để giảm thiểu rủi ro nợ khó đòi.</p>
                        </div>
                        <div>
                            <h5 class="font-medium flex items-center">
                                <i class="fas fa-caret-right text-blue-400 mr-1"></i> Nợ phải trả chủ yếu từ nhà cung cấp
                            </h5>
                            <p class="text-sm text-gray-600 mt-1 pl-5">Cơ cấu nợ phải trả tập trung chủ yếu vào phải trả người bán (3.986 tỷ VNĐ, chiếm 95.5% tổng nợ phải trả), cho thấy Công ty đang tận dụng hiệu quả nguồn tài trợ từ nhà cung cấp. Tuy nhiên, việc phụ thuộc quá lớn vào nguồn này tiềm ẩn rủi ro khi nhà cung cấp thay đổi chính sách tín dụng. Công ty nên đa dạng hóa nguồn tài trợ để giảm thiểu rủi ro.</p>
                        </div>
                    </div>
                </div>
                
                <!-- Income Statement Analysis -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6">
                    <h4 class="font-bold text-lg mb-4 flex items-center text-green-600">
                        <i class="fas fa-chart-line mr-2"></i> Phân tích Báo cáo kết quả kinh doanh
                    </h4>
                    <div class="space-y-4 analysis-text">
                        <div>
                            <h5 class="font-medium flex items-center">
                                <i class="fas fa-caret-right text-green-400 mr-1"></i> Biên lợi nhuận gộp ở mức thấp
                            </h5>
                            <p class="text-sm text-gray-600 mt-1 pl-5">Biên lợi nhuận gộp chỉ đạt 2.23% (315.5 triệu VNĐ/14.149 tỷ VNĐ doanh thu) phản ánh áp lực cạnh tranh lớn trong ngành phân phối thiết bị điện. Giá vốn hàng bán chiếm tới 97.77% doanh thu, cho thấy Công ty đang hoạt động với biên lợi nhuận rất mỏng. Để cải thiện tình hình, Công ty cần đàm phán lại giá mua với nhà cung cấp, tìm kiếm nguồn hàng giá tốt hơn hoặc phát triển các dịch vụ giá trị gia tăng để nâng cao khả năng định giá.</p>
                        </div>
                        <div>
                            <h5 class="font-medium flex items-center">
                                <i class="fas fa-caret-right text-green-400 mr-1"></i> Chi phí quản lý vượt quá lợi nhuận gộp
                            </h5>
                            <p class="text-sm text-gray-600 mt-1 pl-5">Chi phí quản lý kinh doanh (340.9 triệu VNĐ) cao hơn lợi nhuận gộp (315.5 triệu VNĐ) là điểm đáng lo ngại. Công ty cần phân tích chi tiết từng khoản mục chi phí để xác định các vị trí có thể cắt giảm hoặc tối ưu hóa. Đặc biệt cần chú ý đến chi phí bán hàng và chi phí quản lý chung để đảm bảo hiệu quả hoạt động.</p>
                        </div>
                        <div>
                            <h5 class="font-medium flex items-center">
                                <i class="fas fa-caret-right text-green-400 mr-1"></i> Vai trò của doanh thu tài chính
                            </h5>
                            <p class="text-sm text-gray-600 mt-1 pl-5">Doanh thu hoạt động tài chính (125.1 triệu VNĐ) đóng vai trò quan trọng trong việc bù đắp một phần chi phí quản lý, giúp Công ty đạt lợi nhuận thuần từ hoạt động kinh doanh (99.8 triệu VNĐ). Tuy nhiên, việc phụ thuộc vào nguồn thu này không bền vững. Công ty nên xem xét các biện pháp tối ưu hóa quản lý tiền mặt để tăng doanh thu tài chính một cách ổn định hơn.</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Cash Flow Analysis -->
            <div class="financial-card bg-white rounded-xl shadow-md p-6 mt-6">
                <h4 class="font-bold text-lg mb-4 flex items-center text-purple-600">
                    <i class="fas fa-money-bill-wave mr-2"></i> Phân tích dòng tiền hoạt động
                </h4>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div class="bg-blue-50 p-4 rounded-lg border border-blue-200">
                        <div class="flex items-center">
                            <div class="bg-blue-100 p-2 rounded-full mr-3">
                                <i class="fas fa-money-bill-alt text-blue-600"></i>
                            </div>
                            <div>
                                <h5 class="font-medium">Tiền mặt thu vào</h5>
                                <p class="text-sm font-bold">1.565 tỷ VNĐ</p>
                                <p class="text-xs text-gray-600 mt-1">Từ hoạt động kinh doanh</p>
                            </div>
                        </div>
                    </div>
                    <div class="bg-green-50 p-4 rounded-lg border border-green-200">
                        <div class="flex items-center">
                            <div class="bg-green-100 p-2 rounded-full mr-3">
                                <i class="fas fa-exchange-alt text-green-600"></i>
                            </div>
                            <div>
                                <h5 class="font-medium">Giao dịch ngân hàng</h5>
                                <p class="text-sm font-bold">13.217 tỷ VNĐ thu / 13.212 tỷ VNĐ chi</p>
                                <p class="text-xs text-gray-600 mt-1">Quy mô lớn, dư cuối kỳ thấp</p>
                            </div>
                        </div>
                    </div>
                    <div class="bg-red-50 p-4 rounded-lg border border-red-200">
                        <div class="flex items-center">
                            <div class="bg-red-100 p-2 rounded-full mr-3">
                                <i class="fas fa-hand-holding-usd text-red-600"></i>
                            </div>
                            <div>
                                <h5 class="font-medium">Quản lý công nợ</h5>
                                <p class="text-sm font-bold">15.561 tỷ tăng / 11.616 tỷ giảm phải thu</p>
                                <p class="text-xs text-gray-600 mt-1">Luồng tiền qua công nợ lớn</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="mt-4 text-sm text-gray-600 analysis-text">
                    <p>Phân tích dòng tiền cho thấy hoạt động kinh doanh chủ yếu dựa vào luồng tiền qua ngân hàng với quy mô lớn (13.217 tỷ VNĐ thu và 13.212 tỷ VNĐ chi), nhưng số dư cuối kỳ rất thấp (5.07 triệu VNĐ). Trong khi đó, tiền mặt tồn quỹ lại ở mức cao (1.139 tỷ VNĐ), cho thấy sự chưa hợp lý trong quản lý thanh khoản. Công ty cần tối ưu hóa cơ cấu tiền mặt và tiền gửi để nâng cao hiệu quả sử dụng vốn, đồng thời tăng cường quản lý các khoản phải thu (15.561 tỷ VNĐ phát sinh tăng và 11.616 tỷ VNĐ phát sinh giảm) để cải thiện dòng tiền từ hoạt động kinh doanh.</p>
                </div>
            </div>
        </section>

        <!-- Industry Benchmarking -->
        <section class="mb-12">
            <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-indigo-500">
                <h4 class="font-bold text-lg mb-4 flex items-center text-indigo-600">
                    <i class="fas fa-industry mr-2"></i> SO SÁNH VỚI TRUNG BÌNH NGÀNH
                </h4>
                <div class="chart-container">
                    <canvas id="benchmarkChart"></canvas>
                </div>
                <div class="mt-4 text-sm text-gray-600 analysis-text">
                    <p>So với trung bình ngành phân phối thiết bị điện tại Việt Nam (theo số liệu tham khảo), Công ty có vòng quay hàng tồn kho (94.67x) cao hơn đáng kể so với mức trung bình ngành (15-20x), phản ánh hiệu quả quản lý tồn kho tốt. Tuy nhiên, biên lợi nhuận gộp (2.23%) thấp hơn nhiều so với trung bình ngành (8-12%), cho thấy áp lực cạnh tranh về giá hoặc cấu trúc chi phí chưa tối ưu. Vòng quay khoản phải thu (6.89x) tương đương trung bình ngành (6-8x), nhưng vẫn ở mức cao cần được cải thiện.</p>
                </div>
            </div>
        </section>

        <!-- SWOT Analysis -->
        <section class="mb-12">
            <h3 class="text-2xl font-bold mb-6 text-dark border-b pb-2 flex items-center">
                <i class="fas fa-clipboard-list mr-2 text-primary"></i> PHÂN TÍCH SWOT
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Strengths & Weaknesses -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-green-500">
                    <div class="flex items-center mb-4">
                        <div class="bg-green-500 text-white p-2 rounded-full mr-3">
                            <i class="fas fa-thumbs-up"></i>
                        </div>
                        <h4 class="font-bold text-lg">ĐIỂM MẠNH (STRENGTHS)</h4>
                    </div>
                    <ul class="space-y-3">
                        <li class="flex items-start">
                            <div class="bg-green-100 text-green-800 rounded-full p-1 mr-2">
                                <i class="fas fa-check text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Quy mô doanh thu lớn:</strong> Đạt 14.149 tỷ VNĐ ngay trong năm đầu hoạt động, thể hiện năng lực kinh doanh và tiếp cận thị trường tốt.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-green-100 text-green-800 rounded-full p-1 mr-2">
                                <i class="fas fa-check text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Hiệu quả quản lý tồn kho:</strong> Vòng quay hàng tồn kho 94.67x, cao hơn nhiều so với trung bình ngành, giảm thiểu chi phí lưu kho.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-green-100 text-green-800 rounded-full p-1 mr-2">
                                <i class="fas fa-check text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Cơ cấu tài chính ổn định:</strong> Không sử dụng nợ vay ngân hàng, giảm rủi ro tài chính và áp lực trả lãi.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-green-100 text-green-800 rounded-full p-1 mr-2">
                                <i class="fas fa-check text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Khả năng thanh toán tốt:</strong> Current ratio 1.74x đảm bảo khả năng đáp ứng các nghĩa vụ ngắn hạn.</span>
                        </li>
                    </ul>
                    
                    <div class="flex items-center mt-6 mb-4">
                        <div class="bg-red-500 text-white p-2 rounded-full mr-3">
                            <i class="fas fa-exclamation-triangle"></i>
                        </div>
                        <h4 class="font-bold text-lg">ĐIỂM YẾU (WEAKNESSES)</h4>
                    </div>
                    <ul class="space-y-3">
                        <li class="flex items-start">
                            <div class="bg-red-100 text-red-800 rounded-full p-1 mr-2">
                                <i class="fas fa-times text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Biên lợi nhuận cực thấp:</strong> Biên lợi nhuận gộp 2.23% và biên lợi nhuận ròng 0.56% không bền vững trong dài hạn.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-red-100 text-red-800 rounded-full p-1 mr-2">
                                <i class="fas fa-times text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Rủi ro từ khoản phải thu lớn:</strong> Phải thu khách hàng 4.106 tỷ VNĐ (71.3% tài sản ngắn hạn) với kỳ thu tiền dài (53 ngày).</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-red-100 text-red-800 rounded-full p-1 mr-2">
                                <i class="fas fa-times text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Chi phí quản lý cao:</strong> 340.9 triệu VNĐ, vượt lợi nhuận gộp, cần được tối ưu hóa cấu trúc.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-red-100 text-red-800 rounded-full p-1 mr-2">
                                <i class="fas fa-times text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Phụ thuộc vào chiếm dụng vốn:</strong> 95.5% nợ phải trả từ nhà cung cấp, rủi ro khi chính sách tín dụng thay đổi.</span>
                        </li>
                    </ul>
                </div>
                
                <!-- Opportunities & Threats -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-blue-500">
                    <div class="flex items-center mb-4">
                        <div class="bg-blue-500 text-white p-2 rounded-full mr-3">
                            <i class="fas fa-lightbulb"></i>
                        </div>
                        <h4 class="font-bold text-lg">CƠ HỘI (OPPORTUNITIES)</h4>
                    </div>
                    <ul class="space-y-3">
                        <li class="flex items-start">
                            <div class="bg-blue-100 text-blue-800 rounded-full p-1 mr-2">
                                <i class="fas fa-arrow-up text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Cải thiện quản lý công nợ:</strong> Tăng cường thu hồi nợ, áp dụng chiết khấu thanh toán sớm có thể cải thiện đáng kể dòng tiền.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-blue-100 text-blue-800 rounded-full p-1 mr-2">
                                <i class="fas fa-arrow-up text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Tối ưu hóa cấu trúc chi phí:</strong> Phân tích chi tiết các khoản mục chi phí quản lý để xác định điểm cắt giảm.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-blue-100 text-blue-800 rounded-full p-1 mr-2">
                                <i class="fas fa-arrow-up text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Đa dạng hóa nguồn hàng:</strong> Tìm kiếm nhà cung cấp mới với điều kiện giá tốt hơn để cải thiện biên lợi nhuận.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-blue-100 text-blue-800 rounded-full p-1 mr-2">
                                <i class="fas fa-arrow-up text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Phát triển dịch vụ giá trị gia tăng:</strong> Cung cấp các giải pháp tích hợp, dịch vụ sau bán hàng để nâng cao khả năng định giá.</span>
                        </li>
                    </ul>
                    
                    <div class="flex items-center mt-6 mb-4">
                        <div class="bg-yellow-500 text-white p-2 rounded-full mr-3">
                            <i class="fas fa-bolt"></i>
                        </div>
                        <h4 class="font-bold text-lg">NGUY CƠ (THREATS)</h4>
                    </div>
                    <ul class="space-y-3">
                        <li class="flex items-start">
                            <div class="bg-yellow-100 text-yellow-800 rounded-full p-1 mr-2">
                                <i class="fas fa-exclamation text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Áp lực cạnh tranh về giá:</strong> Ngành phân phối thiết bị điện có nhiều đối thủ, dễ dẫn đến chiến tranh giá.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-yellow-100 text-yellow-800 rounded-full p-1 mr-2">
                                <i class="fas fa-exclamation text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Rủi ro nợ khó đòi:</strong> Khoản phải thu lớn trong bối cảnh kinh tế khó khăn làm tăng rủi ro không thu hồi được nợ.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-yellow-100 text-yellow-800 rounded-full p-1 mr-2">
                                <i class="fas fa-exclamation text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Thay đổi chính sách nhà cung cấp:</strong> Nhà cung cấp có thể siết chặt tín dụng, ảnh hưởng đến nguồn tài trợ.</span>
                        </li>
                        <li class="flex items-start">
                            <div class="bg-yellow-100 text-yellow-800 rounded-full p-1 mr-2">
                                <i class="fas fa-exclamation text-xs"></i>
                            </div>
                            <span class="text-sm"><strong>Biến động kinh tế vĩ mô:</strong> Lạm phát, lãi suất tăng ảnh hưởng đến chi phí và nhu cầu thị trường.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Recommendations -->
        <section class="mb-12">
            <h3 class="text-2xl font-bold mb-6 text-dark border-b pb-2 flex items-center">
                <i class="fas fa-lightbulb mr-2 text-primary"></i> ĐỀ XUẤT CHIẾN LƯỢC
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Short-term -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-purple-500">
                    <h4 class="font-bold text-lg mb-4 flex items-center text-purple-600">
                        <i class="fas fa-clock mr-2"></i> Giải pháp ngắn hạn (0-6 tháng)
                    </h4>
                    <ol class="space-y-4 list-decimal list-inside">
                        <li class="font-medium">Tăng cường quản lý khoản phải thu và công nợ
                            <ul class="list-disc list-inside ml-5 font-normal text-sm text-gray-600 mt-1">
                                <li>Thiết lập hệ thống xếp hạng tín dụng khách hàng để phân loại và quản lý rủi ro</li>
                                <li>Áp dụng chính sách chiết khấu từ 2-3% cho thanh toán trước hạn để khuyến khích thu hồi nợ sớm</li>
                                <li>Xây dựng quy trình theo dõi và nhắc nợ chặt chẽ, phân công trách nhiệm cụ thể</li>
                                <li>Cân nhắc sử dụng các công cụ bảo hiểm tín dụng thương mại cho các khoản phải thu lớn</li>
                            </ul>
                        </li>
                        <li class="font-medium">Tối ưu hóa quản lý chi phí
                            <ul class="list-disc list-inside ml-5 font-normal text-sm text-gray-600 mt-1">
                                <li>Thực hiện rà soát chi tiết từng khoản mục chi phí quản lý kinh doanh</li>
                                <li>Ưu tiên cắt giảm các chi phí không trực tiếp tạo ra giá trị cho khách hàng</li>
                                <li>Áp dụng các giải pháp tiết kiệm chi phí văn phòng, logistic và quản lý</li>
                                <li>Xây dựng hệ thống KPI đo lường hiệu quả chi phí cho từng bộ phận</li>
                            </ul>
                        </li>
                    </ol>
                </div>
                
                <!-- Medium-term -->
                <div class="financial-card bg-white rounded-xl shadow-md p-6 border-t-4 border-blue-500">
                    <h4 class="font-bold text-lg mb-4 flex items-center text-blue-600">
                        <i class="fas fa-calendar-alt mr-2"></i> Chiến lược trung hạn (6-18 tháng)
                    </h4>
                    <ol class="space-y-4 list-decimal list-inside">
                        <li class="font-medium">Cải thiện cấu trúc giá và biên lợi nhuận
                            <ul class="list-disc list-inside ml-5 font-normal text-sm text-gray-600 mt-1">
                                <li>Đàm phán lại hợp đồng với nhà cung cấp hiện tại để cải thiện điều khoản giá</li>
                                <li>Tìm kiếm và phát triển quan hệ với ít nhất 2-3 nhà cung cấp mới để đa dạng nguồn hàng</li>
                                <li>Phân tích và điều chỉnh chính sách giá bán phù hợp với từng phân khúc khách hàng</li>
                                <li>Phát triển các gói dịch vụ giá trị gia tăng (lắp đặt, bảo trì, tư vấn) để nâng cao giá trị đơn hàng</li>
                            </ul>
                        </li>
                        <li class="font-medium">Đa dạng hóa nguồn tài trợ và quản lý vốn
                            <ul class="list-disc list-inside ml-5 font-normal text-sm text-gray-600 mt-1">
                                <li>Thiết lập quan hệ với các ngân hàng để có nguồn tài trợ ngắn hạn khi cần</li>
                                <li>Xây dựng kế hoạch tài chính dài hạn với các kịch bản khác nhau</li>
                                <li>Tối ưu hóa cơ cấu tiền mặt và tiền gửi để nâng cao hiệu quả sử dụng vốn</li>
                                <li>Cân nhắc các hình thức đầu tư ngắn hạn an toàn cho lượng tiền nhàn rỗi</li>
                            </ul>
                        </li>
                    </ol>
                </div>
            </div>
            
            <!-- Long-term -->
            <div class="financial-card bg-white rounded-xl shadow-md p-6 mt-6 border-t-4 border-green-500">
                <h4 class="font-bold text-lg mb-4 flex items-center text-green-600">
                    <i class="fas fa-chart-line mr-2"></i> Định hướng dài hạn (18-36 tháng)
                </h4>
                <ol class="space-y-4 list-decimal list-inside">
                    <li class="font-medium">Phát triển mô hình kinh doanh bền vững
                        <ul class="list-disc list-inside ml-5 font-normal text-sm text-gray-600 mt-1">
                            <li>Xây dựng thương hiệu và uy tín trong ngành để giảm áp lực cạnh tranh về giá</li>
                            <li>Phát triển các dòng sản phẩm/dịch vụ đặc thù có biên lợi nhuận cao hơn</li>
                            <li>Mở rộng mạng lưới khách hàng ổn định, giảm phụ thuộc vào một số ít khách hàng lớn</li>
                            <li>Đầu tư vào hệ thống quản trị và công nghệ để nâng cao hiệu quả hoạt động</li>
                        </ul>
                    </li>
                    <li class="font-medium">Nâng cao năng lực cạnh tranh
                        <ul class="list-disc list-inside ml-5 font-normal text-sm text-gray-600 mt-1">
                            <li>Phát triển đội ngũ nhân sự chuyên nghiệp, đặc biệt trong lĩnh vực quản lý tài chính và kinh doanh</li>
                            <li>Xây dựng hệ thống quản trị rủi ro toàn diện, đặc biệt rủi ro tín dụng và rủi ro thị trường</li>
                            <li>Ứng dụng công nghệ số hóa trong quản lý chuỗi cung ứng và quan hệ khách hàng</li>
                            <li>Thiết lập hệ thống giám sát và cảnh báo sớm các chỉ số tài chính then chốt</li>
                        </ul>
                    </li>
                </ol>
            </div>
        </section>

        <!-- Conclusion -->
        <section class="mb-12">
            <div class="financial-card bg-white rounded-xl shadow-md p-6 border-l-8 border-primary">
                <h3 class="text-2xl font-bold mb-4 text-dark flex items-center">
                    <i class="fas fa-file-signature mr-2 text-primary"></i> KẾT LUẬN VÀ KIẾN NGHỊ
                </h3>
                <div class="prose max-w-none analysis-text">
                    <p class="mb-4">Báo cáo phân tích toàn diện tình hình tài chính năm 2023 của Công ty TNHH Thiết bị Điện Việt Trường Thành cho thấy một bức tranh tổng thể với nhiều điểm sáng nhưng cũng không ít thách thức. Với tổng tài sản 7.252 tỷ VNĐ và doanh thu 14.149 tỷ VNĐ ngay trong năm đầu hoạt động, Công ty đã chứng minh được năng lực tiếp cận thị trường và tạo dựng quan hệ kinh doanh. Tuy nhiên, biên lợi nhuận thấp (gộp 2.23%, ròng 0.56%) cùng với khoản phải thu lớn (4.106 tỷ VNĐ) và chi phí quản lý cao (340.9 triệu VNĐ) là những vấn đề cần được ưu tiên giải quyết.</p>
                    
                    <p class="mb-4">Về cơ cấu tài chính, Công ty có khả năng thanh toán ngắn hạn tốt (Current ratio 1.74x) và hiệu quả quản lý hàng tồn kho cao (Vòng quay 94.67x). Tuy nhiên, sự phụ thuộc quá lớn vào nguồn tài trợ từ nhà cung cấp (95.5% nợ phải trả) và khoản phải thu khách hàng chiếm tỷ trọng lớn trong tài sản (71.3%) tiềm ẩn nhiều rủi ro cần được quản lý chặt chẽ.</p>
                    
                    <p class="mb-4">Để phát triển bền vững, Công ty cần tập trung vào các giải pháp đồng bộ: (1) Tăng cường quản lý công nợ và tối ưu hóa dòng tiền; (2) Cải thiện biên lợi nhuận thông qua đàm phán giá với nhà cung cấp và điều chỉnh chính sách giá bán; (3) Tối ưu hóa cơ cấu chi phí, đặc biệt là chi phí quản lý kinh doanh; (4) Đa dạng hóa nguồn tài trợ để giảm phụ thuộc vào nhà cung cấp; và (5) Phát triển các dịch vụ giá trị gia tăng để nâng cao khả năng cạnh tranh.</p>
                    
                    <p>Với việc thực hiện đồng bộ các giải pháp nêu trên cùng với việc xây dựng hệ thống quản trị tài chính chuyên nghiệp, Công ty hoàn toàn có thể cải thiện hiệu quả hoạt động, nâng cao năng lực cạnh tranh và phát triển bền vững trong những năm tiếp theo.</p>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="bg-gray-100 rounded-xl p-6 text-center border-t border-gray-200">
            <div class="flex justify-center space-x-4 mb-4">
                <a href="#" id="printBtn" class="text-gray-600 hover:text-primary transition-colors">
                    <i class="fas fa-print text-xl"></i>
                    <span class="block text-xs mt-1">In ấn</span>
                </a>
            </div>
            <p class="text-sm text-gray-600">Báo cáo được lập bởi <strong>Phòng Phân tích Tài chính</strong></p>
            <p class="text-sm text-gray-600">Ngày 29 tháng 04 năm 2025</p>
            <div class="mt-4 pt-4 border-t border-gray-200">
                <p class="text-xs text-gray-500">© 2025 CÔNG TY TNHH THIẾT BỊ ĐIỆN VIỆT TRƯỜNG THÀNH. Bảo lưu mọi quyền.</p>
                <p class="text-xs text-gray-500 mt-1">Tài liệu này chỉ dành cho mục đích nội bộ và không được phép sao chụp, phân phối mà không có sự đồng ý bằng văn bản.</p>
            </div>
        </footer>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Asset Structure Pie Chart
            const assetCtx = document.getElementById('assetPieChart').getContext('2d');
            const assetChart = new Chart(assetCtx, {
                type: 'pie',
                data: {
                    labels: ['Tiền & tương đương (15.8%)', 'Các khoản phải thu (79.1%)', 'Hàng tồn kho (4.0%)', 'Tài sản khác (1.1%)'],
                    datasets: [{
                        data: [15.8, 79.1, 4.0, 1.1],
                        backgroundColor: [
                            '#60a5fa',
                            '#3b82f6',
                            '#93c5fd',
                            '#bfdbfe'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                boxWidth: 12,
                                padding: 20
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.label + ': ' + context.raw + '%';
                                }
                            }
                        }
                    }
                }
            });

            // Capital Structure Pie Chart
            const capitalCtx = document.getElementById('capitalPieChart').getContext('2d');
            const capitalChart = new Chart(capitalCtx, {
                type: 'pie',
                data: {
                    labels: ['Nợ phải trả (57.5%)', 'Vốn chủ sở hữu (42.5%)'],
                    datasets: [{
                        data: [57.5, 42.5],
                        backgroundColor: [
                            '#10b981',
                            '#059669'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                boxWidth: 12,
                                padding: 20
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.label + ': ' + context.raw + '%';
                                }
                            }
                        }
                    }
                }
            });

            // Receivables Analysis Bar Chart
            const receivablesCtx = document.getElementById('receivablesChart').getContext('2d');
            const receivablesChart = new Chart(receivablesCtx, {
                type: 'bar',
                data: {
                    labels: ['Phải thu KH đầu kỳ', 'Phát sinh tăng', 'Phát sinh giảm', 'Phải thu KH cuối kỳ'],
                    datasets: [{
                        label: 'Giá trị (tỷ VNĐ)',
                        data: [0, 15.56, 11.62, 4.11],
                        backgroundColor: [
                            'rgba(99, 102, 241, 0.6)',
                            'rgba(99, 102, 241, 0.6)',
                            'rgba(99, 102, 241, 0.6)',
                            'rgba(99, 102, 241, 1)'
                        ],
                        borderColor: [
                            'rgba(99, 102, 241, 1)',
                            'rgba(99, 102, 241, 1)',
                            'rgba(99, 102, 241, 1)',
                            'rgba(99, 102, 241, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.raw + ' tỷ VNĐ';
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Giá trị (tỷ VNĐ)'
                            }
                        }
                    }
                }
            });

            // Payables Analysis Bar Chart
            const payablesCtx = document.getElementById('payablesChart').getContext('2d');
            const payablesChart = new Chart(payablesCtx, {
                type: 'bar',
                data: {
                    labels: ['Phải trả NB đầu kỳ', 'Phát sinh tăng', 'Phát sinh giảm', 'Phải trả NB cuối kỳ'],
                    datasets: [{
                        label: 'Giá trị (tỷ VNĐ)',
                        data: [0, 15.56, 11.62, 3.99],
                        backgroundColor: [
                            'rgba(168, 85, 247, 0.6)',
                            'rgba(168, 85, 247, 0.6)',
                            'rgba(168, 85, 247, 0.6)',
                            'rgba(168, 85, 247, 1)'
                        ],
                        borderColor: [
                            'rgba(168, 85, 247, 1)',
                            'rgba(168, 85, 247, 1)',
                            'rgba(168, 85, 247, 1)',
                            'rgba(168, 85, 247, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.raw + ' tỷ VNĐ';
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Giá trị (tỷ VNĐ)'
                            }
                        }
                    }
                }
            });

            // Profitability Trend Line Chart
            const profitabilityCtx = document.getElementById('profitabilityChart').getContext('2d');
            const profitabilityChart = new Chart(profitabilityCtx, {
                type: 'line',
                data: {
                    labels: ['Quý 1', 'Quý 2', 'Quý 3', 'Quý 4'],
                    datasets: [
                        {
                            label: 'Biên lợi nhuận gộp (%)',
                            data: [1.8, 2.0, 2.2, 2.5],
                            borderColor: 'rgba(59, 130, 246, 1)',
                            backgroundColor: 'rgba(59, 130, 246, 0.1)',
                            borderWidth: 2,
                            tension: 0.3,
                            fill: true
                        },
                        {
                            label: 'Biên lợi nhuận ròng (%)',
                            data: [0.3, 0.4, 0.5, 0.8],
                            borderColor: 'rgba(239, 68, 68, 1)',
                            backgroundColor: 'rgba(239, 68, 68, 0.1)',
                            borderWidth: 2,
                            tension: 0.3,
                            fill: true
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': ' + context.raw + '%';
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Tỷ lệ %'
                            }
                        }
                    }
                }
            });

            // Benchmarking Radar Chart
            const benchmarkCtx = document.getElementById('benchmarkChart').getContext('2d');
            const benchmarkChart = new Chart(benchmarkCtx, {
                type: 'radar',
                data: {
                    labels: ['Biên lợi nhuận gộp', 'Biên lợi nhuận ròng', 'Vòng quay tồn kho', 'Vòng quay phải thu', 'ROE'],
                    datasets: [
                        {
                            label: 'Việt Trường Thành',
                            data: [2.23, 0.56, 94.67, 6.89, 5.18],
                            backgroundColor: 'rgba(59, 130, 246, 0.2)',
                            borderColor: 'rgba(59, 130, 246, 1)',
                            borderWidth: 2,
                            pointBackgroundColor: 'rgba(59, 130, 246, 1)',
                            pointRadius: 4
                        },
                        {
                            label: 'Trung bình ngành',
                            data: [10, 3, 18, 7, 12],
                            backgroundColor: 'rgba(16, 185, 129, 0.2)',
                            borderColor: 'rgba(16, 185, 129, 1)',
                            borderWidth: 2,
                            pointBackgroundColor: 'rgba(16, 185, 129, 1)',
                            pointRadius: 4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': ' + context.raw + (context.dataIndex < 2 ? '%' : 'x');
                                }
                            }
                        }
                    },
                    scales: {
                        r: {
                            angleLines: {
                                display: true
                            },
                            suggestedMin: 0,
                            suggestedMax: 100
                        }
                    }
                }
            });

            // Animate progress bars
            const progressBars = document.querySelectorAll('.progress-fill');
            progressBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0';
                setTimeout(() => {
                    bar.style.width = width;
                }, 300);
            });
        });
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <script>
        // ...existing code...
        document.addEventListener('DOMContentLoaded', function() {
            // ...existing code...
    
            // In ấn
            document.getElementById('printBtn').addEventListener('click', function(e) {
                e.preventDefault();
                window.print();
            });
        });
    </script>
</body>
</html>"""