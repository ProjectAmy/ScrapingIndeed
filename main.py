from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_option = Options()
chrome_option.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options=chrome_option)

browser.get('https://id.indeed.com/jobs?q=python+developer&l=Jakarta&from=searchOnHP&vjk=338a746b0c47660e')

pages = browser.find_elements(By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div[5]/div/div[1]/nav/ul/li/a')
print('jumlah halaman : ', len(pages)-1)
for page in pages:
    nomor = page.text
    i = 1
    if nomor:
        print(nomor)