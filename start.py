from app import create_application
from app.config import init_db
from app.routes import init_routes

app = create_application()
init_routes(app)
init_db(app)

if __name__ == '__main__':
    app.run()
