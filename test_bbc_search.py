import time
from driver_path import driver


def test_bbc_search_1():
    driver.get('https://www.bbc.com/')
    search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    search_maybe_later_button.click()
    search_input_css = driver.find_element_by_css_selector('#orb-search-q')

    print(search_input_css, "Нашел Search по CSS")
    # driver.quit()


def test_bbc_search_2():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_input_xpath = driver.find_element_by_xpath('//input[@id="orb-search-q"]')

    print(search_input_xpath, "Нашел Search по XPath")
    # driver.quit()


def test_bbc_weather_1():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_more_css = driver.find_element_by_class_name('istats-notrack')
    search_more_css.click()
    search_weather_css = driver.find_element_by_css_selector('body.wwhp-edition-international:nth-child(2) '
                                                             'div.orb-nav-pri.orb-nav-pri-white.orb-nav-dyn.orb-nav'
                                                             '-active div.orb-panel-active div.orb-panel '
                                                             'div.orb-panel-content.b-g-p.b-r.orb-nav-sec '
                                                             'ul:nth-child(2) li.orb-nav-weather > a:nth-child(1)')

    print(search_weather_css, "Погода найдена по CSS")
    # driver.quit()


def test_bbc_weather_2():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_more_css = driver.find_element_by_class_name('istats-notrack')
    search_more_css.click()
    search_weather_xpath = driver.find_element_by_xpath('//li [@class="orb-nav-weather"]')

    print(search_weather_xpath, "Погода найдена по XPath")
    # driver.quit()


def test_bbc_huge_window_1():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_huge_window_css = driver.find_element_by_css_selector('body.wwhp-edition-international:nth-child(2) '
                                                                 'div.content:nth-child(2) '
                                                                 'section.module.module--promo:nth-child(3) '
                                                                 'div.module__content ul.media-list '
                                                                 'li.media-list__item.media-list__item--1:nth-child('
                                                                 '1) '
                                                                 'div.media.media--hero.media--primary.media--overlay'
                                                                 '.block-link > a.block-link__overlay-link')

    print(search_huge_window_css, "Большое новостное окно найдено по CSS")
    # driver.quit()


def test_bbc_huge_window_2():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_huge_window_xpath = driver.find_element_by_xpath('//a [@rev="hero1|overlay"]')

    print(search_huge_window_xpath, "Большое новостное окно найдено по XPath")
    # driver.quit()


def test_bbc_even_elements_1():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_even_elements_css = driver.find_element_by_css_selector('#orb-nav-links ul :nth-child(even)')

    print(search_even_elements_css, "Четные элементы найдены по CSS")
    # driver.quit()


def test_bbc_even_elements_2():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_even_elements_xpath = driver.find_element_by_xpath(
        '//div [@class="orb-nav-section orb-nav-links orb-nav-focus"] /ul /li[position() mod 2 = 0]')

    print(search_even_elements_xpath, "Четные элементы найдены по XPath")
    # driver.quit()


def test_bbc_date_1():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_date_css = driver.find_element_by_css_selector('.module--header h2')

    print(search_date_css, "Дата найдена по CSS")
    # driver.quit()


def test_bbc_date_2():
    driver.get('https://www.bbc.com/')
    # search_maybe_later_button = driver.find_element_by_class_name('sign_in-exit')
    # search_maybe_later_button.click()
    search_date_xpath = driver.find_element_by_xpath(
        '//section [@class="module module--header"] /h2 [@class="module__title"]')

    print(search_date_xpath, "Дата найдена по XPath")
    driver.quit()
