from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic

from reviews.forms import ReviewCreateForm
from reviews.models import Review


class ReviewListView(generic.ListView):
    model = Review
    paginate_by = 5

    def get_queryset(self):
        return Review.objects.active()

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['form'] = ReviewCreateForm()
        return super().get_context_data(object_list=object_list, **kwargs)


class ReviewCreateView(generic.FormView):
    form_class = ReviewCreateForm

    def form_valid(self, form):
        form.save()
        messages.info(self.request, 'Ваш отзыв отправлен на модерацию')
        return redirect('review-list')

