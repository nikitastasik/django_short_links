from django.shortcuts import get_object_or_404
from django.shortcuts import render
import random, string, json
from short_link.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect

LENGTH = 6


@csrf_protect
def create_short_link(request):
    return render(request, 'short_link/index.html', {})


def redirect_original(request, short_url_id):
    url = get_object_or_404(Urls, pk=short_url_id)
    url.transition_count += 1
    url.save()
    return HttpResponseRedirect(url.long_url)


def short_link(request):
    url_from_request = request.POST.get("url", "Undefined")
    if url_from_request:
        short_id = get_short_code(LENGTH)
        url = Urls(long_url=url_from_request, short_url_id=short_id)
        url.save()
        resp_url = {'url': "http://127.0.0.1:8000" + "/" + short_id}
        return HttpResponse(json.dumps(resp_url),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")


def get_short_code(length):
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(char) for _ in range(length))
