# Ethereum Address Explorer

This project is a web application that allows users to search for Ethereum addresses and view their current balance and transaction history.

## Features

- Search for any Ethereum address
- Display current balance of the address
- Show a list of transactions associated with the address
- User-friendly web interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/dana120703/ethereum-address-explorer.git
   cd ethereum-address-explorer
   ```

2. Install the required packages:
   ```
   pip install flask requests matplotlib flask-cors
   ```

## Configuration

1. Open `main.py` and replace the `api_key` variable with your own Etherscan API key:
   ```python
   api_key = "YOUR_ETHERSCAN_API_KEY"
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Enter an Ethereum address in the search box and click "Search"

4. View the balance and transaction history for the entered address

## Project Structure
│
├── app.py
├── main.py
├── README.md
└── templates/
└── index.html


- `app.py`: Flask application that handles web requests and renders the UI
- `main.py`: Contains functions for interacting with the Ethereum blockchain via Etherscan API
- `templates/index.html`: HTML template for the web interface

## Contributing

Contributions to the Ethereum Address Explorer are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you want to contact me, you can reach me at `danaabarzinje@gmail.com`.

## Acknowledgements

- [Etherscan](https://etherscan.io/) for providing the API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for the UI components
