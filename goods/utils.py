from goods.models import Products
from django.db.models import Q


def q_search(query):
    if query.isdigit() and len(query) < 10:
        return Products.objects.filter(id=int(query))

    keywords = [i for i in query.split() if len(i)>2]
    q_obj = Q()

    for key in keywords:
        q_obj |= Q(description__icontains=key)
        q_obj |= Q(name__icontains=key)

    return Products.objects.filter(q_obj)