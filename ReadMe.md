
# GS Management System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A web-based management system built with PHP, JavaScript, and MySQL for managing game servers or similar services.

## Features

- User authentication system (login/logout)
- Dashboard interface
- Server management capabilities
- Responsive web design
- MySQL database integration
- Session management
- Multi-language support (English/Spanish)

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript, jQuery
- **Backend**: PHP
- **Database**: MySQL
- **Server**: Apache
- **Dependencies**: 
  - Bootstrap (v5.1.3)
  - jQuery (v3.6.0)
  - Font Awesome (v5.15.4)

## Installation

### Prerequisites

- Web server (Apache recommended)
- PHP 7.4 or higher
- MySQL 5.7 or higher
- Composer (for dependency management)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yvhiku/GS-Managment-System.git
   cd GS-Managment-System
   ```

2. Set up the database:
   - Create a MySQL database
   - Import the SQL file from `/database/gs_management.sql`

3. Configure the application:
   ```bash
   cp config.example.php config.php
   ```
   Edit `config.php` with your database credentials:
   ```php
   define('DB_HOST', 'localhost');
   define('DB_USER', 'your_username');
   define('DB_PASS', 'your_password');
   define('DB_NAME', 'your_database');
   ```

4. Set up the web server:
   - Point your web server to the `public` directory
   - Ensure `mod_rewrite` is enabled for clean URLs

5. Access the application:
   - Open your browser to `http://localhost` (or your configured domain)
   - Default admin credentials (change after first login):
     - Username: `admin`
     - Password: `admin123`

## Directory Structure

```
├── assets/              # Static assets (CSS, JS, images)
├── config/              # Configuration files
├── database/            # Database schema and migrations
├── includes/            # PHP includes and utilities
├── languages/           # Translation files
├── libs/                # External libraries
├── pages/               # Application pages
├── public/              # Web server root
├── templates/           # HTML templates
├── uploads/             # File upload directory
├── .htaccess            # Apache configuration
├── config.example.php   # Example configuration
├── LICENSE              # MIT License
└── README.md            # This file
```

## Usage

1. **Login**: Access the system using your credentials
2. **Dashboard**: View system overview after login
3. **Server Management**: Add, edit, or remove servers
4. **User Management**: Manage user accounts (admin only)
5. **Settings**: Configure system preferences

## Screenshots

(Add actual screenshots from the system here)
- Login page
- Dashboard view
- Server management interface

## API Endpoints

The system provides these API endpoints:

- `/api/login` - User authentication
- `/api/servers` - Server management
- `/api/users` - User management (admin only)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support or questions, please open an issue on GitHub.

