<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://orteil.dashnet.org/experiments/cookie/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
store = driver.find_element(By.CSS_SELECTOR, value="#store")

timeout = time.time() + 1
stop = time.time() + 1 * 60
while time.time() < stop:
    cookie.click()
    if time.time() > timeout:
        money = driver.find_element(By.CSS_SELECTOR, value="#money")
        money = int(money.text.replace(",", ""))
        store = driver.find_element(By.CSS_SELECTOR, value="#store")
        max_price = 0
        prev_element = driver.find_element(By.CSS_SELECTOR, value="#store div b")
        bought_something = False
        for element in driver.find_elements(By.CSS_SELECTOR, value="#store div b"):
            print(element.text)
            price = element.text.split(" - ")[1]
            price_num = int(price.replace(",", ""))
            print(price_num)
            print(f"I have {money} cookies")
            if int(money) > price_num:
                max_price = price_num
                prev_element = element
            else:
                prev_element.click()
                bought_something = True
                break
        if not bought_something:
            prev_element.click()
        timeout = time.time() + 5

result = driver.find_element(By.CSS_SELECTOR, value="#saveMenu #cps")
print(result.text)
driver.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Optional - Keep the browser open (helps diagnose issues if the script crashes)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
#
# # Get cookie to click on.
# cookie = driver.find_element(by=By.ID, value="cookie")
#
# # Get upgrade item ids.
# items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
# item_ids = [item.get_attribute("id") for item in items]
#
# timeout = time.time() + 5
# five_min = time.time() + 60 * 5  # 5 minutes
#
# while True:
#     cookie.click()
#
#     # Every 5 seconds:
#     if time.time() > timeout:
#
#         # Get all upgrade <b> tags
#         all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
#         item_prices = []
#
#         # Convert <b> text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         # Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]
#
#         # Get current cookie count
#         money_element = driver.find_element(by=By.ID, value="money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#         # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element(by=By.ID, value=to_purchase_id).click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#     # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(by=By.ID, value="cps").text
#         print(cookie_per_s)
#         break
=======
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://orteil.dashnet.org/experiments/cookie/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
store = driver.find_element(By.CSS_SELECTOR, value="#store")

timeout = time.time() + 1
stop = time.time() + 1 * 60
while time.time() < stop:
    cookie.click()
    if time.time() > timeout:
        money = driver.find_element(By.CSS_SELECTOR, value="#money")
        money = int(money.text.replace(",", ""))
        store = driver.find_element(By.CSS_SELECTOR, value="#store")
        max_price = 0
        prev_element = driver.find_element(By.CSS_SELECTOR, value="#store div b")
        bought_something = False
        for element in driver.find_elements(By.CSS_SELECTOR, value="#store div b"):
            print(element.text)
            price = element.text.split(" - ")[1]
            price_num = int(price.replace(",", ""))
            print(price_num)
            print(f"I have {money} cookies")
            if int(money) > price_num:
                max_price = price_num
                prev_element = element
            else:
                prev_element.click()
                bought_something = True
                break
        if not bought_something:
            prev_element.click()
        timeout = time.time() + 5

result = driver.find_element(By.CSS_SELECTOR, value="#saveMenu #cps")
print(result.text)
driver.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Optional - Keep the browser open (helps diagnose issues if the script crashes)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
#
# # Get cookie to click on.
# cookie = driver.find_element(by=By.ID, value="cookie")
#
# # Get upgrade item ids.
# items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
# item_ids = [item.get_attribute("id") for item in items]
#
# timeout = time.time() + 5
# five_min = time.time() + 60 * 5  # 5 minutes
#
# while True:
#     cookie.click()
#
#     # Every 5 seconds:
#     if time.time() > timeout:
#
#         # Get all upgrade <b> tags
#         all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
#         item_prices = []
#
#         # Convert <b> text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         # Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]
#
#         # Get current cookie count
#         money_element = driver.find_element(by=By.ID, value="money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#         # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element(by=By.ID, value=to_purchase_id).click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#     # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(by=By.ID, value="cps").text
#         print(cookie_per_s)
#         break
>>>>>>> 54efe6e67173470a814e51c6d84ea55a45fb80e5
