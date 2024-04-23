from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

def extract(link):
    options = Options()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options = options)
    driver.get(link)

    title = driver.find_element(By.TAG_NAME, "h1").text
    body = driver.find_element(By.CLASS_NAME, "td-post-content").text
    driver.close()
    return title, body

import os
file_names = ['blackassign0001', 'blackassign0002', 'blackassign0003', 'blackassign0004', 'blackassign0005', 'blackassign0006', 'blackassign0007', 'blackassign0008', 'blackassign0009', 'blackassign0010', 'blackassign0011', 'blackassign0012', 'blackassign0013', 'blackassign0014', 'blackassign0015', 'blackassign0016', 'blackassign0017', 'blackassign0018', 'blackassign0019', 'blackassign0020', 'blackassign0021', 'blackassign0022', 'blackassign0023', 'blackassign0024', 'blackassign0025', 'blackassign0026', 'blackassign0027', 'blackassign0028', 'blackassign0029', 'blackassign0030', 'blackassign0031', 'blackassign0032', 'blackassign0033', 'blackassign0034', 'blackassign0035', 'blackassign0036', 'blackassign0037', 'blackassign0038', 'blackassign0039', 'blackassign0040', 'blackassign0041', 'blackassign0042', 'blackassign0043', 'blackassign0044', 'blackassign0045', 'blackassign0046', 'blackassign0047', 'blackassign0048', 'blackassign0049', 'blackassign0050', 'blackassign0051', 'blackassign0052', 'blackassign0053', 'blackassign0054', 'blackassign0055', 'blackassign0056', 'blackassign0057', 'blackassign0058', 'blackassign0059', 'blackassign0060', 'blackassign0061', 'blackassign0062', 'blackassign0063', 'blackassign0064', 'blackassign0065', 'blackassign0066', 'blackassign0067', 'blackassign0068', 'blackassign0069', 'blackassign0070', 'blackassign0071', 'blackassign0072', 'blackassign0073', 'blackassign0074', 'blackassign0075', 'blackassign0076', 'blackassign0077', 'blackassign0078', 'blackassign0079', 'blackassign0080', 'blackassign0081', 'blackassign0082', 'blackassign0083', 'blackassign0084', 'blackassign0085', 'blackassign0086', 'blackassign0087', 'blackassign0088', 'blackassign0089', 'blackassign0090', 'blackassign0091', 'blackassign0092', 'blackassign0093', 'blackassign0094', 'blackassign0095', 'blackassign0096', 'blackassign0097', 'blackassign0098', 'blackassign0099', 'blackassign0100']
path = "/home/chilltoast/Desktop/Intern Assignment/Extracted_Text"

with open("/home/chilltoast/Desktop/Intern Assignment/Links", "r") as lnk:
    lnk_list = lnk.readlines()
    for i in range(0, len(lnk_list)):
        try:
            extracted_text = extract(lnk_list[i])
            file = os.path.join(path, file_names[i])
            with open(file, "w") as f:
                f.write(str(extracted_text))
            print("assign : ", i + 1)

        except NoSuchElementException as nse:
            continue
print("Finished")