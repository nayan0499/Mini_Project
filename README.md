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


### How I met the requirements 

* Model 
* Repository Pattern
* Abstraction: The higher the level of a module, the less detail. The lower the level, the more detail. 

[![Untitled-Diagramss-Page-2-drawio.png](https://i.postimg.cc/tCVCwTdP/Untitled-Diagramss-Page-2-drawio.png)](https://postimg.cc/Vdm8bzVL)



[![Untitled-Diagram-drawiosss-Page-1-drawio-2.png](https://i.postimg.cc/LsjPpDzt/Untitled-Diagram-drawiosss-Page-1-drawio-2.png)](https://postimg.cc/PLrJbmVJ)
#### Project structure





### Demo - Update function 

```Python 

   def update(self, *args):
        list_of_items = self.repo.get()
        print(self.tabulate_list(list_of_items, True))
        index = self.get_index(len(list_of_items))
        updated_details = self.item_type.get_update(*args)
        self.repo.update(index, updated_details)
        return updated_details

 ```


### Improvements
* Do more tests
* Persist data in a database 
