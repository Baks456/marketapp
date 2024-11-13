from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) < 10:
        return Products.objects.filter(id=int(query))

    vector = SearchVector('name', 'description')
    que = SearchQuery(query)

    result = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0.01).order_by("-rank")
    result = result.annotate(
        headline=SearchHeadline('name', que, start_sel='<span style="background-color:yellow;">', stop_sel='</span>'), )
    result = result.annotate(
        bodyline=SearchHeadline('description', que, start_sel='<span style="background-color:yellow;">',
                                stop_sel='</span>'), )
    return result

    # keywords = [i for i in query.split() if len(i)>2]
    # q_obj = Q()
    #
    # for key in keywords:
    #     q_obj |= Q(description__icontains=key)
    #     q_obj |= Q(name__icontains=key)
    #
    # return Products.objects.filter(q_obj)
