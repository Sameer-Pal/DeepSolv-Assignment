# django-fb-scraper

`django-fb-scraper` is a Django application designed to scrape Facebook Marketplace groups and store product information in a database. This tool enables users to efficiently collect and manage data from various Facebook Marketplace listings.

## Features

- **Facebook Marketplace Scraping**: Extract product details from Facebook Marketplace groups.
- **Database Storage**: Save scraped product information into a structured database.
- **Django Integration**: Seamlessly integrates with Django for easy management and customization.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.x**: The programming language used for development.
- **Django**: A high-level Python web framework.
- **Facebook Scraper Library**: A Python library for scraping Facebook data.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ochieng424/django-fb-scraper.git
   cd django-fb-scraper
   ```
   
2. **Set Up a Virtual Environment:** 

        Edit
        python -m venv venv
        source venv/bin/activate  
        On Windows, use `venv\Scripts\activate` 

    
    
3. **Install Dependencies:**

    Install the required Python packages using pip.

       pip install -r requirements.txt

The requirements.txt file includes necessary packages such as Django and the Facebook scraper library.


## Configuration

    Create an `.env` file and add your Facebook credentials:

```ini
    FACEBOOK_EMAIL=your_facebook_email
    FACEBOOK_PASSWORD=your_facebook_password
```


## Apply Migrations:

Set up the database by applying migrations.

```ini
python manage.py makemigrations
python manage.py migrate

```
## Run the Development Server:
**Start the Django development server.**

    python manage.py runserver

**The application will be accessible at** 
    
   ``` 
http://127.0.0.1:8000/home.
```


## Application Flow

### URL Routing  
The URL [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home) is connected to a **view**, which retrieves data from **models** and renders it using an **HTML template**.

### Flow Diagram  
1. **User Request** → The user visits [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home).  
2. **Django View** → The request is handled by a Django **view** function or class.  
3. **Database Interaction** → The view fetches required information from **models**.  
4. **Template Rendering** → The retrieved data is passed to an **HTML template** for display.  
5. **Response to User** → The rendered page is returned to the user’s browser.


