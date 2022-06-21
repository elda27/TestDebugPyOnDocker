# Practice debugging Python code on docker-compose for VSCode.

In this example, we will run `main.py` on a Docker container.
Then, you can debug the Python process running in the container from VSCode in the host.

## Usage

For release:

```bash
docker-compose up
```

For debugging :
After executing the following command, start debugging on VSCode.

```bash
docker-compose -f ./docker-compose.yaml -f ./docker-compose.debug.yaml up
```

## Implementation

In `docker-compose.debug.yaml`, replace configurations to debug Python.
The following is a list of configurations that are replaced.

- `entrypoint` is replaced with `python -m debugpy`.
- Use and share port 5678 for communication between host and container. (This is the port set in the debugpy argument.)
- Share entrypoint-debug.sh with host.

If you are deleting source code in a Docker container, it may be useful to share the host's source code with the Docker volume.
