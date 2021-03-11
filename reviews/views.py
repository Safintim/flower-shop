from django.views import generic

from reviews.models import Review


class BaseReview:
    model = Review


class ReviewListView(BaseReview, generic.ListView):
    paginate_by = 5


class ReviewCreateView(BaseReview, generic.CreateView):
    fields = ('name', 'phone', 'city', 'social_link', 'text')

