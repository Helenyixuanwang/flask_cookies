# import the function that will return an instance of a connection
from flask_app.configs.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Cookie:
    DB = 'cookie_flask_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies;"
# make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
    # Create an empty list to append our instances of friends
        cookies = []
    # Iterate over the db results and create instances of friends with cls.
        for cookie in results:
            cookies.append( cls(cookie) )
        return cookies
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO cookies ( name,type, num_of_boxes  ) VALUES ( %(name)s , %(type)s , %(num_of_boxes)s );"
        # data is a dictionary that will be passed into the save method from server.py
        # return a id for the newly created record
        new_id= connectToMySQL(cls.DB).query_db( query, data )
        return new_id
    # the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls, cookie_id):
        query  = "SELECT * FROM cookies WHERE id = %(id)s;"
        data = {'id':cookie_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    

    @classmethod
    def update(cls,data):
        query = """UPDATE cookies 
                SET name=%(name)s,
                type=%(type)s,num_of_boxes=%(num_of_boxes)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
    
    # @classmethod
    # def delete(cls, cookie_id):
    #     query  = "DELETE FROM cookies WHERE id = %(id)s;"
    #     data = {"id": cookie_id}
    #     return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM cookies WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def is_valid_cookie(cookie):
        is_valid = True
        print(f'string length of the input cookies is {len(cookie["num_of_boxes"])}')

        if len(cookie["name"]) <= 0:
            is_valid = False
            flash("client name is required.")
        elif len(cookie["name"]) < 2: 
            flash("name must be at least 2 characters")
            is_valid = False
        if len(cookie["type"]) <= 0:
            is_valid = False
            flash("Type is required.")
        elif len(cookie["type"]) < 2: 
            flash("type must be at least 2 characters")
            is_valid = False
        if len(cookie["num_of_boxes"]) <= 0:
            is_valid = False
            flash("number of boxes is required.")
        elif int(cookie["num_of_boxes"]) <=0:
            is_valid = False
            flash("Quantity must be at least 1")
        

        #this way, it won't report the base 10 error when do not input anything in num_of_boxes
        # if cookie["num_of_boxes"]:#if there is some input
        #     if int(cookie["num_of_boxes"]) <=0:#then decide if it is less than zero or equals to zero
        #         is_valid = False
        #         flash("Please enter a valid number")
        # else:#do not input any string or number
        #     flash("Please do not leave num of boxes blank")
        #     is_valid = False

        print(type(cookie['num_of_boxes']))

        return is_valid
            
