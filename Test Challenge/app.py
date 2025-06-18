from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow: /admin_secret_panel_171k/"

@app.route('/admin_secret_panel_171k/')
def admin_panel():
    return "Welcome hacker! You found my secret hideout so here's your reward! ACS{171k_1n_r0b0ts}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
