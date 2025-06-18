from flask import Flask, Response, render_template
app = Flask(__name__)

@app.route('/')
def index():
    content = render_template('index.html')
    resp = Response(content)
    resp.headers['X-Secret-Flag'] = 'ACS{ch3ck_y0ur_h34d3r}'
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
