# Pacmann_Super_Cashier_Project

## Background
In order to easier shopping experience both for Customer Seller as a Merchant, sparked ideas to design and create the self cashier system that was built from Python Code to assist Customer to do some several task such as picking products to cart, listing down the product, validating the items that are listed, and calculating the price of items.

## Objective
The self-service cashier system project has the objective and functionality that elaborate into several parts, as below :
1. The system can handle the list task of 
      <br>a. add_item 		: Adding the item into cart
      <br>b. update_item_name : Updating the name of item in cart
      <br>c. update_item_qty 	: Updating the quantity of item in cart
      <br>d. update_item_price 	: Updating the price of item in cart
      <br>e. delete_item 		: Deleting the certain item in cart
      <br>f. reset_transactions	: Making empty the list items in cart
      <br>g. check_order		: Checking the items to validate the format data
      <br>h. total_price		: Calculating total price of all items
      <br>i. display		: Displaying the list items in cart
2. 	Applying the python code functionality based in Object Oriented Programming.
3.	Applying the python code in modular form/script.
4.	Applying the python code in structured documented (Docstring) and clean code (referred on PEP8 rules).


## Detail of Code File
The documents code on this project containing two files, the first one is cashier.py, the main code in scripted form and become module on the file test, and the second one is file main.ipynb that become test code on Notebook file.

 
 ## Flowcharts
![Blank board - Page 1](https://user-images.githubusercontent.com/46970478/216847667-3b07e411-ac62-4333-8c2e-601f732dd8e7.png)

## Description Flowchart of Program
<br>1. Creating new instance of class Transaction as a Customer's cart item. This class containing functions that run the tasks of Cashier system (add item, calculate the total price, etc). After creating the instance, Customer can choose the task(function) to process the transaction.

<br>2. add_item()
       <br>Customer can add the new item with calling function add_item() containing 3 parameters [nama_item(str), jumlah_item(int), harga_item(int)] that represent the        shopping cart in dictionary form. This function will validate the data type input, whether already matched with data type standarized on system, if yes              continue the process in function, if not tell the customer to input correct data format. 

<br>3. update_item_name()
       <br>Customer can update the item name with calling function update_item_name() containing 2 parameters [nama_item(str), nama_baru(str)]. This function replaces          the old item name with the new one of item that picked and uses the validation process as well for data that inputted.

<br>4. update_item_qty()
       <br>Customer can update the item quantity with calling function update_item_qty() containing 2 parameters [nama_item(str), jumlah_baru(int)]. This function              replaces the old quantity of nama_item(str) with jumlah_baru(int) and uses the validation process as well for data that inputted.

<br>5. update_item_price()
<br>Customer can update the item name with calling function update_item_price() containing 2 parameters [nama_item(str), harga_baru(int)]. This function replace          the old price name of nama_item(str) with harga_baru(int) and uses the validation process as well for data that inputted.

<br>6. display()
       <br>Customer can display all transactions that have picked with function display().

<br>7. delete_item()
<br>Customer can delete the certain item name with calling function delete_item() containing 1 parameter [nama_item(str)]. This function delete the nama_item(str)        (key-value) and uses the validation process as well for data that inputted.

<br>8. check_order()
<br>Customer can check the order using check_order() function without argument inputted. This function check all the format data have inputted whether already            matched or not with format standarized, and validates if items have existed in the cart or not.

<br>9. total_price()
<br>Customer can total price of the whole of Transactions using function total_price().

<br>10. reset_transaction()
<br>Customer can make cart empy with using function reset_transaction(). This function delete the nama_item(str) (key-value) and validates if items have existed          in the cart or not before making empty the cart.


## Functions/Attributes

![image](https://user-images.githubusercontent.com/46970478/216855663-2b33ad61-d3e1-45b9-9c5f-3dd99d62f280.png)

## Result of Test
The detail result of test can be checked on this [notebook document](https://github.com/vanny29bowo/pacmann_super_cashier_project/blob/master/main.ipynb).

## Conclusion
This project contained a self-service cashier system that was built from Python Code to assist Users' experience in buying products from the store, such as listing down the product that was picked, validating the items that are listed, and calculating the price.

## Future Work
To further development on this system, maybe the system can be added features to detect the product already expired or not, or advance validating the product original or imitation. 
