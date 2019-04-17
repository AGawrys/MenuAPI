# MenuAPI
## A simple server in Flask
## How to Run
1. Install python
2. Check to see if you have pip installed 
by entering "pip" into the command prompt. 
If it is not installed some message will indicate 
that the command is unrecognized.  

On windows : "python -m pip install -U pip". 

On linux or MacOS : "pip install -U pip"

3. Install SQLite by navigating to their page and choosing the correct
option for your machine.

4. Make sure to have the following also installed:

pip install flask_sqlalchemy

pip install flask_marshmallow

pip install marshmallow-sqlalchemy


5. Now, get the code from this repository by cloning it into
a desired location. Type "git clone this_git_url".

6. Once you have the code opened up. Go into the python interactive
shell and type 

"from MenuServer import db"

"db.create_all()"

7. I used postman (https://www.getpostman.com/postman) to simulate. 
Simply open up postman, make sure the param is your
localhost (ex. localhost:5000/menu), you are on the "body" tab, with the raw button toggled, and
have JSON/Application selected in the drop down menu below params.

8. Choose the option on the side of the params (GET, POST, PUT, DELETE) and 
enter the corresponding link. 

-To create menu write a desired menu name in the textbox

{

    "name" : "Lunch Special"

}

And press Send on the POST option. 

-To see all menus: localhost:5000/menu Option GET

-To get menu by id: localhost:5000/menu/1 (1 is the id here)

-To delete a menu: localhost:5000/menu Option DELETE

-To update a menu: localhost:5000/menu Option PUT with the following in the textbox

{

    "name" : "Your updated name"

}


Done!
