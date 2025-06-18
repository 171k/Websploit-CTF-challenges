from flask import Flask, request, render_template, Response

app = Flask(__name__)
FLAG = "ACS{4l3rt_w1th_js}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    q = request.args.get('q', '')
    if not q:
        return render_template('search_empty.html')
    # Pass raw user input, no sanitization
    return render_template('search.html', user_input=q, flag=FLAG)

@app.route('/flag')
def flag():
    # Only return flag if request is AJAX (from JS fetch with header)
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return Response(FLAG, mimetype='text/plain')
    return "Nope", 403

if __name__ == "__main__":
    app.run(debug=True, port=5555, host="0.0.0.0")
