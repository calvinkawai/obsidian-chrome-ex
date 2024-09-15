# Obsidian Chrome Extension

Create a markdown file using a Chrome extension given file name and tags.

New file contains YAML-style properties such as created date, tags, source(current chrome url).

## Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Load the frontend to the Chrome extension:
   - Navigate to `chrome://extensions/`
   - Click on "Load unpacked"
   - Locate the `frontend` folder of the project and select it

## Running the Backend

1. Create a copy of the `.env-example` file:

   ```bash
   cp .env-example .env
   ```

2. Set the value for `MARKDOWN_PATH` in the `.env` file to specify the directory for new markdown files.

3. Run the backend:

   ```bash
   fastapi run backend
   ```

## Demo

### Create a New Note

![Screenshot 2024-09-15 at 12 13 41 AM](https://github.com/user-attachments/assets/aa215adb-17cd-4316-bd5f-95f72449d5be)

### New Note

![Screenshot 2024-09-15 at 12 15 56 AM](https://github.com/user-attachments/assets/b674dc5c-71cc-48b3-872b-5c5523440237)
