from flask import Flask, request, render_template, redirect, url_for, abort, make_response
import re

app = Flask(__name__)

FLAG = "ACS{b4d_r3v13w_g1v3s_fl4g!}"

# Products with simple info
products = {
    1: {"name": "Dalgona Candy", "desc": "Isnt that the candy from Squid Game?!!", "price": 5.99, "image": "/static/images/dalgonacandy.jpg"},
    2: {"name": "Bungeoppang", "desc": "Filled with sweet red bean paste!", "price": 14.99, "image": "/static/images/Bungeoppang.jpg"},
    3: {"name": "Cookies", "desc": "Delicious but dangerous for website if not secured", "price": 3.99, "image": "/static/images/cookies.jpg"},
    4: {"name": "Bingsu", "desc": "made with frozen milk or water-based ice, topped with various sweet ingredients", "price": 7.99, "image": "/static/images/bingsu.jpg"},
    5: {"name": "Bibimbap", "desc": "warm rice topped with various seasoned vegetables, meat, a fried egg, and gochujang", "price": 19.99, "image": "/static/images/bibimbap.jpg"},
    6: {"name": "Kimchi", "desc": "made from salted and fermented vegetables with a variety of seasonings", "price": 9.99, "image": "/static/images/kimchi.jpg"},
    7: {"name": "Bulgogi", "desc": "made with thinly sliced marinated beef. Known for its sweet and savory flavor profile.", "price": 19.99, "image": "/static/images/bulgogi.jpg"},
    8: {"name": "Tteokbokki", "desc": "rice cakes simmered in a garlicky, sweet, and spicy gochujang sauce until velvety and tender.", "price": 19.99, "image": "/static/images/tteokbokki.jpg"},
    9: {"name": "Spicy Chicken", "desc": "chicken fried in a crunchy coating, then smothered in a sticky, sweet and spicy sauce", "price": 9.99, "image": "/static/images/chicken.jpg"},
}

# Reviews stored per product id
reviews = {
    1: [{"username": "admin", "comment": "ahhh i love this candy!!"}],
    2: [{"username": "admin", "comment": "red bean paste ftw"}],
    3: [{"username": "admin", "comment": "mmm cookies, where did i stored mine again..?"},{"username": "171k", "comment": "this admin comments too much grr"}],
    4: [{"username": "admin", "comment": "This..made..my..mouth..drooling.."}],
    5: [{"username": "admin", "comment": "hungry"}],
    6: [{"username": "admin", "comment": "Very...healthy!"}],
    7: [{"username": "admin", "comment": "@171k please treat me some bulgogi"},{"username": "171k", "comment": "@admin lol, no way"}],
    8: [{"username": "admin", "comment": "tteokbokki is the besttt!!!"}],
    9: [{"username": "admin", "comment": "2spicy4me"}],
}

@app.route('/')
def index():
    resp = make_response(render_template('index.html', products=products))
    resp.set_cookie("hint", "secret key is ilovecookies")
    return resp

@app.route('/product/<int:pid>', methods=['GET', 'POST'])
def product(pid):
    if pid not in products:
        abort(404)

    if request.method == 'POST':
        username = request.form.get('username', 'Anonymous')
        comment = request.form.get('comment', '')
        reviews.setdefault(pid, []).append({
            "username": username,
            "comment": comment,
        })
        return redirect(url_for('product', pid=pid))

    return render_template('product.html', product=products[pid], reviews=reviews.get(pid, []))

# Admin page only accessible with a secret key (simulate admin login)
@app.route('/admin/<secret_key>')
def admin(secret_key):
    if secret_key != "ilovecookies":
        abort(403)

    # Clean up XSS payloads to prevent reuse
    xss_pattern = re.compile(r"<\s*script", re.IGNORECASE)
    for pid in reviews:
        reviews[pid] = [
            r for r in reviews[pid]
            if not xss_pattern.search(r["comment"])
        ]

    return f"<h1>Wow a bad review!</h1><p>FLAG: {FLAG}</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5050, host="0.0.0.0")
