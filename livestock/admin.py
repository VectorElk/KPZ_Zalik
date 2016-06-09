from django.contrib import admin
from livestock.models import *
# Register your models here.


class RespondentSearch(admin.ModelAdmin):
    list_display = ('name', 'business_adress', 'actual_adress')
    search_fields = ('name', 'business_adress', 'actual_adress')
    list_filter = ('name', 'business_adress', 'actual_adress')

admin.site.register(Respondent, RespondentSearch)


class LivestockProductionSearch(admin.ModelAdmin):
    list_display = ('name', 'unit', 'amount', 'id')
    search_fields = ('name', 'unit', 'id__name')
    list_filter = ('name', 'unit')

admin.site.register(LivestockProduction, LivestockProductionSearch)


class CattleAndPoultrySearch(admin.ModelAdmin):
    list_display = ('name', 'cattle', 'pigs', 'sheep_goat', 'horses', 'poultr', 'id')
    search_fields = ('name', 'cattle', 'pigs', 'sheep_goat', 'horses', 'poultr', 'id__name')
    list_filter = ('name', 'id')

admin.site.register(CattleAndPoultry, CattleAndPoultrySearch)


class PoultrySearch(admin.ModelAdmin):
    list_display = ('name', 'adult', 'young', 'cattle_and_poultry_id')
    search_fields = ('name', 'cattle_and_poultry_id__name')
    list_filter = ('name', 'cattle_and_poultry_id')

admin.site.register(Poultry, PoultrySearch)
