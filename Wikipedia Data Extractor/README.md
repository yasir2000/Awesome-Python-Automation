# To Run This Wikipedia Extractor Code Using Python

### **You need to install 'wikipedia' library using pip**

#### Steps to Install 'wikipedia'



**First create virtual env in your IDE and set it by using given commands**

##### macOS 
```
python3 -m venv .venv
source .venv/bin/activate
```


##### Linux

```
sudo apt-get install python3-venv    #If needed
python3 -m venv .venv
source .venv/bin/activate
```

##### Windows
```
py -3 -m venv .venv
.venv\scripts\activate
```

use this command in your virtual env to install wikipedia

```
pip install wikipedia
```


-------
**Now you can run this in your IDE**

###### **You can change "language = jp" to another language you wish to translate to as well.**








<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->


Assuming you have the following directory structure:

```
your_project/
│
├── main.py
├── search_handler.py
├── wikipedia_client.py
├── .env
└── requirements.txt  # Include 'wikipedia-api' and 'python-dotenv'
```

### Step 6: Features and Patterns

- **Single Responsibility Principle**: Each class has one responsibility (Wikipedia interaction, handling user searches).
- **Open/Closed Principle**: We can extend the system (e.g., adding more features or changing language support) without modifying existing code significantly.
- **Liskov Substitution Principle**: If we derived more classes from `WikipediaClient` (e.g., different Wikipedia API clients), they could substitute `WikipediaClient` without issues.
- **Inversion of Control**: The `SearchHandler` depends on the abstraction `WikipediaClient` rather than a concrete implementation.
- **Dependency Injection**: We pass `WikipediaClient` to `SearchHandler` instead of having it create an instance internally.


To use this code, ensure you have the necessary packages installed, typically via a `requirements.txt` file:
```plaintext
wikipedia-api
python-dotenv
``` 

You can install these using pip:
```bash
pip install -r requirements.txt
``` 

This design forms a solid foundation for further development and enhancements.  
