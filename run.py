from flaskblog import create_app
from flaskblog.config import Config, ConfigTest

app = create_app(Config)

if __name__ == '__main__':
    app.run(debug=True)

