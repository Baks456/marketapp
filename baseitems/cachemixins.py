from django.core.cache import cache


class CacheMixin():

    def set_or_get_cache(self, querry, cache_name, cache_time):
        data = cache.get(cache_name)
        if data is None:
            data = querry
            cache.set(cache_name, data, cache_time)
        return data
