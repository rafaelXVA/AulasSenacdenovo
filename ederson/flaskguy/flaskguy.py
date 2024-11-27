from main import app

@app.route('/')
def homepage():
    return "não vou quarta feira"
@app.route('/blog')
def blog():
    return "cachorro"