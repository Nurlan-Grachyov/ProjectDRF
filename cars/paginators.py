from rest_framework.pagination import PageNumberPagination


class MotoPaginator(PageNumberPagination):
    page_size = 2