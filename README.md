# Client Master

A Python-based GUI application for managing client project structures and assets.

## Description

Client Master is a desktop application that helps automate the creation of client project structures. It provides a simple interface to create organized client folders with associated assets, specifically designed for managing .pur files in a network environment.

## Features

- Simple and intuitive GUI interface
- Automated client folder structure creation
- Asset file management (.pur files)
- Network path support
- Error handling and user feedback
- Dark mode interface

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- Network access to specified paths

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TorresVisual/client_master.git
```

2. Navigate to the project directory:
```bash
cd client_master
```

3. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

1. Run the application:
```bash
python client_master.py
```

2. Enter the client's name in the input field
3. Click "Create Structure" to generate the client folder and copy the necessary assets

## Project Structure

```
client_master/
├── assets/
│   └── NewScene.pur
├── client_master.py
└── README.md
```

## Configuration

The application uses the following default paths:
- Base path: `\\ORTHANC\Fileserver\Torres\Ark Assets\Projects`
- Source .pur file: `\\ORTHANC\Fileserver\Torres\My Programms\Client Master\assets\NewScene.pur`

To modify these paths, edit the `on_submit()` function in `client_master.py`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- TorresVisual 