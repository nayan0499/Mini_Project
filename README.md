# POP-UP CAFE


## Project Background: 
This CLI project was developed to fulfil the clients' constantly changing requirements. Currently, this app allows users to view and choose from multiple menu options, including creating, updating, reading, and deleting data which persists in csv files.

### Client requirements: 
The following requirements have been implemented in my app. 

* Create a product, courier, or order dictionary and add it to a list 
* View all products, couriers, or orders
* Update the status of an order
* Persist data
* Update or delete a product, order, or courier
* List orders by status or courier


### Project design 
This tree represents the directories in this repository. 

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

* Model the business domain using classes 
* Use of the repository pattern
* Use of Abstraction


[![Untitled-Diagramss-Page-2-drawio.png](https://i.postimg.cc/tCVCwTdP/Untitled-Diagramss-Page-2-drawio.png)](https://postimg.cc/Vdm8bzVL)


[![Untitled-Diagram-drawiosss-Page-1.jpg](https://i.postimg.cc/T33CBrt0/Untitled-Diagram-drawiosss-Page-1.jpg)](https://postimg.cc/svbYhZdG)



### Demo - Update function 

```Python 
    
   # service.py
   product_service = Service(prod_repo, Product)
   
   # app.py
   ...elif sub_menu.selected == 3:
            service.update()
            
   # order.py        
   ... @classmethod
        def get_update(cls):

        product_details = {}
        for key in cls.keys:
            input_by_user = input(f'{key}: ')
            if input_by_user != '':
                product_details[key] = input_by_user
        try:
            product_details = cls.get_validated_update(product_details)
            return product_details
        except TypeError as e:
            print(e)  
            return cls.get_update_details()
            
   # service.py
   def update(self, *args):
        list_of_items = self.repo.get()
        print(self.tabulate_list(list_of_items, True))
        index = self.get_index(len(list_of_items))
        updated_details = self.item_type.get_update(*args)
        self.repo.update(index, updated_details)
        return updated_details

 ```
### What I enjoyed working on 
* Unit testing 

### Improvements
* Do more tests
* Persist data in a database 
