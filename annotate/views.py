# -*- coding: utf-8 -*-

# Django built-in
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login # for user login

# Custom module
from annotate.models import Annotation
from annotate.forms import UserForm, AnnotationForm


"""
    Class Based View: https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/
    Working with Form: https://docs.djangoproject.com/en/dev/topics/forms/
"""
class UserView(View):


    form_class = UserForm
    template_name = "user.html"

    # if UserView use UserForm, is get better use UserForm?
    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        user = authenticate(username=email)
        form = self.form_class(request.POST)
        print('method post')
        print(email)
        print(user)
        print(form)
        if user is not None:
            if user.is_active: # user is valid
                login(request, user)
                print('user is valid')
                if form.is_valid():

                    # Handling Session
                    # https://docs.djangoproject.com/en/dev/topics/http/sessions/
                    if 'nickname' in dict(request.POST):
                        request.session['nickname'] = dict(request.POST)['nickname']
                        print request.session['nickname']
                    if 'email' in dict(request.POST):
                        request.session['email'] = dict(request.POST)['email']
                        print request.session['email']

                    print('form is valid')

                    return HttpResponseRedirect(reverse('process')) # user is valid, redirect to process page
            
                else: # user is not valid
                    print('user is not valid')
                    return render(request, self.template_name, {'form': form}) # return with form error
        return render(request, self.template_name, {'wrong_email': 'wrong-email'})

        


class AnnotationView(View):

    
    form_class = AnnotationForm
    template_name = "annotate.html"
    nickname = ''
    email = ''

    def get(self, request, *args, **kwargs):
        self.nickname = request.session['nickname'][0]
        self.email = request.session['email'][0]

        all_entries = Annotation.objects.all()
        return render(request, self.template_name, {'nickname': self.nickname,
                                                    'email': self.email,
                                                    'all': all_entries})

    def post(self, request, *args, **kwargs):
        print('method post')
        print(request.session)
        print(request.session['nickname'])
        print(request.session['nickname'][0])
        print(request.POST)
        self.nickname = request.session['nickname'][0]
        self.email = request.session['email'][0]

        self.comment_type = request.POST['comment_type']
        print(self.email)
        print(self.comment_type)

        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()

        return render(request, self.template_name, {'nickname': self.nickname,
                                                    'email': self.email,
                                                    'comment_type': self.comment_type})

