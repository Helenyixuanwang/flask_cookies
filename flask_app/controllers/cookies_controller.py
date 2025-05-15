from flask import render_template,request,redirect
from flask_app import app

from flask_app.models.cookie import Cookie


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    cookies = Cookie.get_all()
    print(cookies)
    return render_template("index.html", all_cookies = cookies)

@app.route('/cookie/new')
def display_new():
    return render_template("new_order.html")

@app.route('/create_cookie', methods=["POST"])
def create_cookie():
    #add validation after reading validation part
    if not Cookie.is_valid_cookie(request.form):
        print("Validation Fail")
        return redirect('/cookie/new')
    print(request.form)
    id = Cookie.save(request.form)
    return redirect("/")

@app.route('/show_edit/<int:cookie_id>')
def show_edit(cookie_id):
    one_cookie = Cookie.get_one(cookie_id)
    print(one_cookie)
    return render_template("edit_cookie.html", one_cookie=one_cookie)

@app.route('/update_cookie', methods=["POST"])
def edit_cookie():
    cookie_id = request.form['id']
    if not Cookie.is_valid_cookie(request.form):
        print("Validation Fail")
        return redirect(f'show_edit/{cookie_id}')
    print(request.form)
    # there is a hidden attribute being transferred through the html form
    Cookie.update(request.form)
    return redirect("/")

@app.route('/delete/<int:id>', methods=['POST'])
def delete_cookie(id):
    data = {
        "id": id
    }
    Cookie.delete(data)
    return redirect('/')


# @app.route('/user/<int:user_id>')
# def get_oneUser(user_id):
    
#     one_user = User.get_one(user_id)
#     print(one_user)
#     return render_template("showOne.html", one_user=one_user)

# @app.route('/user/delete/<int:user_id>')
# def destroy(user_id):
#     User.delete(user_id)
#     return redirect('/')
