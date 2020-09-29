import os
from app import create_app

# Creating app instance
app = create_app(os.environ.get('FLASK_ENV'))

if __name__ == '__main__':
    app.run()
