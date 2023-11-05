# User Management System

## Introduction

This project is a simple user management system backend built using FastAPI and Firebase. The system provides APIs for user registration, login, profile management, and user deletion. Firebase is used for user authentication and Firestore for data storage.

## Table of Contents

- [Getting Started](#getting-started)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
- [User Registration](#user-registration)
- [User Login](#user-login)
- [User Profile](#user-profile)
- [User Deletion](#user-deletion)
- [Validation and Security](#validation-and-security)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Deployment](#deployment)
- [Conclusion](#conclusion)
- [Appendix](#appendix)

## Getting Started

- Clone this repository.
- Create and activate a virtual environment (recommended).
- Install project dependencies using `pip install -r requirements.txt`.
- Set up your Firebase project and obtain the necessary credentials.
- Configure your environment variables for Firebase.

## Authentication

User authentication is handled through Firebase. Firebase Authentication provides secure user registration and login. Refer to [Firebase Authentication](https://firebase.google.com/docs/auth) for more information.

## API Endpoints

The following API endpoints are available:

- `/register`: Register a new user.
- `/login`: Log in an existing user.
- `/profile`: Retrieve and update user profiles.
- `/delete`: Delete a user account.

## User Registration

- Send a POST request to `/register` with user information.
- The user will be created in Firebase and their data stored in Firestore.
- Passwords are securely stored in Firebase and not in Firestore.

## User Login

- Send a POST request to `/login` with user credentials.
- On successful login, a Firebase Auth token is returned.

## User Profile

- Send a GET request to `/profile` to retrieve user profile information.
- Send a PUT request to `/profile` to update user profile information.

## User Deletion

- Send a DELETE request to `/delete` to request the deletion of your account.

## Validation and Security

- Input validation is implemented for all user inputs.
- API endpoints are secured to ensure only authenticated users can access their profiles.

## Error Handling

Common error responses are defined for different scenarios to help you diagnose issues.

## Testing

- Use tools like Postman to test the API endpoints.
- Sample test cases and expected results are provided in the code documentation.

## Deployment

- Deploy the application to a production environment of your choice.
- Make sure to set the appropriate environment variables.

## Conclusion

This user management system provides essential features for user registration, login, profile management, and account deletion. It ensures the security and privacy of user data by using Firebase for authentication and Firestore for storage.
