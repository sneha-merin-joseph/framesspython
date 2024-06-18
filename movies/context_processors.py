from .models import *


def get_all_childrens(querysets):
    child_lists = []
    for queryset in querysets:
        childrens = get_childrens(queryset)
        child_lists.append(childrens)
    return child_lists

def get_childrens(queryset):
    append_dictionary = {
        "id" : str(queryset.id),
        "name": queryset.name
    }
    append_dictionary["children"] = get_inner_childern(queryset)
    return append_dictionary

def get_inner_childern(inner_queryset):
    queryset_data = []
    querysets = Category.objects.filter(parent_id=inner_queryset)
    for queryset in querysets:
        append_dictionary = {
        "id" : str(queryset.id),
        "name": queryset.name
        }
        append_dictionary["children"] = get_inner_childern(queryset)
        queryset_data.append(append_dictionary)
    return queryset_data

def categories(request):
    category_querysets =Category.objects.prefetch_related('category_parent').filter(parent_id=None,is_active=True)
    category_querysets = get_all_childrens(category_querysets)
    return{
        'categories':category_querysets,  
    }