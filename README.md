# WhatsApp_Bot

This program can not only send whatsapp messages to number, but also can send geo-location and files. If someone have lots of contacts and messages to send, there is a function "read_contact_file_and_send_msgs" which can read csv file and send whatsapp msgs, file or location to the particular number (Please refer the given CSV for the format or else error will throw). 

### If you want to send messages to the contacts which are not in your contact list, Don't worry it will still send the messages.

## Steps to follow:
1) Go to https://app.chat-api.com . This site can give 3 days free trial without any restriction for sending any particular numbers of messages. Also check for its subscription.
2) Create an account and login.
3) Get the API URL and token from dashboard, which will be like following:
   e.g Your API URL https://eu67.chat-api.com/instance2XXXXX/ and token vfpvt1xxxxxxxxxx
4) Copy this URL and token paste into env_var.json file.
5) You will get a QR Code to scan in that website. Scan through your mobile whatsapp number from which you want to send messages.
6) That's All. You can use the code now.


CSV Format should be like (delimiter should be semicolon(;)):
---
contact;msg;type;latitude;longitude;location  
9170708xxxxx;Hi there;text;;;  
9180151xxxxx;This is the place;loc;51.51916;-0.139214;  
9190245xxxxx;See this file;file;;;https://www.libreoffice.org/themes/libreofficenew/img/logo.png  

Note: Phone number should be with country code("+" not required)
      e.g. 919876543210

![](https://github.com/Dhiraj47/WhatsApp_Bot/blob/main/files/csv.PNG)

### Output (For sending messages from csv file:
![](https://github.com/Dhiraj47/WhatsApp_Bot/blob/main/files/output.PNG)
