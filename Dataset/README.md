# Dataset
[Dataset và Source Code](https://drive.google.com/drive/u/0/folders/1g6_sMzaRsyTOu-aJAhpOAN0vzawcYp-Q)

# Mô tả
Dataset cho bài toán này tập trung hoàn toàn vào các biển số xe Việt Nam được nhóm tự thu thập, cắt từ các videos nhóm quay được trong quá trình tham gia giao thông và một số videos về chủ đề giao thông trên tìm kiếm được trên Youtube.

Tổng số lượng ảnh trong dữ liệu gồm $2470$ ảnh. Sau đó nhóm phân chia thành $2$ tập dữ liệu training và validation theo tỷ lệ là $8 \div 2$ tức có tổng cộng $2014$ ảnh trong tập train dùng để huấn luyện model và $456$ ảnh trong tập validation dùng để đánh giá model trong quá trình huấn luyện:
* Các file ảnh dùng để train được ghi trong file [train.txt](https://drive.google.com/file/d/12DR2KL0adW1ei1-Bsc0M6j9jxyWk0IVV/view?usp=sharing)
* Các file ảnh dùng để đánh giá được ghi trong file [val.txt](https://drive.google.com/file/d/128zgJbuI4P0jRYWcgAkLe8Coj58zTGIV/view?usp=sharing)

Trong đó có $2$ classes là biển số xe trắng  và biển số xe vàng với số lượng mỗi class là:
* Trong tập vailidation có $1075$ biển số trắng và $44$ biển số vàng
* Trong tập train có $5828$ biển số trắng và $224$ biển số vàng

Do luật về xe mang biển số vàng mới có vài năm gần đây do đó việc thu thập dữ liệu mới có sự chênh lệch lớn như vậy.
*	Cách gán nhãn là cố gắng gán nhãn đủ tất cả những biển số xe thấy rõ và có khả năng nhìn thấy xuất hiện trong ảnh. Các bouding box được bao quanh các biển số xe tức chứa các biển số xe cần nhận diện
*	Mỗi bouding box sẽ có $5$ giá trị:
	* Số đầu tiên là class id của object nằm trong bouding box:
		* $1$ là biển số vàng.
		* $0$ là biển số trắng.
	* Hai số tiếp theo là tâm của bounding box.
	* Hai số cuối cùng là chiều dài và chiều rộng của ảnh.

*Lưu ý: biểu diễn tâm và kích thước của bounding box là số thập phân thuộc đoạn $[0;1]$ vì model tính toán dựa trên tỉ lệ so với chiều dài, chiều rộng. Và các vị trí tọa độ là số thập phân trong đoạn $(0;1]$*
