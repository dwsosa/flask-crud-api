## Installation

### Using Docker Compose
1. Clone this repository:
    ```bash
    git clone https://github.com/dwsosa/flask-crud-api.git
    cd flask-crud-api
    ```

2. Ensure you have Docker and Docker Compose installed on your machine.

3. Build and start the application with Docker Compose:
    ```bash
    docker-compose up --build
    ```

   This will build the Docker images, create containers for both the Flask app and PostgreSQL database, and start the application.

   - The Flask app will be accessible at `http://127.0.0.1:718` (the port specified in your Docker setup).
   - The PostgreSQL database will be running inside a Docker container.

### Using a Local Environment (Not Recommended)
1. Clone this repository:
    ```bash
    git clone https://github.com/dwsosa/flask-crud-api.git
    cd flask-crud-api
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database and configure the connection settings in the application.

5. Start the Flask app:
    ```bash
    flask run
    ```

   The app will be available at `http://127.0.0.1:5000` by default (or you can specify the port with the `FLASK_RUN_PORT` environment variable).

## Database Setup
When running the app with Docker, the PostgreSQL database will be created automatically as part of the container setup. If running locally (without Docker), you will need to:

1. Install and set up PostgreSQL.
2. Create a database for the app using the DB files.
3. Update the database connection URI in the app’s configuration with your PostgreSQL credentials:

Example:
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database_name'
