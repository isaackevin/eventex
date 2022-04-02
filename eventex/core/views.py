from django.views.generic import ListView, DetailView
from eventex.core.models import Speaker, Talk


home = ListView.as_view(template_name='index.html', model=Speaker)

speaker_detail = DetailView.as_view(model=Speaker)

<<<<<<< HEAD
talk_list = ListView.as_view(model=Talk)
=======
def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
        'courses': Course.objects.all(),
    }

    return render(request, 'core/talk_list.html', context)
>>>>>>> parent of 173b946 (course mti)
