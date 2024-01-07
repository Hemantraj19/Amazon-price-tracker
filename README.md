# Amazon Price Tracker with Twilio Notifications

## Overview
This Python script allows you to track the price of a product on Amazon and receive notifications via Twilio when the price drops below a specified threshold.

## Prerequisites
1. Python 3
2. Install required packages:
    ```bash
    pip install beautifulsoup4 requests twilio
    ```

## Configuration
1. Sign up for a Twilio account and obtain your Account SID and Auth Token.
2. Replace `"your account sid"` and `"your auth token"` in the code with your actual Twilio Account SID and Auth Token.
3. Set up a Twilio phone number and replace `'number_you_got_from_twilio'` with your Twilio phone number.
4. Enter your phone number in the `'your_phone_number'` field.

## Usage
1. Run the script.
    ```bash
    python script_name.py
    ```
2. Enter the Amazon product link when prompted.
3. The script will fetch the current product details and price.
4. Set the minimum price threshold for notification when prompted.

## Notifications
If the current price falls below the specified threshold, you will receive a Twilio SMS notification with the product title and updated price.

## Important Note
Ensure that you have the necessary permissions to scrape data from the Amazon website and comply with their terms of service.

Feel free to modify the code according to your needs.
