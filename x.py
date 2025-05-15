
# @app.get('/')
# async def basic_get():
#     return {"msg":"hi"}

# path parameter
# @app.get('/greet/{name}') #/greet/jay
# async def greet_name(name:str)->dict:
#     return {"mesg":f"Hello {name}"}

# #  BELOW SAME AS ABOVE

# query parameter
# @app.get('/greet') # /greet?name=jay
# async def greet_name(name:str)->dict:
#     return {"mesg":f"Hello {name}"}

# both parameter
# @app.get('/greet/{name}') # /greet/jay?age=23
# async def query_path_paramters(name:str, age:int) -> dict:
#     return {"name":name, "age":age}

# optional
# @app.get('/greet') #/greet?name=jay&age=23
# async def greet_optional(name: Optional[str] = 'John', age: int = 0) -> dict:
#     return {
#         "name" : name,
#         "age" : age
#     }

# @app.post('/create_book')
# async def create_book_endpoint(book_data:CreateBookModel):
#     print(book_data)
#     return {
#         "title" : book_data.title,
#         "author" : book_data.author
#     }


