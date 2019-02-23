from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.utils.crypto import get_random_string

from . import forms
from . import models

def index(request):
    form = forms.ShortURLForm()
    ctx = {'form': form}
    return render(request, 'skurcz_to/index.html', ctx)

def shorten_long_url(request):
    """
    Check if url acquired from POST already exist in the db, and fetch it's short code,
    otherwise create random string and for url, and save in db for future use.
    """
    if request.method == 'POST':
        # TODO: cache lookup
        try:
            short_url = models.ShortURL.objects.get(full_url=request.POST['full_url'])
            short_id = short_url.code
        except models.ShortURL.DoesNotExist:
            form = forms.ShortURLForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['full_url']

                short = form.save(commit=False)
                # generate short code if not in db already
                short_id = get_random_string(length=5)
                short.code = short_id
                short.save()

        url = "{}://{}/{}".format(request.scheme, request.get_host(), short_id)
        return JsonResponse({'success': True, 'short_url': url})

    return JsonResponse({'error':'Error'})


def obtain_long_url(request, code):
    """
    Redirects url with code to the original url
    """
    short = get_object_or_404(models.ShortURL, code=code)
    return redirect(short.full_url, permanent=True)
