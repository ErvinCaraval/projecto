# README

**Art Auction System Backend - Software Development 2, Universidad del Valle**

This repository contains the backend of an art auction application, developed as a project for the Software Development 2 course at the Universidad del Valle. The project focuses on integrating DevOps practices throughout the software development lifecycle, using Django as the primary framework.
TESTEANDO
## Description

The art auction system allows users to create, list, and bid on art piece auctions. This backend manages all the business logic, database interactions, and user authentication and authorization, providing a RESTful API to be consumed by the frontend.

## Features

- **Auction Management:** Creation and listing of auctions, with details such as title, description, image, starting price, and closing time.
- **Bid Management:** Users can place bids on active auctions, with validations to ensure bids exceed the current highest offer.
- **Authentication and Authorization:** User management, registration, login, and permissions for different roles within the application.
- **RESTful API:** A clear and well-structured interface for interaction with the frontend and possibly third parties.

## Technologies Used

- Django: The main framework for backend development.
- Django REST Framework: Facilitates the creation of a RESTful API.
- PostgreSQL: Database used for development and local testing.
- Docker: For containerizing the application and its environment.
- GitHub Actions: For continuous integration and deployment (CI/CD).
- Other DevOps Tools: Heroku, Prometheus, Selenium, Google Forms.

## Configuration and Deployment

**Local Setup:**

1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Perform migrations with `python manage.py migrate`.
4. Start the development server with `python manage.py runserver`.

**Containerization with Docker:**

- Build the image with `docker build -t image_name ..`.
- Launch the services with `docker-compose up`.

**CI/CD with GitHub Actions:**

- CI/CD configurations are defined in `.github/workflows`.
- Each push or pull request to the repository will trigger the continuous integration and deployment pipeline.

## Contributing

To contribute to the project, please follow the "fork-and-pull" workflow:

1. Fork the repository.
2. Create a branch for your feature or correction.
3. Make changes in your branch.
4. Submit a pull request for your changes to be integrated into the main repository.

## License

This project is under the MIT License. See the `LICENSE` file for more details.

---

**Universidad del Valle - Faculty of Engineering - Software Development 2**

