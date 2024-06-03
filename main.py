from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_option = Options()
chrome_option.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options=chrome_option)

browser.get('https://id.indeed.com/jobs?q=python+developer&l=Jakarta&from=searchOnHP&vjk=be87b0982b318c85')

# mencari jumlah halaman
# pages = browser.find_elements(By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div[5]/div/div[1]/nav/ul/li/a')
# print('jumlah halaman : ', len(pages)-1)
# for page in pages:
#     nomor = page.text
#     i = 1
#     if nomor:
#         print(nomor)

# dicari

# company nama


lists = browser.find_elements(By.XPATH, '/html/body/main/div/div[2]/div/div[5]/div/div[1]/div[5]/div/ul/li')
for list in lists:

    try:
        job = list.find_element(By.TAG_NAME, 'span').text
        link = list.find_element(By.TAG_NAME, 'a').get_attribute('href')
        company = list.find_element(By.CLASS_NAME, 'css-63koeb').text
    except Exception as e:
        company = ''

    print('Job : ', job)
    print('Link : ', link)
    print('Company : ', company)
    print('\n')

browser.quit()

# lokasi = browser.find_element(By.XPATH, '/html/body/main/div/div[2]/div/div[5]/div/div[1]/div[5]/div/ul/li[1]/div/div/div/div/div/table/tbody/tr/td[1]/div[2]/div/div[1]/span').text
# print('lokasi : ', lokasi)
# for lok in lokasi:
#     loc = lok.text
#     print("Lokasi : ", loc)

