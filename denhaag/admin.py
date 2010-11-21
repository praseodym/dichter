from dichter.denhaag.models import *
from django.contrib import admin

class CampaignAdmin(admin.ModelAdmin):
  list_display = ('title', 'start_date', 'end_date')
  search_fields = ('title',)
  ordering = ('title',)
admin.site.register(Campaign, CampaignAdmin)

class PoliticianAdmin(admin.ModelAdmin):
  list_display = ('name', 'party')
  search_fields = ('name', 'party')
  ordering = ('name', 'party')
admin.site.register(Politician, PoliticianAdmin)
  
class PartyAdmin(admin.ModelAdmin):
  list_display = ('name',)
admin.site.register(Party, PartyAdmin)

class ContactMethodAdmin(admin.ModelAdmin):
  list_display = ('name','enabled')
admin.site.register(ContactMethod, ContactMethodAdmin)

admin.site.register(CampaignContact)
admin.site.register(PoliticianCampaign)

class PoliticianContactInfoAdmin(admin.ModelAdmin):
  list_display = ('politician', 'address', 'contact_method')
admin.site.register(PoliticianContactInfo, PoliticianContactInfoAdmin)
admin.site.register(Action)
admin.site.register(Response)
admin.site.register(Static)


