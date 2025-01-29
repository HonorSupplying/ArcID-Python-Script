import os
import requests
import base64

def image_to_base64(image_path):
    """Converts an image to a Base64-encoded string."""
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            return encoded_string
    except Exception as e:
        print(f"Error converting {image_path} to Base64: {e}")
        return None

def create_user_api(name,api_url):
    """ Create user function api """
    try:
        response = requests.post(api_url+"/api/v1/users",{
            "external_id" : name
        },headers={
            "Content-Type" : "application/json",
            "Accept" : "application/json",
            "x-api-key" : "hid_arcid"
        },verify="server.pem")
        print(response.json())
        print(response.content)
        return response.status_code
    except Exception as e:
        print(f"Failed: {e}")
        return None
    

async def add_image_api(user_id):
    """ Add image to user """
   

def create_and_add(name,image_path, api_url):
    """Mock function to send an image to an API."""
    try:
        print(f"Processing: {image_path}")
        base64 = image_to_base64(image_path)
        res = create_user_api(name,api_url)
        if res == 200:
            res = add_image_api()

        # with open(image_path, 'rb') as f:
        #     image_file = f.read()
        #     files = {'image': image_file}
        #     response = requests.post(api_url, files=files)
        #     print(response.content)
        #     print(response.status_code)
        #     if response.status_code == 200:
        #         print(f"Successfully uploaded: {image_path}")
        #         return image_path
        #     else:
        #         print(f"Failed to upload {image_path}: {response.status_code}")
        #         return None
    except Exception as e:
        print(f"Error uploading {image_path}: {e}")
        return None


def process_images(folder_path, api_url):
    """Finds images in a folder, uploads them concurrently, and deletes successfully sent ones."""
    image_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) 
                   if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
    filename = os.listdir(folder_path)

    for index,name in enumerate(filename):
        create_and_add(name,image_paths[index],api_url)


if __name__ == "__main__":
    
    IMAGE_FOLDER = "./img"  # Change to your folder path
    API_ENDPOINT = "https://127.0.0.1"  # Change to your API URL
    process_images(IMAGE_FOLDER, API_ENDPOINT)
    

    # image_path is set of all image in folder
    # for index,paths in enumerate(image_paths) :
    #     print(paths)
    #     base64 = image_to_base64(paths)
    #     upload_image(image_paths[0],api_url)
            
    
    
    # for image_path in results:
    #     if image_path:
    #         os.remove(image_path)
    #         print(f"Deleted: {image_path}")
