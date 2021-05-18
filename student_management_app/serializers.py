from rest_framework import serializers
from .models import *  


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'



    
class EventsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Events
        fields = ('id', 'title', 'category', 'featured_image', 'image_url', 'content', 'created_at', 'status')
    def get_image_url(self, Events):
        request = self.context.get('request')
        url = Events.featured_image.url
        return request.build_absolute_uri(url)




class CarousalSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = HeroCarousal
        fields = ( 'id','alt_text', 'carousal_image','image_url','status','caption','url_link' )

    def get_image_url(self, HeroCarousal):
        request = self.context.get('request')
        url = HeroCarousal.carousal_image.url
        return request.build_absolute_uri(url)

            


class FacultyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyMember
        fields = '__all__'
 