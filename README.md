# Mouse Automation Project

This project is a Python GUI application for automating mouse movements, clicks, and typing random text. The application is designed to simulate human-like interactions with a computer.


## Features

- **Mouse Movement**: Generates and executes human-like mouse movements.
- **Mouse Clicking**: Automates mouse clicking.
- **Typing**: Types random letters or words.
- **Keyboard Monitoring**: Monitors keyboard inputs to stop the automation.

## Prerequisites

- Python 3.x
- Required Python packages (install via `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pavankumarkaki/rewards_automation_project.git
   cd mouse_automation_project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. The GUI will appear with the following options:
   - **Record Coordinate (press 'q')**: Press the 'q' key to record the current mouse position. The coordinates will be displayed in the listbox.
   - **Start Automation**: Starts the automation process using the recorded coordinates.
   - **Stop Automation (press 'esc')**: Press the 'esc' key to stop the automation.

## How It Works

- **Recording Coordinates**: Hover over the desired positions and press 'q' to record the coordinates. Press '0' to stop recording.
- **Automation**: The application will move the mouse to the recorded coordinates, perform clicks, and type random text. The process will repeat for a maximum of 30 cycles or until stopped by pressing 'esc'.

## Modules

- **utils.py**: Contains utility functions for generating random movements and smoothing data.
- **mouse_movement.py**: Handles the generation and execution of mouse movements.
- **mouse_click.py**: Handles mouse clicking.
- **typing.py**: Handles typing random text.
- **keyboard_monitor.py**: Monitors keyboard inputs to stop the automation.
- **gui.py**: Contains the GUI setup and event handling.
- **main.py**: The entry point to run the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please contact pk325530@gmail.com or open an issue on GitHub.
