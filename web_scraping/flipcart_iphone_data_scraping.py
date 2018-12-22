"""
Created on saturday December 22 15:32:22 2018
@author: Ravi
Project on Web scraping :Scraping the Product_name,Price and Rating of phone from E-commerce Flipkart
"""

from bs4 import BeautifulSoup as soup                   #importing BeautifulSoup from bs4 package rename as soup
from urllib.request import urlopen                      #importing urlopen from urllib package


url="https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_2&otracker1=AS_QueryStore_OrganicAutoSuggest_0_2&as-pos=0&as-type=RECENT&as-backfill=on"
client=urlopen(url)                                          #it take the data from my_url and tightly load in client variable
html_page=client.read()                                      #it client.red() read the data and store in variable html-page()
client.close()                                               #it close connection;
page_soup=soup(html_page,"html.parser")                        #it parse the web page into html page


containers=page_soup.find_all("div",{"class":"_3O0U0u"})       #it find all the div tag who has class and  name of:"_3O0U0u"
# print(len(containers))                                        #print the number of item in containers
#print(soup.prettify(containers[0]))                           #arrange the html code in structue formate

container=containers[0]                                       #variable cointainer contain  first  phone  data
name= container.div.img['alt']                                  #name variable contain name of first phone
#print(name)                                                     # display name of first phone

price=container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})          #price contain the price of all iphone
#print(price[0].text)                                             #it display the price of phone and "text" is used to display only text not tags

rating=container.findAll("div",{"class","niH0FQ"})                     #rating of first iphone
#print(rating[0].text)                                                   #it display the rating of phone and "text" is used to display only text not tags

filename="product.csv"                                           # creating the file and name it product.csv
f=open(filename,"w")                                              #open the file in writing mode

headers="Product_name,Price,Rating\n"
f.write(headers)


for container in containers:                                                                 # loop for extracting the nproduct_name,price,rating of all phones

    product_name = container.div.img['alt']
    price = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
    price=price[0].text
    rating = container.findAll("div", {"class", "niH0FQ"})
    rating=rating[0].text


    #string parsing
    trim_price="".join(price.split(","))                                                        # first split on ", " than joining on blackspace " "
    trim_rupee = trim_price.split("₹")                                                          #spliting on the base "₹"
    final_price="Rs."+trim_rupee[1]                                                             #adding Rs. to price

    final_rating=rating[0:3]                                                                    #slicing in to rating to separate rating

    product_name = product_name.replace(",", "|")                                                #it replace "," with "|"
    print(product_name+","+final_price+","+final_rating+"\n")                                    # display the final product_name,price,rating
    f.write(product_name+","+final_price+","+final_rating+"\n")                                  # writing the data in csv file





