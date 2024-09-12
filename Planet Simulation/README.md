#### .env file
```dotenv
WIDTH=1000
HEIGHT=800
AU=149600000000
G=6.67428e-11
SCALE=0.00000167677   # 250 / AU
TIMESTEP=86400
```


### Explanation of Changes

1. **SOLID Principles**:
   - **Single Responsibility Principle**: Each class has a single responsibility. The `Planet` class handles planet details, while the `PlanetFactory` encapsulates the creation of planets.
   - **Open-Closed Principle**: The factory design allows adding new types of planets without modifying existing code.
   - **Liskov Substitution Principle**: The `SimplePlanetFactory` can be substituted for any other factory implementations without altering the main logic.
   - **Inversion of Control**: Dependency injection is achieved via the factory pattern—`main` does not create planets directly but through the factory.
   - **Dependency Injection**: The `PlanetFactory` is instantiated inside `main`, decoupling the creation of `Planet`.

2. **GoF Design Patterns**:
   - **Abstract Factory**: Implemented for creating planets, allowing flexibility in how planets are instantiated.
   - **Adapter and others**: Not applied here given the primary structure, but could be integrated based on future requirements.

3. **Environment Variables**: Constants such as dimensions and gravitational constant are loaded from a `.env` file to allow easy configuration.
