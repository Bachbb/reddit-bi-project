# 📊 Reddit BI Project

Dự án phân tích dữ liệu mạng xã hội Reddit phục vụ mục tiêu Business Intelligence — đánh giá mức độ quan tâm và cảm xúc của người dùng thông qua các bài viết trên Reddit.

---

## 🎯 Mục tiêu

- Thu thập và làm sạch dữ liệu bình luận từ Reddit
- Phân tích cảm xúc (Sentiment Analysis) theo thời gian
- Xác định các chủ đề được nhắc đến nhiều nhất
- Trực quan hóa kết quả qua dashboard Power BI

---

## 🛠️ Công cụ sử dụng

| Công cụ | Mục đích |
|---|---|
| Python | Xử lý & làm sạch dữ liệu, trích xuất từ khóa |
| MySQL | Lưu trữ và truy vấn dữ liệu |
| Power BI | Xây dựng dashboard trực quan |
| GitHub | Quản lý mã nguồn |

---

## 📁 Cấu trúc thư mục

```
reddit-bi-project/
│
├── reddit_Emotion/              # Phân tích cảm xúc (Sentiment Analysis)
│   ├── emotionreddit.pbix       # File Power BI dashboard cảm xúc
│   ├── reddit_emotion.csv       # Dữ liệu cảm xúc đã xử lý
│   ├── reddit_emotion.py        # Script phân tích & làm sạch cảm xúc
│   └── redditemotion.png        # Ảnh dashboard cảm xúc
│
├── reddit_keywords/             # Phân tích từ khóa & chủ đề
│   ├── clean_reddit_keywords.py # Script trích xuất & làm sạch từ khóa
│   ├── keywordsreddit.pbix      # File Power BI dashboard từ khóa
│   ├── reddit_keywords.csv      # Danh sách từ khóa đã làm sạch
│   └── redditkeywords.png       # Ảnh dashboard từ khóa
│
├── reddit_bi/                   # Database MySQL
│   ├── reddit_keywords.ibd      # File dữ liệu bảng keywords
│   └── reddit_reviews.ibd       # File dữ liệu bảng reviews
│
├── redditDataset.pkl            # Dataset gốc (pickle format)
├── final_report(BI)-group12.pdf # Báo cáo cuối kỳ
└── README.md
```

---

## 🗄️ Cơ sở dữ liệu

### Bảng `reddit_reviews`
| Cột | Kiểu | Mô tả |
|---|---|---|
| review_id | INT | Khóa chính tự tăng |
| text_content | TEXT | Nội dung bài viết |
| subreddit | VARCHAR | Tên subreddit (humor / news) |
| sentiment | VARCHAR | Cảm xúc (Positive / Negative / Neutral) |
| rating | INT | Điểm đánh giá (1-5) |
| review_date | DATETIME | Ngày đăng bài |

### Bảng `reddit_keywords`
| Cột | Kiểu | Mô tả |
|---|---|---|
| id | INT | Khóa chính tự tăng |
| keyword | VARCHAR | Từ khóa |
| count | INT | Số lần xuất hiện |
| subreddit | VARCHAR | Nhóm (All / humor / news) |
| rank_order | INT | Xếp hạng trong nhóm |

---

## 📊 Dashboard Power BI

Dashboard bao gồm các visual:

- **Tổng quan** — Tổng số bài viết, tổng rating, phân bố cảm xúc (Pie chart)
- **Xu hướng cảm xúc** — Line chart 3 đường Positive / Negative / Neutral theo tháng
- **Chủ đề quan tâm** — Bar chart / Word Cloud top từ khóa được nhắc nhiều nhất
- **Phân tích theo subreddit** — So sánh r/humor vs r/news
- **Lọc dữ liệu** — Slicer theo sentiment, subreddit, khoảng thời gian

---

## ⚙️ Hướng dẫn chạy

### 1. Làm sạch & xử lý dữ liệu
```bash
# Phân tích cảm xúc
python reddit_Emotion/reddit_emotion.py

# Trích xuất từ khóa
python reddit_keywords/clean_reddit_keywords.py
```

### 2. Import vào MySQL
```sql
source reddit_bi/database_reddit.sql
```

### 3. Kết nối Power BI
- Get data → MySQL database
- Host: `localhost` | Port: `3306` | Database: `reddit_bi`
- Username: `root`
## 👥 Nhóm thực hiện

Bài tập lớn môn Business Intelligence — Nhóm 12
