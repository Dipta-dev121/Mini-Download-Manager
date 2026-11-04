# MiniDM

MiniDM is a small command-line file downloader written in Python. It prompts for a URL, makes an HTTP request, and saves the response as `downloads/file.zip`.

## Implemented Features

- Prompts for a download URL in the terminal.
- Sends an HTTP GET request using the `requests` library.
- Checks the HTTP response status and reports request failures.
- Saves a successful response to the fixed path `downloads/file.zip`.

The output name and location are currently fixed. The program does not yet provide a graphical interface, progress reporting, or options for choosing the output file.

## Project Structure

```text
MiniDM/
|-- app/
|   |-- downloader.py   # Makes the request and writes the response to disk
|   |-- main.py         # Prompts for the URL and starts the download
|   |-- models.py       # Currently empty
|   `-- utils.py        # Currently empty
|-- downloads/          # Download destination when run as described below
|-- requirements.txt    # Python package dependencies
|-- .gitignore
|-- README.md
`-- venv/               # Local virtual environment created during setup
```

## Installation on Windows

Open PowerShell or Command Prompt in the project folder.

1. Create a virtual environment:

   ```powershell
   py -m venv venv
   ```

2. Activate it in PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   Or activate it in Command Prompt:

   ```bat
   venv\Scripts\activate.bat
   ```

3. Install the project dependencies from the project folder:

   ```powershell
   python -m pip install -r requirements.txt
   ```

## Run the Application

From the project folder, change into `app` and start the entry point:

```powershell
cd app
python main.py
```

Run the application from the `app` directory because the destination path is relative to the current working directory. When launched as above, the downloaded response is written to `downloads/file.zip` in the project folder. Running it from another directory may write to a different location or fail if that destination does not exist.

## Usage Example

Start the application, then paste a direct URL when prompted:

```text
Enter download url: https://example.com/archive.zip
Download Complete!
```

On success, the response is saved as `downloads/file.zip`, regardless of the name in the URL. If the HTTP request fails, the program prints a `Download failed:` message with the request error. The URL in this example is illustrative; use a URL that serves the file you intend to download.

## Technologies

- Python
- `requests` for HTTP requests
- `venv` and `pip` for environment and dependency management
- Dependencies listed in `requirements.txt`: `requests`, `certifi`, `charset-normalizer`, `idna`, and `urllib3`

## Roadmap

These are possible future improvements and are **not implemented** in the current version:

- Allow users to choose the output directory and filename.
- Stream large downloads and show progress.
- Add request timeouts and retry handling.
- Add command-line options for supplying a URL without an interactive prompt.
- Add tests and meaningful functionality for the currently empty `models.py` and `utils.py` modules, if needed by future features.