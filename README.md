# Library Management System API

## How to Run the Project

To get the Library Management System API up and running, follow these steps:

1. **Clone the Repository**:

   - Open your terminal or command prompt.
   - Use the following command to clone the repository to your local machine:
     ```bash
     git clone <repository-url>
     ```
   - Replace `<repository-url>` with the actual URL of the GitHub repository.

2. **Navigate to the Project Directory**:

   - Change your current directory to the project folder:
     ```bash
     cd library_management_system
     ```

3. **Set Up the Environment**:

   - It is recommended to create a virtual environment to manage dependencies. You can do this using `venv`:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies**:

   - Since this project does not use any third-party libraries, there are no additional dependencies to install. However, ensure you have Flask installed. If not, you can install it using:
     ```bash
     pip install Flask
     ```

5. **Run the Application**:

   - Start the Flask server by running the following command:
     ```bash
     python app.py
     ```
   - The server will start, and you should see output indicating that it is running on `http://127.0.0.1:5000/`.

6. **Interact with the API**:
   - You can use tools like Postman or curl to interact with the API endpoints. Make sure to include the `Authorization` header with the token when making requests to protected endpoints.
   - Here’s an example of a curl command to add a book:
     ```bash
     curl -X POST http://127.0.0.1:5000/books \
     -H "Authorization: Bearer mysecrettoken" \
     -H "Content-Type: application/json" \
     -d '{"title": "1984", "author": "George Orwell"}'
     ```

## Running the Tests

To run the tests for the Library Management System API, follow these steps:

1. **Ensure the Environment is Set Up**:

   - Make sure you have followed the steps in the README to set up your environment and activate your virtual environment.

2. **Navigate to the Project Directory**:

   - Open your terminal or command prompt and navigate to the project directory:
     ```bash
     cd library_management_system
     ```

3. **Activate the Virtual Environment** (if not already activated):

   - If you created a virtual environment, activate it:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Run the Tests**:

   - You can run the tests using the `unittest` module:
     ```bash
     python -m unittest discover -s tests
     ```

5. **View the Test Results**:
   - After running the tests, you will see output in the terminal indicating which tests passed and which (if any) failed.

## Design Choices

The design of the Library Management System API was influenced by several key choices:

1. **Framework**:

   - Flask was chosen for its simplicity and flexibility. It allows for quick development and easy integration of features, making it ideal for a small-scale project like this.

2. **Data Storage**:

   - The API uses in-memory lists to store books and members. This choice simplifies the implementation and is suitable for demonstration purposes. However, for a production system, a database (e.g., SQLite, PostgreSQL) would be more appropriate for persistent storage.

3. **Authentication**:

   - Token-based authentication was implemented to secure access to the API. This method is straightforward and allows for easy validation of user access. A hardcoded token is used for simplicity, but in a real application, a more secure method for token generation and storage should be employed.

4. **Pagination**:
   - Pagination was implemented to efficiently handle large datasets. This design choice improves performance and user experience by allowing clients to request data in manageable chunks rather than loading everything at once.

## Assumptions and Limitations

1. **Assumptions**:

   - The system is designed for a small number of books and members, making in-memory storage feasible. It is assumed that the API will be used in a controlled environment where the number of records is limited.

2. **Limitations**:
   - **No Third-Party Libraries**: The project does not utilize any third-party libraries, which limits some functionalities (e.g., advanced data validation, ORM for database interactions).
   - **Hardcoded Token**: The use of a hardcoded token for authentication is a significant limitation. In a real-world application, a more secure and dynamic method for token management should be implemented.
   - **In-Memory Storage**: Since data is stored in memory, all records will be lost when the server is restarted. This approach is not suitable for production use, where persistent storage is required.
   - **Basic Error Handling**: The API includes basic error handling, but it could be improved to provide more informative responses and handle edge cases more gracefully.
