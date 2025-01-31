# HSE Football API

## Getting Started

### Prerequisites
Make sure you have the following installed on your system:

- [Git](https://git-scm.com/)
- [PDM](https://pdm-project.org/en/latest/#installation) 
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation
1. **Clone the repository:**  
   ```shell
    git clone git@github.com:zrasute/hse_football_api.git
    cd hse_football_api
2. **Install all dependencies:**
    ```shell
    pdm install
    eval $(pdm venv activate)
    ```
3. **Set up environment variables**  
Copy the .env.template files and rename them to .env, then update the necessary values.
   ```shell
   cp .env.template .env
   ```
4. **Start PostgreSQL database via Docker Compose:**
    ```shell
    docker compose up -d
    ```
5. **Run FastAPI application using [PDM Scripts](https://pdm-project.org/en/latest/usage/scripts/):**
    ```shell
    pdm run dev_start
    ```
