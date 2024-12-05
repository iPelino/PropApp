# Property Management API

This project is a Property Management API built using Django and Django REST Framework. It provides endpoints for managing products, owners, and properties.

## Features

- User authentication and authorization
- CRUD operations for products, owners, and properties
- API documentation with drf-spectacular
- Debugging with Django Debug Toolbar

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (default database)
- drf-spectacular
- Django Debug Toolbar

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Products

- List and create products: `GET /api/v1/products/` and `POST /api/v1/products/`

### Owners

- List owners: `GET /api/v1/owners/`
- Add new owner: `POST /api/v1/owners/`

### Properties

- List properties: `GET /api/v1/properties/`

## Authentication

This API uses token-based authentication. Ensure you include the token in the `Authorization` header for protected endpoints.

## API Documentation

API documentation is available at `/api/schema/swagger-ui/` when the server is running.

## Debugging

Debugging is enabled with Django Debug Toolbar. It is accessible only from internal IPs.

## License

This project is licensed under the MIT License.
