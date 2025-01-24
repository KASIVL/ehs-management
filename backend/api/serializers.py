from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Appuser, Area, Building, College, Collegedepartment, Department, Departmentbuilding, Focus, Hazard, Lab, Labbiosafetyofficer, Labfocushazard, Labsafetyofficer, Notification, Overdue, Person, Personemail, Room, Userbuilding, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class AppuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appuser
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Area
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class CollegedepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collegedepartment
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentbuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departmentbuilding
        fields = '__all__'

class FocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Focus
        fields = '__all__'

class HazardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hazard 
        fields= '__all__'

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'

class LabbiosafetyofficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labbiosafetyofficer
        fields = '__all__'

class LabfocushazardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labfocushazard
        fields = '__all__'

class LabsafetyofficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labbiosafetyofficer
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class OverdueSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Overdue
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonemailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personemail
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserbuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userbuilding
        fields = '__all__'