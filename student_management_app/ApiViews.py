from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . HodViews import *
from . serializers import CoursesSerializer, NoticeSerializer, EventsSerializer, CarousalSerializer, FacultyMemberSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'cource_list':               'cource_list/',
        'cource_list_item':          'cource_list/<str:item_id>',
        'notice_list':               'notice_list/',
        'notice_list-item':          'notice_list/<str:item_id>',
        'event_list':                'event_list/',
        'event_list_item':           'event_list/<str:item_id>',
        'carousal_list':             'carousal_list/',
        'carousal_list_item':        'carousal_list/<str:item_id>',
        'faculty_member_list':       'faculty_member/',
        'faculty_member_list-item':  'faculty_member/<str:item_id>',
    }

    return Response(api_urls)

@api_view(['GET'])
def cource_list(request):
    cources = Courses.objects.all()
    serializer = CoursesSerializer(cources, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cource_list_item(request, item_id):
    courceitem = Courses.objects.get(pk=item_id)
    serializer = CoursesSerializer(courceitem, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def notice_list(request):
    noitces = Notice.objects.all()
    serializer = NoticeSerializer(noitces, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def notice_list_item(request, item_id):
    noticeitem = Notice.objects.get(pk=item_id)
    serializer = NoticeSerializer(noticeitem, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def event_list(request):
    events = Events.objects.all()
    serializer = EventsSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def event_list_item(request, item_id):
    event = Events.objects.get(pk=item_id)
    serializer = EventsSerializer(event, many=False)
    return Response(serializer.data)
    
@api_view(['GET'])
def carousal_list(request):
    carousal = HeroCarousal.objects.all()
    serializer = CarousalSerializer(carousal, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def carousal_list_item(request, item_id):
    carousal_item = HeroCarousal.objects.get(pk=item_id)
    serializer = CarousalSerializer(carousal_item, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def faculty_member_list(request):
    member = FacultyMember.objects.all()
    serializer = FacultyMemberSerializer(member, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def faculty_member_list_item(request, item_id):
    member = FacultyMember.objects.get(pk=item_id)
    serializer = FacultyMemberSerializer(member, many=False)
    return Response(serializer.data)