from app import app

@app.route('/')
def index():
    return 'Avalon bot v1'
