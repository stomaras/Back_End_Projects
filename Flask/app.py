from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id":0,
        "author":"China",
        "language":"English",
        "title":"Things Fall Apart",
    },
    {
        "id":1,
        "author":"Greece",
        "language":"English",
        "title":"Things Fall Apart again",
    }
]

@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        if(len(books_list) > 0):
            return jsonify(books_list)
        else:
            'Nothing found', 404
    elif request.method == "POST":
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        id = books_list[-1]['id']+1
        
        new_obj = {
            "id":id,
            "author":new_author,
            "language":new_lang,
            "title":new_title,
        }
        books_list.append(new_obj)
        return jsonify(new_obj), 201

@app.route("/book/<int:id>", methods=["GET", "PUT","DELETE"])
def book(id):
    if request.method == "GET":
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
        return 'Book not found', 404
    elif request.method == "PUT":
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                update_book = {
                    "id":id,
                    "author":book['author'],
                    "language":book['language'],
                    "title":book['title'],
                }
                return jsonify(update_book)
        return 'Book not found', 404
    elif request.method == "DELETE":
        for book in books_list:
            if book['id'] == id:
                books_list.remove(book)
                return jsonify(books_list)
        return 'Book not found', 404
    
if __name__ == "__main__":
    app.run(debug=True)
# Re-loader in flask 
# watches all file changes
# Useful during development

# Debugger

# client ---> request ---> flask server --- request object ---> view function 

# Context in flask achieve this by making several objects global within a thread without interfering each other.

# There are two contexts in flask the 1) application context and 2) request context 

# application context 
# 1) - current_app instance of the current application
# 2) - g object that the application can use for temporary storage during the handling of the request and this variable is reset
# with each request.

# request context
# 1) -request which is the actual request contact and it encapsulate the contents of an HTTP request send by the client 
# 2) -session which is a dictionary that the application can use to store values that are remembered between requests
# flask activate application and request before dispatching the request to the application and removes them off to the request 
# is handled when the application context is pushed the current_app and g becomes availableto the thread etc.

# when a request dispatching form the client we need to find out what View function to invoke the service this request
# look on the applications urls map which contains a mapping to the urls with the view functions than handle them 


# Request Object 
# Methods: -get_data
# Methods: -get_json
# Methods: -is_secure

# Variables 
# -endpoint
# -method
# -host
# -url-base_url
# environ

# Request hooks
# - before_request
# - before_first_request
# - after_request
# - teardown_request 
# g context global as storage 

# Response 
# status code
# headers
# 
# Response Object 
# Methods 
# - set_cookie === it adds the cookie to the response
# - delete_cookie === it removes the cookie from the response
# - set_data === set to string or byte data
# - get_data