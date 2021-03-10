from main.models import Category


def categories(request):
    return {
        'categories': Category.objects.active().parent_null()
    }
