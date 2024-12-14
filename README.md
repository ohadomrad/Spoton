# Spoton Final DS Project


## ML Prerequisites

### Download And Install Requirements

1. Download and install [Python 3](https://www.python.org/downloads/)
   1. Or an IDE with Python like [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)
2. Create a venv under the ml folder
   1. PyCharm - configure interpreter and determine the .venv location
   2. Or create venv using terminal 
      ```
      python -m venv myenv
      ```
3. Activate the .venv
   1. for Windows
      ```
          .\.venv\Scripts\activate
      ```
   2. for macOS/Linux
      ```
          source myenv/bin/activate
      ```
4. Install the required Python packages with:
    ```
    pip install -r .\ml\requirements.txt
    ```

### Configure Environemnt Variables

1. Create a new file named `.env` in the root directory of the project.

2. Copy the content of the [.env.template](/.env.template) file to your newly created `.env` file.

3. Edit the values of the properties to match your environment.


## Run Data Collection Scripts

- To Collect Data Separately:

    Open a terminal and run:

  - Deezer
    ```
    python .\ml\src\data_collection\deezer_callect_data.py
    ```
  - Spotify
    ```
    python .\ml\src\data_collection\spotify_collect_data.py
    ```
  - Google
    ```
    python .\ml\src\data_collection\google_collect_data.py
    ```