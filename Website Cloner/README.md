# Python Script

## Script - Website Cloner

### Run server
python sever.py

### Open local site in browser
http://127.0.0.1:7000/

Enter a website link and click Clone Now
It downloads the website and loads the home page of the website in your local IP

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Explanation:

1. **Loading Environment Variables:** The `.env` file is used to load configurable values like `PORT` and `HOST`.

2. **Abstract Factory and Strategy Patterns:** The `WebpageDownloader` interface is created to follow the Strategy pattern, while `PyWebCopyDownloaderFactory` serves as an Abstract Factory to create instances of downloader strategies.

3. **Facade Pattern:** A `WebpageManager` class acts as a facade to simplify the interaction with the `WebpageDownloader`.

4. **Single Responsibility Principle (SRP):** The `RequestHandler` class now has a clear role as a controller, delegating the downloading logic to the `WebpageManager`.

5. **Dependency Injection:** The `WebpageManager` is injected with a `WebpageDownloaderFactory` to decouple the handler from the specific downloading strategy.

6. **Inversion of Control (IoC):** The application flow is controlled by the `main` function, launching the server and handling requests. 