# Deploy a simple django hello world app to Heroku

This repository is a simple Django project that is ready for deployment on Heroku. To successfully deploy this project, please follow the instructions below:

## Prerequisites

Before getting started with the deployment process, ensure that you have the following:

- A Heroku account
- The Heroku CLI installed on your machine
- Python 3 installed on your machine

## Steps for Deployment

1. Clone this repository to your local machine.
2. Create a virtual environment for this project using the following command:
    
    ```
    python3 -m venv env
    ```
    
3. Activate the virtual environment using the following command:
    
    ```
    source env/bin/activate
    ```
    
4. Install the required packages using the following command:
    
    ```
    pip install -r requirements.txt
    ```
    
5. Generate a new secret key for your Django project. You can use any online tool or generate it using the following command:
    
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
    
    Copy the generated secret key.
    
6. Create a new file named `.env` in the root directory of the project. Add the following lines to it:
    
    ```
    SECRET_KEY={your_secret_key}
    DEBUG=True
    ```
    
    Replace `{your_secret_key}` with the secret key you generated in step 5.
    
6. Test the project locally using the following command:
    
    ```
    python manage.py runserver
    ```
    
    Open your browser and go to `http://localhost:8000/`
    
10. Create a new app on Heroku and link it to this repository.

    ```
    heroku create
    ```

11. Add the following environment variables in the Heroku app settings:

    ```
    SECRET_KEY={your_secret_key}
    DISABLE_COLLECTSTATIC=1
    ```

Replace `{your_secret_key}` with the secret key you generated in step 5.

12. Deploy the app to Heroku using the following command:

    ```
    git push heroku master
    ```

Wait for the deployment to finish.

13. Test the app on Heroku by opening it in your browser.

## Issues

Any issues with the deployment process? Please open an issue on this repository.