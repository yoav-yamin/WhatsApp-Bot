from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

# Initialize model and tokenizer
MODEL_NAME = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Function to generate a response using the DialoGPT model
def auto_respond(user_input):
    user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    generated_ids = model.generate(user_input_ids,
                                   max_length=1000,
                                   pad_token_id=tokenizer.eos_token_id,
                                   attention_mask=torch.ones(user_input_ids.shape, device=user_input_ids.device))
    response_ids = generated_ids[:, user_input_ids.shape[-1]:][0]
    response = tokenizer.decode(response_ids, skip_special_tokens=True)
    return response


# Set up URLs
BASE_URL = "https://web.whatsapp.com/"
CHAT_URL_TEMPLATE = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

# Initialize web browser
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(BASE_URL)
browser.maximize_window()

# Define phone number and initial messages
PHONE_NUMBER = "972123456789"  # Modify this phone number as needed
INITIAL_MESSAGE_1 = "Hi There. This is the bot I'm creating"
INITIAL_MESSAGE_2 = "Hello, I am a WhatsApp bot"


# Function to open a chat with a specific phone number
def open_chat(phone_number):
    browser.get(CHAT_URL_TEMPLATE.format(phone=phone_number))
    time.sleep(12)
    input_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, input_box_xpath)))
    return input_box


# Function to send a message in the chat
def send_message(input_box, message):
    input_box.send_keys(message)
    input_box.send_keys(Keys.ENTER)
    time.sleep(5)


# Function to get the last message received in the chat
def get_last_message():
    last_message_xpath = "//div[contains(@class, 'message-in')]//span[contains(@class, 'selectable-text')]"
    user_messages = browser.find_elements(By.XPATH, last_message_xpath)
    if user_messages:
        return user_messages[-1].text, user_messages[-1].id
    return None, None


# Function to handle incoming messages and respond accordingly
def handle_messages(input_box):
    last_received_message, last_message_id = get_last_message()
    close_chat = False

    while not close_chat:
        while True:
            current_message, current_message_id = get_last_message()
            if current_message_id != last_message_id:
                last_received_message = current_message
                last_message_id = current_message_id
                break
            time.sleep(1)

        if current_message.lower() == "hello":
            send_message(input_box, INITIAL_MESSAGE_2)
        elif current_message.lower() == "date":
            now = datetime.now()
            date_time_str = now.strftime("%d/%m/%Y %H:%M:%S")
            send_message(input_box, date_time_str)
        elif current_message.lower() == "bye":
            send_message(input_box, "Have a good day!")
            close_chat = True
        else:
            response = auto_respond(current_message)
            send_message(input_box, response)


# Start the conversation
input_box = open_chat(PHONE_NUMBER)
send_message(input_box, INITIAL_MESSAGE_1)
handle_messages(input_box)

# Close the browser
browser.close()
