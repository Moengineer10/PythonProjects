# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:51:19 2022

@author: moham
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
url='https://www.zappos.com/adidas-men-sneakers-athletic-shoes/CK_XARC81wFaAQHAAQLiAgQBAgsY.zso'
page_object=requests.get(url)
parsed_object=BeautifulSoup(page_object.content,'html.parser')
shoe_boxes=parsed_object.find_all('div',class_='Yl-z')
shoe_df=pd.DataFrame(columns=['Brand','Name','Price', 'Color(s) Available', 'Offers'])
for shoe in shoe_boxes:
    brand=shoe.find('span',itemprop='name').text
    name=shoe.find('dd',itemprop='name').text
    price=shoe.find('span',itemprop='price').text
    color=shoe.find('dd',itemprop='color').text
    offers=shoe.find('dd',itemprop= 'offers').text
    miniShoe=pd.DataFrame(columns=list(shoe_df.columns),data=[[brand,name,price,color,offers]])
    shoe_df=pd.concat([shoe_df,miniShoe])
    
#print(shoe_df)


