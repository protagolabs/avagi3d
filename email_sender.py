import httpx
from typing import List
import asyncio

import os
import time



# The function to perform the async POST request
async def send_email_payloads(payloads: List[dict]):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payloads)
            if response.status_code == 200:
                return response.json()  # or response.text if response is not JSON
            else:
                return f"Request failed with status code: {response.status_code}"
        except Exception as e:
            return f"An error occurred: {e}"
            
            
if __name__ == "__main__":


    cwd = os.getcwd()
    data_path = os.path.join(cwd, "charactors")

    # The URL to which the POST request should be made
    url = 'http://3.8.207.30:8777/emails/send'

    while True:

        email_names = os.listdir(data_path)

        for e in email_names:

            file_dir = os.path.join(data_path, e)
            file_dir = os.path.join(file_dir, "model.glb")
            if os.path.exists(file_dir):
                # Define the payload according to the EmailSendingPayload structure
                # to_message_id and to_thread_id can be found from before
                # to_email, as previous example, is zhouhan.zhang@netmind.ai
                # processed_img_s3_path is the 3d mesh you generated
                payloads = [
                    {
                        "to_email": e,
                        "to_message_id": "18e670c669812e27",
                        "to_thread_id": "18e619bbb1942536",
                        "processed_img_s3_path": file_dir
                    }
                    # You can add more dictionaries to this list as needed.
                ]




                asyncio.run(send_email_payloads(payloads))
                
                print(payloads)

        time.sleep(120)