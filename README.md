# Task: Build a Dynamic Profile Endpoint

Simple RESTful API endpoint that returns your profile information along with a dynamic cat fact fetched from an external API.

## Profile Endpoint (core requirements)

### Required endpoint

- Create a *GET* endpoint at: `/me`
- The endpoint must return JSON data with Content-Type: `application/json`
- Must integrate with the [Cat Facts API](https://catfact.ninja/) to fetch dynamic cat facts

### Response structure (required fields)

Your endpoint must return a JSON response in this exact format:

{
  "status": "success",
  "user": {
    "email": "<your email>",
    "name": "<your full name>",
    "stack": "<your backend stack>"
  },
  "timestamp": "<current UTC time in ISO 8601 format>",
  "fact": "<random cat fact from Cat Facts API>"
}

### Field specifications

- `status` — Must always be the string "success"
- `user.email` — Your personal email address
- `user.name` — Your full name
- `user.stack` — Your backend technology stack (e.g., "Node.js/Express", "Python/Django", "Go/Gin")
- `timestamp` — Current UTC time in ISO 8601 format (e.g., "2025-10-15T12:34:56.789Z")
- `fact` — A random cat fact fetched from the Cat Facts API

## Setup Instructions
