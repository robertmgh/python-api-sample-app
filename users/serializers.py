from rest_framework import serializers

from .models import User, AccessGroup, AccessMembership

class UserSerializer(serializers.ModelSerializer):
    
   def validate_age(self, value):
       if value < 0:
           raise serializers.ValidationError('Age can not be lower then 0')
       return value
       
   def validate(self, data):
       if data['name'] == data['surname']:
           raise serializers.ValidationError('Name and surname can not be qeual')
       return data
    
   class Meta:
       model = User
       fields = ('id', 'name', 'surname', 'email', 'age', 'admin', 'active_from')
       
class AccessGroupSerializer(serializers.ModelSerializer):
    
   class Meta:
       model = AccessGroup
       fields = ('id', 'name', 'description')
       
class AccessMembershipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AccessMembership
        fields = ('id', 'access_group', 'user', 'inviter', 'invite_data')
