# URL Shortener Service

This is a simple, lightweight URL shortening service built with Python and Flask. It provides a minimal REST API to create short URLs, handle redirects, and view basic analytics for each link. The project is designed to be simple, robust, and easy to run.

## Features

-   **Shorten URL**: Create a unique 6-character code for any valid long URL.
-   **Redirect**: Automatically redirect users from a short URL to the original destination.
-   **Analytics**: Track the number of clicks for each short URL.
-   **Thread-Safe**: Designed to handle concurrent requests without data corruption.

## Tech Stack

-   **Backend**: Python 3.8+
-   **Framework**: Flask
-   **Testing**: Pytest

## Getting Started

Follow these instructions to get the application running on your local machine.

### Prerequisites

-   Python 3.8 or newer.

### Setup & Installation

1.  **Clone the repository or unzip the archive:**
    ```
    # If it's a git repo
    # git clone <repository_url>

    # Navigate into the project directory
    cd url-shortener
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```
    # Create the environment
    python3 -m venv venv

    # Activate it (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the Flask server:**
    ```
    python -m flask --app app.main run --port 5001
    ```
    *Note: We use port `5001` to avoid potential conflicts with services like macOS AirPlay that often occupy port `5000`.*

2.  The API will now be available at `http://localhost:5001`.

### Running Tests

To verify that all functionality works as expected, run the test suite:
