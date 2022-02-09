Mô tả bộ dữ liệu
Bộ dữ liệu cho bài toán tập trung hoàn toàn vào các biển số xe Việt
Nam được nhóm tự thu thập, cắt khung hình từ các videos nhóm quay được
trong quá trình tham gia giao thông và một số video về chủ đề giao thông trên
youtube.
	Tổng số lượng ảnh trong dữ liệu gồm 2470 ảnh. Sau đó nhóm phân chia thành 2 tập dữ liệu train và validation theo tỷ lệ là 8:2 tức có tổng cộng 2014 ảnh trong tập train dùng để huấn luyện mô hình và 456 ảnh trong tập validation dùng để đánh giá mô hình trong quá trình huấn luyện.
	Trong đó có 2 class là biển số xe trắng  và biển số xe vàng với số lượng mỗi class là:
	Trong tập vailidation có 1075 biển số trắng và 44 biển số vàng
	Trong tập train có 5828 biển số trắng và 224 biển số vàng
Do luật về xe mang biển số vàng mới có vài năm gần đây do đó việc thu thập dữ liệu mới có sự chênh lệch lớn như vậy.
•	Cách gán nhãn là cố gắng gán nhãn đủ tất cả những biển số xe thấy rõ và có khả năng nhìn thấy xuất hiện trong ảnh. Các bouding box được bao quanh các biển số xe tức chứa các biển số xe cần nhận diện
•	Mỗi bouding box sẽ có 5 giá trị 
Số đầu tiên chỉ nhãn của đối bouding box có thể là biển số vàng 1, biển số trắng 0
2 số tiếp theo là tâm của bounding box 
2 số cuối cùng là chiều dài và chiều rộng của ảnh. Để chuẩn hoá 
