from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json

"""
[Home Page] Latest Hotel Rooms Pagination APIView
"""
class PublicLatest(APIView):

    """
    [GET] Returns latest list of hotel room json based on page number
    
    Parameters:
        - page_number: page the user wants to view    
    """
    def get(self, request, page_number):
        
        #NOTE: Database implementation would be done here using 'page_number' parameter.

        dummy_data = sample_data
        
        return JsonResponse(dummy_data, safe=False)

"""
[Home Page] Hotel Room APIView 
"""
class PublicRoom(APIView):

    """
    [GET] Returns hotel room json based on ID
    
    Parameters:
        - ID: a hotel room ID    
    """
    def get(self, request, ID):
        
        #NOTE: Database implementation would be done here using 'ID' parameter.

        dummy_data = sample_data[ID]

        return JsonResponse(dummy_data, safe=False)



class LoginPage(APIView):

    def get(self, request):

        return HttpResponse("You are at the log in view")


sample_data = [{   
                "id": "0",
                "hotelName:": "Best Western",
                "beds": "2",
                "baths": "1",
                "price": "$1000 per night",
                "thumbnail": "pictures/room_0_0.jpg",
                "room_previews": ["pictures/room_0_0.jpg", "pictures/room_0_1.jpg", "pictures/room_0_2.jpg", "pictures/room_0_3.jpg", "pictures/room_0_4.jpg"]
            },
            {   
                "id": "1",
                "hotelName:": "Best Westorn",
                "beds": "2",
                "baths": "1",
                "price": "$1250 per night",
                "thumbnail": "pictures/room_1_2.jpg",
                "room_previews": ["pictures/room_1_2.jpg", "pictures/room_1_1.jpg", "pictures/room_1_0.jpg", "pictures/room_1_3.jpg", "pictures/room_1_4.jpg"]
            },
            {   
                "id": "2",
                "hotelName:": "Best Westorn",
                "beds": "1",
                "baths": "1",
                "price": "$800 per night",
                "thumbnail": "pictures/room_2_3.jpg",
                "room_previews": ["pictures/room_2_3.jpg", "pictures/room_2_1.jpg", "pictures/room_2_2.jpg", "pictures/room_2_0.jpg", "pictures/room_2_4.jpg"]
            },
            {   
                "id": "3",
                "hotelName:": "Best Westorn",
                "beds": "3",
                "baths": "1",
                "price": "$1400 per night",
                "thumbnail": "pictures/room_3_0.jpg",
                "room_previews": ["pictures/room_3_0.jpg", "pictures/room_3_1.jpg", "pictures/room_3_2.jpg", "pictures/room_3_3.jpg", "pictures/room_3_4.jpg"]
            },
            {   
                "id": "4",
                "hotelName:": "Best Western",
                "beds": "1",
                "baths": "1",
                "price": "$800 per night",
                "thumbnail": "pictures/room_4_0.jpg",
                "room_previews": ["pictures/room_4_0.jpg", "pictures/room_3_1.jpg", "pictures/room_3_2.jpg", "pictures/room_3_3.jpg", "pictures/room_3_4.jpg"]
            },
        ]