## Django TODO API

This is a Django REST API for managing TODOs. Users can register, login, create, retrieve, update, and delete TODO items.

### Features

* User registration and login
* Create, list, update, and delete TODO items
* User authentication for accessing TODO resources

### Technologies Used

* Django
* Django REST Framework

### Getting Started

1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies: `pip install requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

### API Endpoints

* **Register User (POST):** `/signup/`
  * Takes username, email, password and confirm password in the request body.
  * Returns a success message and user details on successful registration.
* **Login User (POST):** `/login/`
  * Takes username and password in the request body.
  * Returns a success message on successful login.
* **List Todos (GET):** `/` (requires authentication)
  * Returns a list of all TODO items for the authenticated user.
* **Create Todo (POST):** `/` (requires authentication)
  * Takes title and description in the request body.
  * Returns the newly created TODO item.
* **Get Todo Detail (GET):** `/<int:todo_id>/` (requires authentication)
  * Returns details of a specific TODO item.
* **Update Todo (PUT):** `/<int:todo_id>/` (requires authentication)
  * Takes optional title and description updates in the request body.
  * Returns the updated TODO item.
* **Delete Todo (DELETE):** `/<int:todo_id>/` (requires authentication)
  * Returns a success message upon deletion.

### Authentication

This API uses session-based authentication by default.

### Usage Example

1. Register a new user with a POST request to `/signup/`.
2. Login the user with a POST request to `/login/`.
3. Create a new TODO item with a POST request to `/`, including a title and description in the request body.
4. List all TODO items for the authenticated user with a GET request to `/`.
