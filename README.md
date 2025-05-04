# 🏡 Lấy dữ liệu trang Web - 123nhadatviet.com

## Giới thiệu dự án

Dự án Python này giúp tự động thu thập dữ liệu **Cho thuê nhà riêng** từ trang web bất động sản [123nhadatviet.com](https://123nhadatviet.com/), xuất và lưu tất cả các dữ liệu vào file Excel. Dữ liệu bao gồm hình ảnh, tiêu đề, mô tả, giá, hướng, diện tích, địa chỉ và ngày đăng tin.

---

## Tính năng

- Tự động truy cập vào trang web 123nhadatviet.com, chuyên mục "Nhà đất cho thuê", tự động chọn "Cho thuê nhà riêng".

- Tự động trích xuất dữ liệu của từng mục nhà, đất trong 10 trang đầu tiên.

- Nếu dữ liệu bị thiếu hoặc chưa lấy được sẽ hiển thị thông báo.

- Lưu và trích xuất dữ liệu vào file Excel.

- Cài đặt việc lên lịch để tự lấy và xuất dữ liệu tự động vào lúc 6:00 sáng hàng ngày.

---

## Yêu cầu hệ thống

- Phiên bản Python 3.7 trở lên.
- Sử dụng trình duyệt Google Chrome để lấy dữ liệu.

---

## Thư viện cần cài đặt

Cài đặt tất cả thư viện cần thiết bằng lệnh:

```bash
pip install selenium pandas schedule openpyxl
```

## Trong đó:

- Thư viện Selenium: Là một công cụ mạnh dùng để tự động hóa trình duyệt Web. Nó cho phép bạn điều khiển trình duyệt như một người dùng thật.

- Thư viện Pandas: Được sử dụng trong thao tác dữ liệu, là công cụ phân tích và xử lý dữ liệu mạnh mẽ của ngôn gữ lập trình Python.

- Thư viện Schedule: Đây là một thư viện rất phổ biến dùng để lập lịch chạy các tác vụ (jobs) theo thời gian.

- Thư viện Openpyxl: Thư viện openpyxl trong Python là một thư viện dùng để đọc, ghi và chỉnh sửa các tập tin Excel có định dạng .xlsx (Excel 2007 trở lên). Nó cho phép bạn làm việc với bảng tính Excel một cách linh hoạt.
