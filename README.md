# AI Research Journey — 7 Days

Một website giáo trình tự học tiếng Việt, dạng sách trực tuyến, cho sinh viên CNTT mới biết C/C++ và chưa học Python/ML.

**Website có sẵn 7 chương**, mục lục, giao diện responsive, chế độ sáng/tối, tìm chương, tiến độ localStorage, tài liệu tham khảo và 4 ví dụ Python.

> Đây là dự án biên soạn độc lập, lấy cảm hứng từ *kiểu trình bày sách có mục lục* của https://lenbui.github.io/bookai/. Không sao chép nội dung/mã nguồn của giáo trình gốc. Không liên kết chính thức với tác giả giáo trình hay các giảng viên được đề cập.

## 1. Xem thử trên máy

- Giải nén ZIP.
- Mở `index.html` trong Chrome, Edge hoặc Firefox.
- Chọn **Ngày 1** từ mục lục.

Không cần Node.js, Python hoặc server để xem website. Python chỉ dùng cho các ví dụ nghiên cứu (nên chạy trên Google Colab).

## 2. Đăng GitHub Pages (giao diện GitHub)

1. Truy cập https://github.com/new và tạo repository public, ví dụ `ai-research-7days`.
2. Chọn **Add file → Upload files**, upload **toàn bộ nội dung bên trong thư mục** `ai-research-7days` (giữ nguyên các thư mục `assets/`, `examples/`, `notes/` và `.github/`). Không upload chỉ file ZIP.
3. Chọn **Commit changes**.
4. Vào **Settings → Pages → Build and deployment**.
5. Chọn **Source: Deploy from a branch**, **Branch: main**, **Folder: / (root)**, rồi **Save**.
6. Đợi GitHub triển khai; trang sẽ có địa chỉ `https://TEN-TAI-KHOAN.github.io/ai-research-7days/` nếu tên repo như ví dụ.

Để đơn giản, site dùng đường dẫn tương đối, vì vậy hoạt động cả khi repo có tên khác. Không cần GitHub Actions.

## 3. Đăng bằng Git

```bash
git init
git add .
git commit -m "Publish AI Research Journey 7 Days"
git branch -M main
git remote add origin https://github.com/USERNAME/ai-research-7days.git
git push -u origin main
```

Sau đó kích hoạt Pages như mục 2.

## 4. Cấu trúc

```text
ai-research-7days/
├── index.html              # Trang chủ
├── day01.html ... day07.html
├── assets/
│   ├── style.css           # Giao diện
│   └── app.js              # Theme / mục lục / tiến độ
├── examples/
│   ├── day02_python_basics.py
│   ├── day03_linear_model.py
│   ├── day04_classification.py
│   └── day05_neural_network.py
├── notes/
│   ├── day01-research-map.md
│   ├── day06-paper-template.md
│   └── day07-mini-project.md
├── .nojekyll
├── LICENSE
└── README.md
```

## 5. Chỉnh sửa

- Nội dung chương: sửa `day01.html` ... `day07.html`.
- Màu chữ/giao diện: sửa `assets/style.css`.
- Điều hướng và lưu tiến độ: sửa `assets/app.js`.
- Để cá nhân hóa, thay tên sách, tác giả, thông tin giới thiệu trực tiếp trong HTML.
- **Lưu ý:** trạng thái hoàn thành được lưu trong `localStorage` trên trình duyệt, không đồng bộ giữa máy và không tự ghi vào repository.

## 6. Chạy ví dụ Python

Mở https://colab.research.google.com/ → New notebook → copy nội dung từng file trong `examples/` vào một cell → Run. Các ví dụ ngày 4–5 cần `scikit-learn` (thường có sẵn trong Colab; nếu chưa có chạy `!pip install scikit-learn`).

## 7. Giới hạn của giáo trình

Đây là **lộ trình khám phá**, không phải chứng chỉ hay khóa đào tạo đầy đủ về ML. Trong 7 ngày không thể học xong backpropagation, xác suất thống kê hay tái lập một nghiên cứu quy mô lớn. Các ví dụ minh họa là bài tập, không phải kết quả nghiên cứu mới.

## Nguồn học thêm

- https://course.elementsofai.com/1
- https://developers.google.com/machine-learning/intro-to-ml
- https://docs.python.org/3/tutorial/
- https://scikit-learn.org/stable/
- https://scholar.google.com/
- https://www.semanticscholar.org/

## License

Mã nguồn và văn bản biên soạn riêng trong dự án này được phát hành theo giấy phép MIT, xem `LICENSE`. Nội dung liên kết ngoài thuộc chủ sở hữu tương ứng.
