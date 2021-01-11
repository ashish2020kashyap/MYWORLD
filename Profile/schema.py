import graphene
from graphene import Argument
from graphene_django import DjangoObjectType
from authentication.models import Profile



class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = '__all__'

class Query(graphene.ObjectType):

    all_profile= graphene.List(ProfileType)

    def resolve_all_profile(root, info):
        return Profile.objects.all()



schema = graphene.Schema(query=Query)