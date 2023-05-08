# password_hashing

## What's the point of this project?
The idea of this project is to implement a secure user registration model in the system.  
The password is not stored in the database, instead a hashed password is stored. 
The password hash includes a salt and a random number of re-hashing (from 10,000 to 15,000 iterations).

In the ```main``` we have a simple script to add a new user and check to log in.
## What does it look like? 
To simplify the demonstration, I used the standard Python dictionary.
```
database = {username: [salt, hashed_password, number_of_iteration]}
```
Example:
```
username = "miraslauli"
unhashed_password = "helloworld123"
```
Result:
```
{'miraslauli': ['113a94fb81e4e09164a7f05fd47018fc', 
                'eafaf3733349c76bc358497bd38b0904bb1f010985896efe32d5e1016cf19262f362b796a4431622eee1df40227fbc73f93eaf2a87fb0a122c11cd11c5ddc98f', 
                14552]}
```
