from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic

from reviews.forms import ReviewForm
from reviews.models import Review


class BaseReview:
    model = Review

    def get_queryset(self):
        return Review.objects.active()


class ReviewListView(BaseReview, generic.ListView):
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = ReviewForm()
        return context


class ReviewCreateView(generic.FormView):
    form_class = ReviewForm

    def form_valid(self, form):
        form.save()
        messages.info(self.request, 'Ваш отзыв отправлен на модерацию')
        return redirect('review-list')
