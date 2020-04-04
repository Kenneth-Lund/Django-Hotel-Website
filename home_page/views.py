from django.shortcuts import render
from django.http import HttpResponse
import requests

 
"""
Main view for the homepage of this website.
    
    STEPS
    - 1. Request list of latest hotel rooms for first page
    - 2. Extract first room's preview images
    - 3. Render the template with extracted response data
"""
def main(request):
    
    # API Call fetches a list of rooms based on page number
    response_data = requests.get("http://127.0.0.1:8000/api/latest/page=1/")
    
    dummy_hotel_data = response_data.json()

    initial_preview_list = dummy_hotel_data[0].get('room_previews')

    context = { 'room_data': dummy_hotel_data, 'preview_list': initial_preview_list }

    return render(request, "home_page/body.html", context)

"""
Hotel Room Preview List (AJAX View)
    
    This view responds to an AJAX function call in order to update the rendered HTML.

    STEPS
    - 1. Request a hotel room data based on ID
    - 2. Extract hotel room's preview images
    - 3. Update the previewTable.html template within the body.html template
"""
def update_preview_list(request, ID):

    # API Call fetches a single room based on ID
    response_data = requests.get("http://127.0.0.1:8000/api/room/id=" + str(ID) + "/")

    dummy_room_data = response_data.json()
    
    room_preview_list =  dummy_room_data.get('room_previews')

    context = { 'preview_list': room_preview_list }

    return render(request, "home_page/previewTable.html", context)

#NOTE: To be implemented
def login(request):
    return HttpResponse("You are at the login page view.")