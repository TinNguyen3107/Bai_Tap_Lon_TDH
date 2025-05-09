from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import schedule

def du_lieu():

    driver = webdriver.Chrome()
    driver.get("https://123nhadatviet.com/")
    time.sleep(3)

    cho_thue = driver.find_element(By.XPATH, '//*[@id="ctl00_mainmenu"]/li[3]/a')
    ActionChains(driver).move_to_element(cho_thue).perform()
    time.sleep(2)

    nha_rieng = driver.find_element(By.XPATH, '//*[@id="ctl00_mainmenu"]/li[3]/ul/li[2]/a')
    nha_rieng.click()
    time.sleep(3)

    data = []
    
    # for page in range(1, 11):
    #     if page > 1:
    #         driver.get(f"https://123nhadatviet.com/rao-vat/cho-thue/nha-rieng/trang--{page}.html")
    #         time.sleep(3)
    
    page = 1

    while True:
        if page > 1:
            driver.get(f"https://123nhadatviet.com/rao-vat/cho-thue/nha-rieng/trang--{page}.html")
            time.sleep(3)

        danh_sach = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div')

        if not danh_sach:
            print(f"Không tìm thấy bài đăng ở trang {page}, dừng lại.")
            break

        for bai_dang in danh_sach:
            try:
                try:
                    image = bai_dang.find_element(By.XPATH, './/div[1]/a/img').get_attribute('src')
                except:
                    image = "Không có ảnh"

                try:
                    title = bai_dang.find_element(By.CLASS_NAME, 'ct_title').text
                except:
                    title = "Không có tiêu đề"
                
                try:
                    description = bai_dang.find_element(By.CLASS_NAME, 'ct_brief').text
                except:
                    description = "Không có mô tả"
                
                try:
                    price = bai_dang.find_element(By.CLASS_NAME, 'ct_price').text
                except:
                    price = "Không có giá"
                
                try:
                    direct = bai_dang.find_element(By.CLASS_NAME, 'ct_direct').text
                except:
                    direct = "Không có hướng"

                try:
                    area = bai_dang.find_element(By.CLASS_NAME, 'ct_dt').text
                except:
                    area = "Không có diện tích"
                
                try:
                    address = bai_dang.find_element(By.CLASS_NAME, 'ct_dis').text
                except:
                    address = "Không có địa chỉ"

                try:
                    date = bai_dang.find_element(By.CLASS_NAME, 'ct_date').text
                except:
                    date = "Không có ngày đăng"

                data.append([image, title, description, price, direct, area, address, date])

            except Exception as e:
                print("Lỗi khi lấy bài:", e)
        
        page += 1

    df = pd.DataFrame(data, columns=["Ảnh", "Tiêu đề", "Mô tả", "Giá", "Hướng", "Diện tích", "Địa chỉ", "Ngày đăng"])
    df.to_excel(r"D:\BaiTap\Tu_Dong_Hoa\BaiTapLon\cho_thue_nha_rieng.xlsx", index=False)

    driver.quit()
    print("Đã lưu dữ liệu")

# du_lieu()
schedule.every().day.at("06:00").do(du_lieu)

while True:
    schedule.run_pending()
    time.sleep(10)
