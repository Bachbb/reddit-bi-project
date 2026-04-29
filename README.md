# Reddit BI Project

## Giới thiệu
Dự án phân tích dữ liệu bình luận trên Reddit bằng Python, MySQL và Power BI.

## Công cụ sử dụng
- Python / Google Colab: xử lý dữ liệu ETL
- MySQL Workbench: lưu trữ và truy vấn dữ liệu
- Power BI: xây dựng dashboard
- GitHub: lưu trữ source code và báo cáo

## Dataset
Dữ liệu gồm các bình luận Reddit sau khi xử lý, bao gồm các cột:
- review_id
- text_content
- subreddit
- sentiment
- rating
- review_date

## Các file trong project
- `etl_reddit.py`: Code Python xử lý dữ liệu
- `database_reddit.sql`: Code SQL tạo database, bảng và truy vấn
- `reddit_cleaned.csv`: Dataset sau xử lý
- `baocaoBI.pdf`: Báo cáo bài tập

## Quy trình thực hiện
1. Đọc dữ liệu Reddit bằng Python
2. Làm sạch dữ liệu và tạo thêm các trường phân tích
3. Import dữ liệu vào MySQL
4. Truy vấn dữ liệu bằng SQL
5. Xây dựng dashboard bằng Power BI
6. Phân tích insight và viết báo cáo

## Dashboard Insights
- Phần lớn bình luận có sentiment tích cực
- Rating cao chiếm tỷ lệ lớn
- Có thể lọc dữ liệu theo sentiment và thời gian
- Dashboard hỗ trợ quan sát xu hướng review theo thời gian
