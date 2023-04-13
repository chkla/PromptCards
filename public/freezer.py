from main import app
from flask_frozen import Freezer

app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

if __name__ == '__main__':
    # freezer.run(debug=True)
    freezer.freeze()