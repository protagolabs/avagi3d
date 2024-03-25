#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import httpx
import requests

import asyncio  
import time


async def main(data_path):
    """ Main program """


    url = "http://3.8.207.30:8777/images"
    params = {
        "current_date_str": "2024-03-22"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()
    
    print(data)
    senders = []
    senders_num = {}
    for d in data:
        sender = d["sender"]
        if sender not in senders:
            senders_num[sender] = 0
            senders.append(sender)
    
    print(senders_num)
    url2 = 'http://3.8.207.30:8777/images/download'
    


    for i, d in enumerate(data):
        print(d)

        idx = d["img_s3_path"]
        id0 = idx.find("<") + 1
        id1 = idx.find(">")

        email_id = idx[id0:id1]

        # print(email_id)

        if not os.path.exists(os.path.join(data_path, email_id)):
            os.mkdir(os.path.join(data_path, email_id))

    


        params = {'img_s3_path': d['img_s3_path']}



        # Perform the GET request and get the response
        try:
            response = httpx.get(url2, params=params)
            # Check if the request was successful
            if response.status_code == 200:
                # Response is successful. We would normally process the response here.
                response_text = response.text.strip('\'"')
            else:
                response_text = f"Request failed with status code: {response.status_code}"
        except Exception as e:
            response_text = f"An error occurred: {e}"

        # print(response_text)

        def download_file_from_s3(download_url, local_file_path):
            """
            Downloads a file from an S3 link and saves it to a local file path.

            Parameters:
            - download_url: The URL to the S3 file (can be a signed URL for private files).
            - local_file_path: The local path where the file should be saved.
            """
            
            try:
                response = requests.get(download_url)
                
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Open the local file in binary write mode and save the content
                    with open(local_file_path, 'wb') as file:
                        file.write(response.content)
                    print(f"File successfully downloaded to {local_file_path}")
                else:
                    print(f"Failed to download file. Status code: {response.status_code}")
            
            except Exception as e:
                print(f"An error occurred: {e}")

        # Example usage
        download_url = response_text # This should be your actual S3 URL



        local_file_path = os.path.join(data_path, email_id, "image{}.png".format(senders_num[d['sender']]))  # Specify your desired local path, please use the full path
        download_file_from_s3(download_url, local_file_path)

        senders_num[d['sender']] += 1
            
            

if __name__ == "__main__":

    cwd = os.getcwd()
    data_path = os.path.join(cwd, "images")

    while True:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(data_path))
        time.sleep(120)





