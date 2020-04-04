# Django Framework Hotel Website

![alt text](https://github.com/Kenneth-Lund/Django-Hotel-Website/blob/master/readme_image.png)
**UX created by Kenneth Lund**

This project was created with the intention of learning the basic fundamentals of the Django web framework.

## App Structure

* **home_page**
  * Calls simple_site_api for dummy JSON data
  * Renders HTML/CSS templates
  * Handles AJAX call for HTML template updating
  * URLS:
     http://localhost/home-page/               (Presents homepage)
     http://localhost/update-preview-list/id=  (Updates homepage preview list based on AJAX call within template)

* **simple_site_api**
  * Provides data for the home_page views using Django Rest Framework (DRF)
  *  URLS:
    http://localhost/api/latest/page=/ (Returns a list of avaialble hotel rooms based on page number)
    http://localhost/api/room/id=/     (Returns a hotel room based on ID)
      

