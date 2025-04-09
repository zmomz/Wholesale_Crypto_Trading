# Wholesale Crypto Trading

This project provides a streamlined web interface for cryptocurrency wholesale trading operations. Built using Python, Streamlit, and integrated with Binance's cryptocurrency trading API via `ccxt`, it enables users to manage buy and sell trades efficiently and intuitively.

## Objective

- Provide a simple and efficient interface for wholesale cryptocurrency trading.
- Enable users to execute trades directly on Binance.
- Allow real-time balance checks, order management, and profitability tracking.

## Key Features

- **Interactive Web Interface:** Easy-to-use Streamlit-based UI.
- **Real-Time Binance Integration:** Execute buy/sell orders via Binance API.
- **Balance & Cost Management:** Clearly display available balances and estimated trade costs.
- **Flexible Trading Options:** Supports bulk trade execution, selective coin trading, and automatic price updates.

## Technologies and Tools

- Python
- Streamlit
- Binance API (via ccxt)
- SQLite (for internal state management)

## Repository Structure

- `main.py`: Main Streamlit app interface.
- `model.py`: Business logic for trading operations and data handling.
- `data.db`: SQLite database file for state management.
- `logo.png`: App branding logo.
- `requirements.txt`: Python package dependencies.
- `procfile` & `setup.sh`: Deployment scripts.

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/zmomz/Wholesale_Crypto_Trading.git
cd Wholesale_Crypto_Trading
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run main.py
```

### 4. Configure Binance API
- Obtain API Key and Secret from [Binance API](https://www.binance.com/en/api-management).
- Enter these credentials within the Streamlit sidebar interface.

## Usage

### Buying Cryptocurrencies:
- Select trading pairs and specify USDT amount per trade.
- Review balance and estimated costs before executing orders.

### Selling Cryptocurrencies:
- Automatically updates prices for wallet-held coins.
- Select coins individually or in bulk based on profitability.
- Set the sell amount either in USD or as a percentage.

## Contributions

Contributions and improvements are welcome. Submit a pull request or open an issue for discussion.

## License

This repository is under the MIT License. See the [LICENSE](LICENSE) file for more details.

