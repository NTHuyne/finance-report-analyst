import uuid
from typing import List, Dict, Any, Optional
from src.utils.file_handler import extract_content

class MultiFileHandler:
    def __init__(self):
        self.files = []
    
    def add_file(self, file_obj, file_name: str) -> str:
        """
        Thêm một file vào danh sách xử lý
        
        Args:
            file_obj: Object file đã upload
            file_name: Tên file
            
        Returns:
            file_id: ID của file trong hệ thống
        """
        file_id = str(uuid.uuid4())
        
        # Trích xuất nội dung file
        content = extract_content(file_obj, file_name)
        
        # Thêm vào danh sách
        self.files.append({
            "file_id": file_id,
            "file_name": file_name,
            "content": content
        })
        
        return file_id
    
    def get_files(self) -> List[Dict[str, Any]]:
        """
        Lấy danh sách tất cả các file
        
        Returns:
            Danh sách thông tin file
        """
        return self.files
    
    def get_file(self, index: int) -> Optional[Dict[str, Any]]:
        """
        Lấy thông tin của một file theo chỉ số
        
        Args:
            index: Chỉ số của file
            
        Returns:
            Thông tin file hoặc None nếu chỉ số không hợp lệ
        """
        if 0 <= index < len(self.files):
            return self.files[index]
        return None
    
    def clear(self) -> None:
        """
        Xóa tất cả files
        """
        self.files = []
