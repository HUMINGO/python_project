#coding = utf-8


from basics import *

def add_user():

    login()
    driver.find_element_by_xpath('//*[@id="menus"]/li[3]/a/cite').click()
    #进入新增页面
    iframe1 = driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
    driver.switch_to.frame(iframe1)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/button[1]').click()
    time.sleep(1)
    driver.switch_to.default_content()

    iframe2 = driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
    driver.switch_to.frame(iframe2)
    driver.find_element_by_xpath('//*[@id="username-in"]').send_keys('ceshi01')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/input').send_keys("teacher01")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[3]/div/input').send_keys('123456')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/div/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/dl/dd[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[6]/div/div/div/input').click()
    driver.find_element_by_xpath('')



def edi_user():
    pass


def del_user():

    pass


def main():

    add_user()


if __name__ == '__main__':
    main()
    driver.quit()