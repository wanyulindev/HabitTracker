import datetime

# Step 1. - Using request.post() to create new user account:
import requests

USERNAME = "wanyudevtest"
TOKEN = "shdjkhfewuroidfjlk"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# After I created the username and everything, I may hide these two line for later:
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# Q:
# Instead writing response = requests.post(pixela_endpoint, json=user_params), why not just
# write response = requests.post(pixela_endpoint, params=user_params)
# GPT:
# Using json: When you use the json parameter, the data is sent as a JSON object in the
# request body. This is typically used when you need to send structured data, such as when
# working with RESTful APIs that expect JSON payloads. The json parameter will automatically
# set the Content-Type header to application/json.
#
# Using params: The params parameter is used to send data as URL query parameters in the
# request URL. This is commonly used for GET requests and for some APIs that accept POST
# requests with data encoded in the URL. It does not send the data in the request body,
# and it's not the right choice for sending structured JSON data.
#
# In your case, if the Pixela API expects user creation data to be sent as a JSON object
# in the request body, then using json is the correct choice. If you were to use params,
# the data would be appended to the URL as query parameters, which is likely not what the
# API expects for user creation.
#
# Always refer to the API documentation for the specific requirements on how to send data,
# and use the appropriate method (json or params) based on the API's specifications.
#--------------------------------------------------------------------------------------------
# Step 2. - create graphs:
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPHID = "graph1"

graphs_config = {
    "id": GRAPHID,
    "name": "Walks Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# Since we already succeeded to create our graphs, let's just hide it out:
# response = requests.post(graphs_endpoint, json=graphs_config, headers=headers)
# print(response.text)
# print(graphs_endpoint)
#----------------------------------------------------------------------------------------------
# Step 3. - Challenge: Add a Pixel to the Habit Tracker using a Post Request:

pixel_endpoint = f"{graphs_endpoint}/{GRAPHID}"

CURRENT = str(datetime.datetime.now().date()).replace("-", "")
# print(CURRENT)
# or we could also write as:
# today = datetime.datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": CURRENT,
    "quantity": "2.35"
}

# response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)
# Well done!
#---------------------------------------------------------------------------------------------
# Step 4. - Talk about how to delete/update using requests:




#---------------------------------------------------------------------------------------------
# Initial commit:
# Q: for ChatGPT:
# could you suggest me how to avoid facing the same conflict next time when i create a
# new repo in local directory, and also create a new remote at my github, and try to connect
# them together?
#
# ChatGPT
# Certainly! To avoid facing conflicts when creating a new repository in your local directory
# and connecting it to a new remote on GitHub, you can follow these steps:
#
# Create the Local Repository:
# First, create a new directory on your local machine where you want to store your project.
# Open a terminal window and navigate to the directory you just created.
# Run the following commands to initialize a new Git repository:
# csharp
# Copy code
# git init

# Add Your Project Files:
# Copy or create your project files within this directory.
# Create an Initial Commit:
# Run the following commands to add your project files to the Git repository and make an
# initial commit:
# sql
# Copy code
# git add .
# git commit -m "Initial commit"

# Create a New Repository on GitHub:
# Go to GitHub (https://github.com) and log in to your account.
# Click the '+' icon in the top right corner and select 'New repository.'
# Follow the instructions to create a new repository on GitHub. You can choose to initialize
# it with a README file or not, depending on your preference.

# Connect the Local and Remote Repositories:
# On the GitHub repository page, you will see the repository's URL
# (e.g., https://github.com/your-username/your-repo.git). Copy this URL.
# In your terminal, add the remote repository as follows, replacing the URL with the one you
# copied:
# csharp
# Copy code
# git remote add origin https://github.com/your-username/your-repo.git
# Verify that the remote has been added correctly:
# Copy code
# git remote -v

# Push Your Local Repository to GitHub:
# Finally, push your local repository to GitHub:
# css
# Copy code
# git push -u origin main

# This command pushes your code to the 'main' branch on GitHub. If you're using a different
# branch name, replace 'main' with your branch name.
# By following these steps, you should be able to create a new repository on GitHub and
# connect it to your local repository without running into unrelated history conflicts.
# It's important to initialize a new local repository first, make an initial commit, and
# then add the remote. This sequence usually prevents unrelated history conflicts.
#----------------------------------------------------------------------------------------------

