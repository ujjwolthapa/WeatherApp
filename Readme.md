# WeatherApp

A Django-based web application that displays real-time weather information for any city using the [OpenWeatherMap API](https://openweathermap.org/api). Built with Python, HTML, and CSS — containerized with Docker and deployed on PythonAnywhere.

🌐 **Live Demo:** [ujjwol.pythonanywhere.com](http://ujjwol.pythonanywhere.com/)

---

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3.8, Django                |
| Frontend   | HTML, CSS                         |
| API        | OpenWeatherMap API                |
| Container  | Docker, Docker Compose            |
| CI/CD      | GitHub Actions                    |
| Hosting    | PythonAnywhere                    |

---

## Project Structure

```
WeatherApp/
├── weather/                  # Django app — views, models, URLs
├── weatherapp/               # Django project settings
├── templates/                # HTML templates
├── static/                   # CSS and static assets
├── stagingfolder/            # Staging environment files
├── manage.py                 # Django management script
├── Dockerfile                # Container image definition
├── docker-compose.yml        # Docker Compose configuration
└── .github/
    └── workflows/            # GitHub Actions CI/CD pipelines
```

---

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- An [OpenWeatherMap API key](https://openweathermap.org/api)

### Run Locally (without Docker)

```bash
# Clone the repo
git clone https://github.com/ujjwolthapa/WeatherApp.git
cd WeatherApp

# Install dependencies
pip install django

# Run the development server
python manage.py runserver
```

Visit: `http://localhost:8000`

---

## Docker

### Using Docker Compose (recommended)

Pulls the pre-built image from Docker Hub and starts the app:

```bash
docker compose up
```

Visit: `http://localhost:8000`

### Build & Run Manually

```bash
# Build the image
docker build -t weatherapp .

# Run the container
docker run -p 80:80 weatherapp
```

Visit: `http://localhost`

---

## Configuration

You will need an OpenWeatherMap API key to fetch weather data. Get one for free at [openweathermap.org](https://openweathermap.org/api) and set it in the appropriate settings file:

```python
# weather/views.py or settings
API_KEY = 'your_openweathermap_api_key'
```

---

## CI/CD — GitHub Actions to AWS EC2

The project uses GitHub Actions with a **self-hosted runner registered on an AWS EC2 instance** for automated builds, Docker Hub pushes, and live deployment.

### How It Works

The self-hosted runner is installed directly on the EC2 instance. When a workflow triggers, GitHub Actions runs the job on that EC2 machine — building the Docker image, pushing it to Docker Hub, and immediately running `docker compose up` to deploy the updated container on the same instance. This means every push to `staging` results in an automatic live deployment on EC2 with zero manual steps.

### Staging Workflow (`.github/workflows/staging.yml`)

**Trigger:** Push to the `staging` branch

**Steps:**
1. Checkout code
2. Set up Python 3.8
3. Build Docker image → `<DOCKER_USER>/weatherapp:latest`
4. Login to Docker Hub
5. Push image to Docker Hub
6. Run `docker compose up` on the EC2 instance — app is live immediately

```bash
git push origin staging
# → triggers build, push, and deploy on EC2 automatically
```

### Setting Up the Self-Hosted Runner on EC2

1. Launch an EC2 instance (Ubuntu recommended) and ensure Docker & Docker Compose are installed
2. In your GitHub repo, go to **Settings → Actions → Runners → New self-hosted runner**
3. Follow the instructions to download and configure the runner on the EC2 instance
4. Start the runner:
   ```bash
   ./run.sh
   ```
5. Add the required secrets in **Settings → Secrets and variables → Actions**

### Required Secrets

| Secret            | Description              |
|-------------------|--------------------------|
| `DOCKER_USERNAME` | Docker Hub username      |
| `DOCKER_PASSWORD` | Docker Hub password      |

---

## Live Deployment

The app is deployed and accessible at:

**[http://ujjwol.pythonanywhere.com/](http://ujjwol.pythonanywhere.com/)**

---

## License

This project is open source. See the [LICENSE](LICENSE) file for details.
