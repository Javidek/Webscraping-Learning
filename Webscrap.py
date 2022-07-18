import requests
from bs4 import BeautifulSoup

def webscarping(mydb):
    for itera in range(1,300):
        req=requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page=%i'% itera)
        soup=BeautifulSoup(req.text,'html.parser')
        temp=soup.find_all('div',attrs={'class':"card-content vehicle-card-body order-3 vehicle-card-challenger-body",'data-test':"cardContent"})
        for item in temp:
            name_car=item.find('span',attrs={'class':'vehicle-header-make-model text-truncate'}).text.split(' ')
            Product_c_year=item.find('span',attrs={'class':'vehicle-card-year font-size-1'}).text
            accident_car=item.find('div',attrs={'data-test':'vehicleCardCondition'}).text.split(' ')
            price_car=item.find('div',attrs={'data-test':'vehicleCardPricingBlockPrice'})
            miles_car=item.find('div',attrs={'data-test':'vehicleMileage'}).text.split(' ')
            namecar=str(name_car[0])
            model=str(name_car[1])
            Product_c=int(Product_c_year)
            miles=int(miles_car[0].replace(',',''))
            if accident_car[0]== ('No' or 'no'):
                    accident=0
            else:
                    accident=int(accident_car[0])
            if price_car != None:
                price=int(price_car.text[1:].replace(',',''))
            else:
                break
            mycursor = mydb.cursor()
            mycursor.execute('INSERT INTO Info_car VALUES (\'%s\',\'%s\',\'%i\',\'%i\',\'%i\',\'%i\')'
                    %(namecar,model,miles,accident,Product_c,price))
            mydb.commit()