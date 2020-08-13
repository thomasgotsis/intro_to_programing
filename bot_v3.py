from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

fp = webdriver.FirefoxProfile(
    "C:\\Users\\Thomas\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\31wtuwdv.default-release")
driver = webdriver.Firefox(firefox_profile=fp)
driver.get("https://www.easports.com/fifa/ultimate-team/web-app/")
time.sleep(40)
element = driver.find_element_by_xpath("//button[@class='ut-tab-bar-item icon-transfer']")  # Botao transfer e click
element.click()
time.sleep(5)
element = driver.find_element_by_xpath("//body[@class='futweb landscape with-fifa-header']")  # search transfer market
element.click()
time.sleep(5)
element = driver.find_element_by_xpath("//input[@placeholder='Type Player Name']")  # barra de player name
player = "rony lopes"
element.send_keys(player)
time.sleep(5)
element = driver.find_element_by_xpath("//span[@class='btn-text']")  # nome do jogador na barra
element.click()
time.sleep(5)
element = driver.find_element_by_xpath("//div[3]//div[2]//input[1]")  # max bid
bid = 400
element.send_keys(bid)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action']")  # search button
element.click()
time.sleep(3)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 1
element.click()
time.sleep(2)

element = driver.find_element_by_xpath("//body[@class='futweb landscape with-fifa-header']/main["
                                       "@class='ut-root-view']/section[@class='ut-tab-bar-view "
                                       "game-navigation']/section[@class='ut-navigation-container-view']/div["
                                       "@class='ut-navigation-container-view--content']/div[@class='ut-split-view "
                                       "sidebar-right']/div[@class='ut-content']/section["
                                       "@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
                                       "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li["
                                       "2]/div[1]")
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 2
element.click()
time.sleep(2)

element = driver.find_element_by_xpath("//body[@class='futweb landscape with-fifa-header']/main["
                                       "@class='ut-root-view']/section[@class='ut-tab-bar-view "
                                       "game-navigation']/section[@class='ut-navigation-container-view']/div["
                                       "@class='ut-navigation-container-view--content']/div[@class='ut-split-view "
                                       "sidebar-right']/div[@class='ut-content']/section["
                                       "@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
                                       "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li["
                                       "3]/div[1]")
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 3
element.click()
time.sleep(2)

element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[4]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 4
element.click()
time.sleep(2)

element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[5]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 5
element.click()
time.sleep(2)
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[6]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 6
element.click()
time.sleep(2)
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[7]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 7
element.click()
time.sleep(2)
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[8]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 8
element.click()
time.sleep(2)

element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[9]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 9
element.click()
time.sleep(2)

element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[10]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 10
element.click()
time.sleep(2)

element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[11]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 11
element.click()

element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[12]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 12
element.click()

element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[13]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 13
element.click()
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[14]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 14
element.click()
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[15]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 15
element.click()
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[16]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 16
element.click()
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[17]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 17
element.click()
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[18]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 18
element.click()
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[19]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 19
element.click()
element = driver.find_element_by_xpath(
    "//body[@class='futweb landscape with-fifa-header']/main[@class='ut-root-view']/section["
    "@class='ut-tab-bar-view game-navigation']/section[@class='ut-navigation-container-view']/div["
    "@class='ut-navigation-container-view--content']/div[@class='ut-split-view sidebar-right']/div["
    "@class='ut-content']/section[@class='ut-pinned-list-container SearchResults ui-layout-left']/div["
    "@class='paginated-item-list ut-pinned-list']/ul[@class='paginated']/li[20]/div[1]")  # abaixar o cursor pro
# proximo player
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@class='btn-standard call-to-action bidButton']")  # bid 20
element.click()
