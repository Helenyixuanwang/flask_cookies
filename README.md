# Cookie Orders Management System

A Flask web application for managing cookie orders, featuring a responsive interface for creating, viewing, editing, and deleting orders.

## Features

- Create new cookie orders with customer name, cookie type and quantity
- View all existing cookie orders in a well-organized table
- Edit cookie order details
- Delete cookie orders with confirmation
- Responsive Bootstrap interface
- MySQL database backend

## Live Demo

The application is deployed and accessible at: http://3.22.217.192

## Technologies Used

### Backend
- Python 3.12
- Flask web framework
- PyMySQL for database connectivity
- Gunicorn WSGI server

### Frontend
- HTML5 / CSS3
- Bootstrap 5 for responsive design
- Jinja2 templating engine

### Infrastructure
- AWS EC2 for hosting
- Ubuntu Server
- Nginx as reverse proxy
- MySQL database

## Project Structure

```
cookie_app/
├── flask_app/              # Main application package
│   ├── __init__.py         # Package initializer
│   ├── configs/            # Configuration files
│   │   ├── __init__.py
│   │   └── mysqlconnection.py  # Database connection setup
│   ├── controllers/        # Route handlers
│   │   └── cookies_controller.py  # Cookie order controllers
│   ├── models/             # Data models
│   │   └── cookie.py       # Cookie model with database operations
│   └── templates/          # Jinja2 HTML templates
│       ├── index.html      # Order listing page
│       ├── edit_cookie.html # Order editing page
│       └── new_order.html  # Order creation page
├── server.py               # Application entry point
└── wsgi.py                 # WSGI entry point for Gunicorn
```

## Installation and Setup

### Prerequisites
- Python 3.6 or higher
- MySQL Server
- Git

### Local Development Setup

1. Clone the repository
```bash
git clone https://github.com/Helenyixuanwang/flask_cookies.git
cd flask_cookies
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up MySQL database
```sql
CREATE DATABASE cookie_flask_schema;
CREATE TABLE cookies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    num_of_boxes INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

5. Configure database connection
Update the database credentials in `flask_app/configs/mysqlconnection.py` if needed.

6. Run the application
```bash
python server.py
```

The application should be available at http://localhost:5000

### Production Deployment

For production deployment to AWS EC2, refer to the detailed [Deployment Guide](https://github.com/Helenyixuanwang/flask_cookies/blob/main/deployment_guide.md).

## Database Schema

The application uses a simple data model with a single table:

**cookies**
- `id`: INT (Primary Key, Auto Increment)
- `name`: VARCHAR(255) (Customer name)
- `type`: VARCHAR(255) (Cookie type)
- `num_of_boxes`: INT (Number of boxes ordered)
- `created_at`: DATETIME (Timestamp of creation)
- `updated_at`: DATETIME (Timestamp of last update)

## Usage

1. **View Orders**: The home page displays all cookie orders in a table
2. **Create Order**: Fill out the form on the home page to create a new cookie order
3. **Edit Order**: Click the "Edit" button next to an order to modify its details
4. **Delete Order**: Click the "Delete" button to remove an order (with confirmation)

## Development

### Adding Features

To extend the application:

1. Add new routes in `flask_app/controllers/cookies_controller.py`
2. Add corresponding methods in `flask_app/models/cookie.py` for database operations
3. Create or update templates in `flask_app/templates/` for the UI

### Styling

The application uses Bootstrap 5 for styling. Modify the templates to customize the appearance.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Coding Dojo for the Flask curriculum
- Bootstrap team for the responsive UI framework
