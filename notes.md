# Notes on Implementation

This document provides brief notes on the project's implementation and AI usage, as per the assignment guidelines.

## Development Approach

1.  **Core Logic First**: I started by designing the data structure (`UrlRecord`) and the service functions (`shorten`, `resolve`, `stats`) to ensure the business logic was sound.
2.  **API Layer**: With the service layer in place, I built the Flask routes (`main.py`) to expose the functionality via HTTP endpoints.
3.  **Testing**: I wrote tests using `pytest` to cover the "happy path" (the full shorten-redirect-stats workflow) as well as critical error cases (invalid URLs, non-existent codes).
4.  **Refinement**: I ensured proper error handling was in place, returning appropriate HTTP status codes and clear JSON error messages. I also added a `threading.Lock` to handle concurrency correctly.

## Design Choices

-   **In-Memory Database**: Chosen for simplicity and to meet the requirement of not using an external database. The `InMemoryDB` class is designed as an abstraction, so it could be easily replaced with a persistent database connector (e.g., Redis, SQLAlchemy) without changing the service logic.
-   **URL Validation**: A simple but effective validator was implemented using Python's `urllib.parse` to ensure that only `http` and `https` URLs are processed.
-   **Thread Safety**: A single lock was used for all write operations. Given the low-contention nature of this application, this is a simple and effective strategy. For a higher-traffic system, more granular locking or a database that handles transactions would be a better choice.

## AI Usage

-   **Tool Used**: Perplexity.
-   **Purpose**:
    -   Generating boilerplate code for the Flask application structure and `pytest` setup.
    -   Providing initial implementations for core logic components, which were then reviewed, tested, and refined.
    -   Debugging assistance, particularly in identifying the `ModuleNotFoundError` with `pytest` and the port conflict on macOS.
    -   Drafting documentation and clarifying requirements.
