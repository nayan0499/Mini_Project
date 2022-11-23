# POP-UP CAFE


## Project Background: 

This application runs on the command line. The user is able to view and choose from multiple menu options, including creating, updating, reading, and deleting data from csv files. 

### Client requirements: 
* Create a product, courier, or order dictionary and add it to a list 
* View all products, couriers, or orders
* Update the status of an order
* Persist data
* Update or delete a product, order, or courier
* List orders by status or courier


### Project design 

```
.
├── README.md
├── app.py
├── requirements.txt
├── src
│   ├── courier
│   │   ├── courier.py
│   │   └── courier_repository.py
│   ├── csvhandler
│   │   └── csv.py
│   ├── data
│   │   ├── courier.csv
│   │   ├── order.csv
│   │   └── product.csv
│   ├── menu.py
│   ├── order
│   │   ├── order.py
│   │   └── order_repository.py
│   ├── product
│   │   ├── product.py
│   │   └── product_repository.py
│   ├── repository
│   │   └── repository.py
│   └── service.py
└── test
    ├── resource
    │   └── fake_product.csv
    ├── test_courier.py
    ├── test_order.py
    ├── test_product.py
    ├── test_product_repo.py
    └── test_service.py

```




* Repository Pattern
* Abstraction: The higher the level of a module, the less detail. The lower the level, the more detail. 

[![Untitled-Diagramss-Page-2-drawio.png](https://i.postimg.cc/tCVCwTdP/Untitled-Diagramss-Page-2-drawio.png)](https://postimg.cc/Vdm8bzVL)



[![Untitled-Diagram-drawiosss-Page-1-drawio-2.png](https://i.postimg.cc/LsjPpDzt/Untitled-Diagram-drawiosss-Page-1-drawio-2.png)](https://postimg.cc/PLrJbmVJ)
#### Project structure






### Meeting project requirement
* Unit testing using unittest and pytest 

### Demo - Get index function 

```Python 
  def get_index(self, len_of_items: int):
        max_index = len_of_items - 1
        print(f'Select from 0 to {max_index}')
        try:
            index = int(input('Index: '))
            if index > len_of_items:
                print('Invalid input')
                return self.get_index(len_of_items)
        except:
            print('Invalid input')
            return self.get_index(len_of_items)
        if index not in range(len_of_items) or index == '':
            return self.get_index(len_of_items)
        else:
            return int(index)
 ```


### Improvements
* Do more tests
* Persist data in a database 
