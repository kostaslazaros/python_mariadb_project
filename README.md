# Python MariaDB project

To use, follow the steps below:

## Python requirements

- Python version >= 3.9

- Create virtual environment

  - for windows:

    ```
    python -m venv venv

    venv\Scripts\activate

    pip install -r requirements.txt
    ```

  - for linux:

    ```
    python -m venv venv

    venv/bin/activate

    pip install -r requirements.txt
    ```

  - for conda:

    ```
    conda create -n <your_env_name>

    conda activate <your_env_name>

    conda install --file requirements.txt
    ```

## How to run docker
- To install, follow the instructions [here](https://docs.docker.com/engine/install/)

- From command line, run (in the project's directory):

    ```
    docker compose up -d
    ```


## How to run

- Open console.

- Activate virtual environment.

- Run the following command:

  ```
  python main.py
  ```