# Tracking Meat Web
This project is built with the Django framework and python 3.7.8, the libraries to be installed are:
+ Django 3.2.10
+ Redis
+ Web3

You must have redis-server installed on your machine or it will not work.
After installing it, you have to set the password 'secret' with the command with redis-cli:
```
config set requirepass 'secret'
```

You can also set a different password, but in this case you have to modify the source code
in the **view.py** where the connection with Redis is created.

### Login
It is possible to log in as a basic user or as an administrator:
+ basic user: it is created via the special registration link.
+ admin: it can only be created via the root directory of the project with the command:

```
python manage.py createsuperuser
```

***Attention, in this project redis is used to store the IP of the administrator user named 'admin',
so it will only work when logged in with an administrator with this name.
If you want to change this, you need edit the source code in views.py.***

### Home
This is the homepage where you can view or search for interested lots, you can also see the details
where you can see the transaction made on Ethereum's Ropsten testnet.
If you are an administrator you can also add a new lot by entering the tracking code.
Once the lot is entered the transaction will be saved on Ropsten sending the lot code and description in sha256 as a message.

### Links
This project is deployed on Amazon Web Service at this [URL](http://54.221.91.208/).



