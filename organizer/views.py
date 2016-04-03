from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.views.generic import View

from .models import Startup, Tag

def homepage(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': tag_list})
#    tag_list = Tag.objects.all()
#    template = loader.get_template('organizer/tag_list.html')
#    context = RequestContext(request, {'tag_list': tag_list})
#    output = template.render(context)
#    return HttpResponse(output)

#    return render_to_response('organizer/tag_list.html', {'tag_list': Tag.objects.all()})
def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup': startup})

def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})
#    tag = get_object_or_404(Tag, slug__iexact=slug)
#    template = loader.get_template('organizer/tag_detail.html')
#    context = RequestContext(request, {'tag': tag})
#    return HttpResponse(template.render(context))

#    return render_to_response('organizer/tag_detail.html', {'tag': tag})

def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})