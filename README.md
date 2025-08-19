# Docker Cleaner

A Python CLI tool to clean up unused Docker resources (containers, images, volumes). Designed for homelabs and development environments to free up disk space.

## Features

- **Safe by default:** Performs a dry-run unless explicitly told to delete.
- **Targeted cleanup:** Choose to remove only stopped containers, dangling images, *or* unused volumes.
- **Dockerized:** Can be run itself as a Docker container for ultimate convenience.

## Installation & Usage

### Method 1: Run directly with Python
1. Clone the repo and navigate into it:
    ```bash
    git clone https://github.com/chrono-vn/docker-cleaner.git
    cd docker-cleaner
    ```
2. (Optional) Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run it!
    ```bash
    # See what would be cleaned
    python cleaner.py

    # Clean everything unused
    python cleaner.py --all
    ```

### Method 2: Run with Docker Compose (Recommended)
1. Clone the repo:
    ```bash
    git clone https://github.com/chrono-vn/docker-cleaner.git
    cd docker-cleaner
    ```
2. **Dry-run (Safe mode):**
    ```bash
    docker-compose run --rm docker-cleaner
    ```
3. **Clean everything:**
    ```bash
    docker-compose run --rm docker-cleaner --all
    ```

## Command Examples

```bash
# Remove all stopped containers
python cleaner.py --containers

# Do a dry-run to see what dangling images exist
python cleaner.py --images --dry-run

# Remove unused volumes and dangling images
python cleaner.py --volumes --images

# The nuclear option: clean all unused resources
python cleaner.py --all
```

## How it Works

This script uses the official [Docker SDK for Python](https://docker-py.readthedocs.io/) to interact with the Docker daemon on your host machine. When run in a container, it mounts the host's Docker socket (`/var/run/docker.sock`), allowing it to manage the host's Docker environment.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a Pull Request (PR) for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
