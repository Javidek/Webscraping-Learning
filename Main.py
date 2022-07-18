from sklearn import tree
from CreateDB import Create_db
from Webscrap import webscarping

print('____Hi  you start practice in maktabkhune Python Advance(finall project)_____')
print('________Predictions made based on the site https://www.truecar.com/__________')

input_car=input('please enter name car and Model (ex:BMW X3) for predict price:').split(' ')
input_miles=input('please enter miles this car:')
input_Product=input('please enter Product years:')
input_accident=input('please enter several times accident this car :')
mydb=Create_db()
webscarping(mydb)
print('It is based on price predict miles,Product year and accident also complete machine information stored in Info_car table into Car database')
x=[]
y=[]
query='select Model,Miles,Product_c,Accident,Price from Info_car where Name = "%s";'% input_car[0]
cursor=mydb.cursor()
cursor.execute(query)
count=0
for Model_db,Miles_db,Product_db,Accident_db,Price_db in cursor:
    if Model_db == input_car[1]:
            x.append([Miles_db,Product_db,Accident_db])
            y.append(Price_db)
            count+=1

new_data=[[input_miles,input_Product,input_accident]]
clf =tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
answer=clf.predict(new_data)

print(f'My Predict Price {input_car[0]} {input_car[1]} in {count} cars: {answer}')
mydb.close()
