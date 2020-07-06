from selenium import webdriver
from bs4 import BeautifulSoup
import time

print("login_page:- for go through login_mail_id and password:")
print("facbook:- for go through facbook:")

through_input = input("enter through_input:-").lower()

driver = webdriver.Chrome("chromedrive_64/chromedriver")
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
driver.maximize_window()
time.sleep(5)

if through_input == "login_page":
	email = driver.find_element_by_name("username").send_keys(input("enter the email or phone_number:-"))
	pass_word = driver.find_element_by_name("password").send_keys(input("enter your password:-"))
	login_button = driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()
elif through_input ==  "facebook":
	face_book = driver.find_element_by_xpath('//span[@class="KPnG0"]').click()
	email_id = driver.find_element_by_id("email").send_keys(input("enter the email_id:-"))
	password = driver.find_element_by_id("pass").send_keys(input("enter password:-"))
	login_button = driver.find_element_by_id("loginbutton").click()
	time.sleep(10)
	pop_up = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
	time.sleep(5)

	
	#get into the profile page :-
	profile_page = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
	time.sleep(5)
	#soup for profile page:-
	response1 = driver.execute_script("return document.documentElement.outerHTML")
	soup1 =BeautifulSoup(response1,"html.parser")
	all_posts = soup1.find_all("div",class_="Nnq7C weEfm")
	dict_for_posts_info = {}
	for i in all_posts:
		div_tag = i.find_all("div",class_="KL4Bh")
		for j in div_tag:
			img_tag= j.find("img")
			dict_for_posts_info[str(img_tag["alt"])] = img_tag["srcset"]
	print(dict_for_posts_info)

	# finding profile information 
	dict_of_profile_info = {}
	count = 0
	main_ul_for_profile_page = soup1.find("ul",class_="k9GMp")
	all_li_tags = main_ul_for_profile_page.find_all("li",class_="Y8-fY")
	for i in all_li_tags:
		count+=1
		if count == 1:
			span1 = i.find("span",class_="-nal3").text
			dict_of_profile_info["no_of_posts"] = str(span1)	
		elif count == 2:
			anchore_tag = i.find("a",class_="-nal3").text
			dict_of_profile_info["followers"] = str(anchore_tag)
		else:
			anchore_tag = i.find("a",class_="-nal3").text
			dict_of_profile_info["following"] = str(anchore_tag)
	print(dict_of_profile_info)


	
	# #followers names and following names
	list_of_followers = []
	var_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
	time.sleep(5)
	response_followers = driver.execute_script("return document.documentElement.outerHTML")
	soup_followers =BeautifulSoup(response_followers,"html.parser")
	var_main_div = soup_followers.find("div",class_="PZuss")
	li_tags = var_main_div.find_all("li")
	for i in li_tags:
		followers_name =i.find("a")
		list_of_followers.append(followers_name["href"])
	print(list_of_followers)
	closing_of_followers_page = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
	time.sleep(5)


	#finding following of mine:-
	list_of_following = []
	var_following = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
	time.sleep(5)
	response_following = driver.execute_script("return document.documentElement.outerHTML")
	soup_following =BeautifulSoup(response_following,"html.parser")
	var_main_div2 = soup_following.find("div",class_="PZuss")
	li_tags2 = var_main_div2.find_all("li")
	for i in li_tags2:
		following_name =i.find("a")
		list_of_following.append(following_name["href"])
	print(list_of_following)
	closing_of_following_page = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
	time.sleep(5)





















