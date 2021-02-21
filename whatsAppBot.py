"""
Created by: Dhiraj
Date: 02/06/2021

info: This program can not only send whatsapp messages to number, but also can send
        geo-location and files. If someone have lots of contacts and messages to send,
        there is a function "read_contact_file_and_send_msgs" which can read csv file
        and send whatsapp msgs, file or location to the particular number (Please refer
        the given CSV for the format or else error will throw)
"""

# Importing packages
import json
from csv import reader
from requests import post


class WABot:

    # Initializing baseurl and token from env_var file
    def __init__(self):
        file = open("env_var.json", "r")
        api = json.loads(file.read())
        self.baseurl = api['url']
        self.token = api['token']
        # print(api)

    # This method send all type of messages using method type.
    def send_requests(self, method, data):

        url = f"{self.baseurl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    # --------------------------------------------------------------------------------
    # This method is used for sending text messages
    def send_message(self, phone_no, text):
        data = {"phone": phone_no,
                "body": text}

        result = self.send_requests(method='sendMessage', data=data)
        return result

    # --------------------------------------------------------------------------------
    # This method is used for sending geolocation
    def geo(self, latitude, longitude, address, phone_no):
        data = {
            "lat": latitude,
            "lng": longitude,
            "address": address,
            "phone": phone_no
        }

        answer = self.send_requests('sendLocation', data)
        return answer

    # --------------------------------------------------------------------------------
    # This method is used for sending file
    def file(self, phone_no, format, file_location, file_description):
        available_files = {'doc': 'document.doc',
                           'gif': 'giffile.gif',
                           'jpg': 'jpgfile.jpg',
                           'png': 'pngfile.png',
                           'pdf': 'presentation.pdf',
                           'mp4': 'video.mp4',
                           'mp3': 'mp3file.mp3'}

        if format in available_files.keys():
            data = {
                'phone': phone_no,
                'body': file_location,
                'filename': available_files[format],
                'caption': f'{file_description} {available_files[format]}'
            }

            return self.send_requests('sendFile', data)

    # --------------------------------------------------------------------------------
    # This method is read csv file and according to type(text or location or file) it will send msgs to the contact
    def read_contact_file_and_send_msgs(self, file_name):

        success = 0
        fail = 0
        result = None
        error_list = []

        with open(file_name, 'r') as file:
            read_file = reader(file, delimiter=';')
            next(read_file)

            for line in read_file:
                # print(line)
                contact = line[0]
                msg = line[1]

                try:

                    if line[2] == "text":
                        result = self.send_message(phone_no=contact, text=msg)

                    elif line[2] == "loc":
                        lat = line[3]
                        lng = line[4]
                        result = self.geo(phone_no=contact, latitude=lat, longitude=lng, address=msg)

                    elif line[2] == "file":
                        file_location = line[5]
                        file_format = file_location[-3:]
                        result = self.file(phone_no=contact, format=file_format, file_location=file_location,
                                           file_description=msg)
                    else:
                        print("Error: Unknown Message Type")
                        error_list.append([contact, "Error: Unknown Message Type"])
                        fail += 1
                        continue

                    # print(result)
                    if result['sent']:
                        print("message successfully sent to: " + contact)
                        success += 1
                    else:
                        print("Error: " + result['message'])
                        error_list.append([contact, result['message']])
                        fail += 1

                except IndexError as e:
                    print("Error: " + result)
                    error_list.append([contact, result, e])
                    fail += 1

        print("No. of Successful Messages sent = ", success)

        if fail > 0:
            print("No. of UnSuccessful Messages sent = ", fail)
            print("Fail List", error_list)


# --------------------------------------------------------------------------------
if __name__ == "__main__":
    bot = WABot()

    # calling send_message method to send a particular message to a number
    # bot.send_message("919876543210", "Hello, How are you ")

    # Pass file name and it will send all msgs from csv file
    # bot.read_contact_file_and_send_msgs(file_name)
