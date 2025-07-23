pytest

markdown
Copy
Edit
*The included `pytest.ini` file configures the path correctly so tests can find the application modules.*

## API Usage

You can interact with the service using any HTTP client, such as `curl` or Postman.

### 1. Shorten a URL

-   **Endpoint**: `POST /api/shorten`
-   **Body**: A JSON object containing the URL.

**Example Request:**
curl -X POST http://localhost:5001/api/shorten
-H "Content-Type: application/json"
-d '{"url": "https://www.perplexity.ai/discover"}'

ruby
Copy
Edit

**Example Response (`201 Created`):**
{
"short_code": "aBcDeF",
"short_url": "http://localhost:5001/aBcDeF"
}

markdown
Copy
Edit

### 2. Redirect a Short URL

-   **Endpoint**: `GET /<short_code>`

**Example Usage:**
curl -L http://localhost:5001/aBcDeF

markdown
Copy
Edit
This will redirect to `https://www.perplexity.ai/discover`.

### 3. Get URL Analytics

-   **Endpoint**: `GET /api/stats/<short_code>`

**Example Request:**
curl http://localhost:5001/api/stats/aBcDeF

ruby
Copy
Edit

**Example Response (`200 OK`):**
{
"url": "https://www.perplexity.ai/discover",
"clicks": 1,
"created_at": "2025-07-23T11:30:00Z"
}

csharp
Copy
Edit

Or as a Markdown-formatted object:

{
"url": "https://www.perplexity.ai/discover",
"clicks": 1,
"created_at": "2025-07-23T11:30:00Z"
}

markdown
Copy
Edit


## Architecture & Design Decisions

-   **Separation of Concerns**: The application is structured into three main layers:
    -   `app/main.py`: The web layer (Flask routes and HTTP handling).
    -   `app/services.py`: The business logic layer.
    -   `app/models.py`: The data persistence layer.
-   **Concurrency**: A `threading.Lock` is used in the in-memory database to ensure atomic updates (like incrementing clicks), making the service safe for concurrent requests.
-   **Storage**: Uses a simple in-memory dictionary for persistence. This keeps the project self-contained but can be easily swapped with a more robust solution (like Redis or a SQL database) by modifying only `app/models.py`.
-   **Code Generation**: Uses Python's `secrets` module to generate cryptographically strong, random short codes, which minimizes the chance of collisions.
