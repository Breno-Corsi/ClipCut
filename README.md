# ClipCut

![ClipCut Logo](ClipCut.png)

## Overview

ClipCut is an open-source software designed to simplify the process of capturing screenshots from your desktop and automatically removing the background. With ClipCut, you can easily take prints of your screen, and the software will process the images to eliminate any unwanted backgrounds, allowing you to copy the clean images directly to your clipboard for easy use.

## Features

- **Automatic Background Removal**: ClipCut uses algorithms to detect and remove backgrounds from your screenshots.
- **Clipboard Integration**: Once the background is removed, the processed image is copied directly to your clipboard for quick access.
- **User-Friendly Interface**: The intuitive design makes it easy for anyone to take screenshots and remove backgrounds with just a few clicks.
- **Open Source**: ClipCut is open-source software, allowing you to contribute to its development and customize it to your needs.

## Installation

### Pip Prerequisites

- Ensure you have [Python](https://www.python.org/downloads/) installed on your machine.
- Install the required libraries by running:

```bash
pip install -r requirements.txt
```

### Bash Prerequisites

- Install the following packages:
```bash
sudo dnf install gnome-screenshot
sudo dnf install wl-clipboard
```

### Clone the Repository

```bash
git clone https://github.com/Breno-Corsi/clipcut.git
cd clipcut
```

### Run the Application

To start ClipCut, run the following command:

```bash
python main.py
```

## Usage

1. Launch ClipCut.
2. Type "1" to take a new screenshot.
3. Select the area on screen of the image you want.
4. The final image will be copied to your clipboard, ready for use in other applications.

## Contributing

We welcome contributions to ClipCut! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Submit a pull request detailing your changes.

## License

ClipCut is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the software as per the terms of the license.

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository or contact us at [breno.tarefas@gmail.com](mailto:breno.tarefas@gmail.com).

## Acknowledgments

- Special thanks to the libraries and tools that made this project possible.