# WhatsApp Bot with DialoGPT Model

## Project Description

The WhatsApp Bot with DialoGPT Model is an automated chat bot designed to interact with users on WhatsApp. It leverages the DialoGPT language model to generate contextually relevant responses to user messages. The project uses Python for the bot's logic and Selenium for web automation to handle interactions with WhatsApp Web.

This project is ideal for understanding web automation, natural language processing, and the integration of AI models in real-world applications.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

### Prerequisites
- Python 3.6 or higher
- Chrome browser installed
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (Ensure the version matches your Chrome browser)

### Python Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/whatsapp-bot-dialoGPT.git
   cd whatsapp-bot-dialoGPT
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install required packages:**
   ```bash
   pip install selenium transformers torch
# Additional Configuration
- Update the PHONE_NUMBER variable in the script with the recipient's phone number. Ensure the phone number is in the international format (e.g., for Israel, use 972123456789).
## Usage
1. **Run the bot:**
   ```bash
   python whatsapp_bot.py
2. **Scan the QR code:**
When the browser opens, scan the WhatsApp Web QR code with your phone to log in.

3. **Interact with the bot:**
The bot will start the conversation by sending predefined initial messages and will respond to incoming messages based on predefined rules and the DialoGPT model.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
