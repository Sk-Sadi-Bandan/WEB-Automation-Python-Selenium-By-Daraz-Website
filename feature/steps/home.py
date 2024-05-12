from selenium import webdriver
import time 
from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(U'Go to Website')
def open_daraz(context):
    context.driver= webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.daraz.com.bd/")
    time.sleep(1)


# Scenario 1
@when(U'Check that search option is displayed')
def step_impl1(context):
    context.driver.find_element(By.XPATH, "//input[@id='q']")
    time.sleep(2)

@Then(U'Click on search option')
def step_impl2(context):
    context.driver.find_element(By.XPATH, "//input[@id='q']").click()

@when(U'Input any product name')
def step_impl3(context):
    context.driver.find_element(By.XPATH, "//input[@id='q']").send_keys('Laptop')
    time.sleep(2)

@Then(U'Check that search icon is displayed')
def step_impl4(context):
    context.driver.find_element(By.XPATH, "//button[@class='search-box__button--1oH7']")
    time.sleep(2)

@When(U'Click on search icon')
def step_impl5(context):
    context.driver.find_element(By.XPATH, "//button[@class='search-box__button--1oH7']").click()

@Then(U'Check that Lenovo laptop is displayed')
def step_impl6(context):
    context.driver.find_element(By.XPATH, "//div[@class='ant-col-19 ant-col-push-5 side-right--Tyehf']//div[1]//div[1]//a[1]//div[1]//img[1]")
    time.sleep(2)

@When(U'Click on Lenovo laptop')
def step_impl7(context):
    context.driver.find_element(By.XPATH, "//div[@class='ant-col-19 ant-col-push-5 side-right--Tyehf']//div[1]//div[1]//a[1]//div[1]//img[1]").click()

@Then(U'Check that add to cart button is displayed')
def step_impl8(context):
    context.driver.find_element(By.XPATH, "//button[contains(@class,'pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl')]")
    time.sleep(2)

@When(U'Click on add to cart button')
def step_impl9(context):
    context.driver.find_element(By.XPATH, "//button[contains(@class,'pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl')]").click()

@Then(U'Check that go to cart button is displayed')
def step_impl10(context):
    context.driver.find_element(By.XPATH, "//button[@type='button']")
    time.sleep(2)

@When(U'Click on go to cart button')
def step_impl11(context):
    context.driver.find_element(By.XPATH, "//button[@type='button']").click()

@Then(U'Check that proceed to checkout button is displayed')
def step_impl12(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT (1)']")
    time.sleep(2)

@When(U'Click on proceed to checkout button')
def step_impl13(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT (1)']").click()



# Scenario 2
@when(U'Check that login option is displayed')
def step_impl1(context):
    context.driver.find_element(By.XPATH, "//ul[@id='anonLoginNew']//span[@class='holder']")
    time.sleep(2)

@Then(U'Click on Login option')
def step_impl2(context):
    context.driver.find_element(By.XPATH, "//ul[@id='anonLoginNew']//span[@class='holder']").click()

@when(U'Input Email')
def step_impl3(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Please enter your Phone Number or Email']").send_keys('sadi1.qups@gmail.com')
    time.sleep(2)

@Then(U'Input Password')
def step_impl4(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Please enter your password']").send_keys('#Sadi313')
    time.sleep(2)

@when(U'Check that Login option is displayed')
def step_impl5(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']")
    time.sleep(2)

@Then(U'Click on Login option')
def step_impl6(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
