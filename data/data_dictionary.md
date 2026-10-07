# 📖 Data Dictionary - Fashion Retail Analytics

This document describes the schema, table relationships, and field definitions utilized in the **Fashion Retail Marketing & Sales Performance Analytics** dashboard.

---

## 🏗️ Data Architecture Overview

The data model follows an analytical schema with **2 Fact Tables** and **3 Dimension Tables**, linked via 1-to-Many relationships.

```mermaid
erDiagram
    dim_danh_sach_san_pham ||--o{ fact_order : "1 to Many (Mã sản phẩm)"
    dim_danh_sach_san_pham ||--o{ fact_mkt_camp_by_sku_cost : "1 to Many (Mã sản phẩm)"
    dim_mkt_camp_cost ||--o{ fact_mkt_camp_by_sku_cost : "1 to Many (Tên chiến dịch)"
    Dim_Date ||--o{ fact_order : "1 to Many (Date)"
    Dim_Date ||--o{ fact_mkt_camp_by_sku_cost : "1 to Many (Date)"
    Dim_Date ||--o{ dim_mkt_camp_cost : "1 to Many (Date)"

    fact_order {
        string ID PK "Mã đơn hàng duy nhất"
        datetime Thoi_gian "Thời điểm đặt hàng"
        string Nguon "Kênh bán hàng (Admin/Online)"
        string Ma_khach_hang "ID định danh khách hàng"
        string Cap_do_khach_hang "Phân khúc khách hàng"
        string San_pham "Tên sản phẩm"
        string Ma_san_pham FK "SKU ID (Khóa ngoại sang Product Dim)"
        string Danh_muc_san_pham "Danh mục ngành hàng"
        decimal Gia "Doanh thu bán ra (Gross Revenue)"
        int So_luong "Số lượng sản phẩm đặt"
        decimal Gia_von "Giá vốn hàng bán (COGS)"
        decimal Chiet_khau "Giá trị chiết khấu áp dụng"
        string Trang_thai "Trạng thái đơn hàng"
    }

    fact_mkt_camp_by_sku_cost {
        string Ten_chien_dich FK "Tên chiến dịch quảng cáo"
        date Ngay "Ngày ghi nhận chi phí"
        string Ma_san_pham FK "Mã SKU chạy ads"
        string Ten_san_pham "Tên SKU chạy ads"
        decimal Tien_da_chay "Chi phí quảng cáo phân bổ theo SKU"
        decimal Ngan_sach "Ngân sách quảng cáo ấn định"
        int Inbox "Số lượng tin nhắn phát sinh từ ads"
        int Comments "Số lượng bình luận bài viết ads"
        int Impressions "Lượt hiển thị bài viết ads"
        int SL_ban_theo_Campaign "Số lượng bán quy đổi từ chiến dịch"
    }

    dim_mkt_camp_cost {
        string Ten_chien_dich PK "Tên chiến dịch marketing"
        date Ngay "Ngày triển khai"
        decimal So_tien_da_chi_tieu "Tổng chi phí thực chi (VND)"
        decimal Ngan_sach_chien_dich "Ngân sách phê duyệt (VND)"
        string Loai_ngan_sach "Daily Budget hoặc Lifetime Budget"
        decimal CPM "Chi phí trên mỗi 1.000 lượt hiển thị"
        decimal CPC "Chi phí trên mỗi lượt nhấp chuột (Click)"
        int Luot_hien_thi "Tổng lượt hiển thị (Impressions)"
        int Click "Tổng lượt nhấp chuột"
    }

    dim_danh_sach_san_pham {
        string Ma_san_pham PK "Mã SKU duy nhất"
        string Ten_san_pham "Tên gọi chính thức của sản phẩm"
        string Danh_muc "Danh mục phân loại (Dress, Shirt, Pants...)"
        string Thuong_hieu "Thương hiệu sản phẩm"
        string Mau_sac "Màu sắc sản phẩm"
        string Chat_lieu "Chất liệu may mặc"
        decimal Gia_nhap "Giá mua vào ban đầu"
        decimal Gia_ban "Giá niêm yết bán lẻ"
        decimal Gia_von "Giá thành sản xuất / vốn lưu kho"
        string Trang_thai "Tình trạng kinh doanh (Active/Discontinued)"
    }

    Dim_Date {
        date Date PK "Ngày chuẩn định dạng YYYY-MM-DD"
        int Year "Năm"
        int Month "Tháng (1-12)"
        string MonthName "Tên tháng"
        int Day "Ngày trong tháng (1-31)"
        int Week "Tuần trong năm (1-52)"
        int WeekOfMonth "Tuần trong tháng (1-5)"
        string DayOfWeek "Thứ trong tuần"
    }
```

---

## 📋 Chi tiết các bảng dữ liệu

### 1. `fact_order` (Bảng giao dịch đơn hàng)
* **Grain (Độ hạt):** 1 dòng = 1 SKU trong đơn hàng được tạo.
* **Thời gian ghi nhận:** 01/05/2024 – 31/05/2024.
* **Quy mô:** 3,451 dòng giao dịch, 2,858 đơn hàng thành công.
* **Mục đích:** Tính toán tổng doanh thu toàn doanh nghiệp (`Total Revenue`), số lượng đơn hàng (`Total Orders`), giá trị trung bình đơn hàng (`AOV`), và đối chiếu với doanh thu tạo ra từ quảng cáo.

### 2. `fact_mkt_camp_by_sku_cost` (Bảng chi phí marketing phân bổ theo SKU)
* **Grain:** 1 dòng = 1 SKU được chạy quảng cáo trong 1 chiến dịch theo từng ngày.
* **Mục đích:** Cung cấp độ sâu phân tích ở cấp độ sản phẩm (SKU-level attribution), giúp đánh giá sản phẩm nào chạy ads hiệu quả nhất.

### 3. `dim_mkt_camp_cost` (Bảng tổng hợp chi phí chiến dịch)
* **Grain:** 1 dòng = 1 chiến dịch marketing theo ngày.
* **Mục đích:** Theo dõi ngân sách (`MKT Budget`), chi phí thực tế (`MKT Spend`), tỷ lệ sử dụng ngân sách (`% Budget Utilization`), và các chỉ số phễu marketing (`CPM`, `CPC`, `CTR`, `Impressions`, `Clicks`).

### 4. `dim_danh_sach_san_pham` (Danh mục sản phẩm)
* **Grain:** 1 dòng = 1 SKU định danh.
* **Mục đích:** Phân tích hiệu suất theo danh mục (`Category`), phân loại sản phẩm chủ lực (Hero Products) vs sản phẩm thứ cấp.

### 5. `Dim_Date` (Bảng thời gian chuẩn)
* **Mục đích:** Hỗ trợ tính toán Time Intelligence (so sánh theo tuần WoW, theo tháng MoM) và đồng bộ trục thời gian giữa doanh số bán lẻ và chi tiêu marketing.
