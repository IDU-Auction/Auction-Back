from apps.about.models import About


def page_data(request):

    context = {
        'about': About.objects.first(),
    }

    return context
