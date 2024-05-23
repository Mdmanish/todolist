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

**Authentication Endpoints (permitAll permission):**

* **Register User (POST):** `/signup/`
  * Takes username and password in the request body.
  * Returns a success message and user details on successful registration.
* **Login User (POST):** `/login/`
  * Takes username and password in the request body.
  * Returns a success message on successful login.

**TODO Endpoints (require IsAuthenticated permission):**

* **List Todos (GET):** `/`
  * Returns a list of all TODO items for the authenticated user with associated steps, categories, and files.
* **Create Todo (POST):** `/`
  * Takes title (required) and other fields in the request body.
  * Returns the newly created TODO item.
* **Get Todo Detail (GET):** `/todos/<int:todo_id>/`
  * Returns details of a specific TODO item, including its steps, categories, and files.
* **Update Todo (PUT):** `/todos/<int:todo_id>/`
  * Takes optional title and description updates in the request body.
  * Returns the updated TODO item.
* **Delete Todo (DELETE):** `/todos/<int:todo_id>/`
  * Returns a success message upon deletion.

**Steps Endpoints (require IsAuthenticated permission):**

* **Add Step to Todo (POST):** `/addstep/<int:todo_id>/`
  * Takes a title for the new step in the request body.
  * Returns the newly created step associated with the specified TODO.
* **Get Step Details (GET):** `/addstep-details/<int:step_id>/`
  * Returns details of a specific step within a TODO.
* **Update Step Details (PUT):** `/addstep-details/<int:step_id>/`
  * Update the title or other details of a specific step.
* **Delete Step (DELETE):** `/addstep-details/<int:step_id>/`
  * Delete a specific step associated with a TODO.

**Categories Endpoints (require IsAuthenticated permission):**

* **Categorize Todo (POST):** `/category/<int:todo_id>/`
  * Adds new category to the selected todo.
* **Get Category Details (GET):** `/category-details/<int:category_id>/`
  * Returns details of a specific category associated with TODOs.
* **Delete Category (DELETE):** `/category-details/<int:category_id>/`
  * Delete a specific category associated with TODOs.

**Files Endpoints (require IsAuthenticated permission):**

* **Upload File to Todo (POST):** `/file/<int:todo_id>/`
  * Include the file data in the request body
  * Returns details of the uploaded file associated with the TODO.
* **Get File Details (GET):** `/file-details/<int:file_id>/`
  * Returns details of a specific file uploaded to a TODO.
* **Delete File (DELETE):** `/file-details/<int:file_id>/`
  * Delete a specific file associated with TODOs.

### Authentication

This API uses session-based authentication by default.

### Usage Example

1. Register a new user with a POST request to `/signup/`.
2. Login the user with a POST request to `/login/`.
3. Create a new TODO item with a POST request to `/`, including a title and description in the request body.
4. List all TODO items for the authenticated user with a GET request to `/`.
