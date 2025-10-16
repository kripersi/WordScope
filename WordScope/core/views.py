from django.shortcuts import render


# Create your views here.
def main(requests):
    return render(requests, 'core/main_page.html')


def about(requests):
    return render(requests, 'core/about.html')
