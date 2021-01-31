from graphene import ObjectType, String, Schema
import graphene
import json
from flask import Flask, request
app = Flask(__name__)

class Query(ObjectType):
    #Schema is defined here
    comment = String(
        id=graphene.String(default_value = ""), 
        name=graphene.String(default_value = ""),
        email = graphene.String(default_value = ""),
        body=graphene.String(default_value = "")
        )

    #Function to resolve the comment and return every comment based on search term
    def resolve_comment(self, root, name, id, email, body):
        relaventComments = []
        searchKey = None
        searchVal = None
        searchableItems = {
            'id':id,
            'name':name,
            'email':email,
            'body':body
            }
        
        for k, v in searchableItems.items():
            if v != "":
                searchKey = k
                searchVal = v
        comments = {
            0:{
            "id":"1",
            "name": "id labore ex et quam laborum",
            "email": "Eliseo@gardner.biz",
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            },
            1:{
            "id":"2",
            "name": "id labore ex sdvdsvdsvdsvdsv quam laborum",
            "email": "Eliseo@gardner.biz",
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            },
            2:{
            "id":"3",
            "name": "id labore ex et quam svdssdvdsvdsv",
            "email": "Eliseo@gardner.biz",
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            },
             3:{
            "id":"4",
            "name": "id labore ex et quam laborum",
            "email": "Eliseo@gardner.biz",
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            },
             4:{
            "id":"5",
            "name": "id labore ex et quam laborum",
            "email": "Eliseo@gardner.biz",
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            },
            5:{
            "id":"6",
            "name": "id labore ex et quam laborum",
            "email": "Eliseo@gardner.biz",
            "body": "Test body"
            },
        }
        # loop through all comments depending on key and value provided then return new array
        for c in comments:
            if comments[c][searchKey] == searchVal:
                relaventComments.append(comments[c])
        return relaventComments
                



schema = Schema(query=Query)
query_string = 'query { comment(email:"Eliseo@gardner.biz") }'
result = schema.execute(query_string)

@app.route('/', methods=['POST'])
def hello_world():
    schema = Schema(query=Query)
    print(request.form['query'])
    query_string = request.form['query']
    result = schema.execute(query_string)
    return str(result)