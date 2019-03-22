from django.contrib import admin
from .models import Family, Individual, Member, Network, Orb


class FamilyAdmin(admin.ModelAdmin):
      list_display = ('name', 'description')


class IndividualAdmin(admin.ModelAdmin):
      list_display = ('name', 'description')


class MemberAdmin(admin.ModelAdmin):
      list_display = ('name', 'user_name')


class NetworkAdmin(admin.ModelAdmin):
      list_display = ('title', 'description')


class OrbAdmin(admin.ModelAdmin):
      list_display = ('title', 'description')
    

admin.site.register(Family, FamilyAdmin)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Orb, OrbAdmin)