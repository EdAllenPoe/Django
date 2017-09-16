# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,HttpResponse

def index(request):
    # return HttpResponse ("Hello World")
    return render(request, 'session_words\index.html')

# def display_result(request):
#     return render(request, 'surveys/results.html')
#
# def process_form(request):
    # try:
    #     request.session['tries']
    # except KeyError:
        # request.session['tries'] = 0
    # request.session['color'] = request.POST['color']
    # request.session['location'] = request.POST['location']
    # request.session['language'] = request.POST['language']
    # request.session['comment'] = request.POST['comment']
    # request.session['tries'] += 1

    # print color
    # return redirect('/result')

def add_word(request):
    word=request.POST['theword']
    print word

    request.session['name']=request.POST['theword']
    # new_word = {}
    # for key, value in request.POST.iteritems():
    #     if key != "csrfmiddlewaretoken" and key != "show-big":
    #         new_word[key] = value
    #     if key == "show-big":
    #         new_word['big'] = "big"
    #     else:
    #         new_word['big'] = ""
    # new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    # try:
    #     request.session['words']
    # except KeyError:
    #     request.session['words'] = []
    #
    # temp_list = request.session['words']
    # temp_list.append(new_word)
    # request.session['words'] = temp_list
    # for key, val in request.session.__dict__.iteritems():
    #     print key, val
    # print "past created at", new_word

    return redirect('\show.html')

# def clear(request):
#     for key in request.session.keys():
#         del request.session[key]



    return redirect('/')
