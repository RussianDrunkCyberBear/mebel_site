from django.shortcuts import render
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def contacts(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			sender_name = form.cleaned_data['sender_name']
			sender_email = form.cleaned_data['sender_email']
			sender_phonenum = form.cleaned_data['sender_phonenum']
			message = form.cleaned_data['message']
			subject = 'Сообщение от: ' + sender_email + ' (обратная связь dommebel-citi)'
			message = 'Сообшение отправлено через форму обратной связи сайта dommebel-citi.ru. \n\nОтправитель:\nemail: ' + sender_email + '\nИмя: ' + sender_name + '\nтел.:' + sender_phonenum + '\n\n' + 'Сообщение:\n' + message 

			recipients = ['nigerukompa@gmail.com'] # заменить info@dommebel-citi.ru

			try:
				send_mail(subject, message, 'noreply@dommebel-citi.ru', recipients, fail_silently=False)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			messages.success(request, "Ваше сообщение успешно отправлено!")
			return HttpResponseRedirect('contacts.html') #render(request, 'contacts.html')
	else:
		#Заполняем форму
		form = FeedbackForm()
	return render(request, 'contacts.html', {'form': form})

class FeedbackForm(forms.Form):
	sender_name = forms.CharField(max_length = 100, required = False, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
	sender_email = forms.EmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'your@email.com'}))
	sender_phonenum = forms.RegexField(regex=r'^\+?1?\d{10,13}$', required = False, widget=forms.TextInput(attrs={'placeholder': '+79997775588'}))
	# subject = forms.CharField(max_length = 100)
	message = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Ваше сообщение'}))

class CallbackRequest(forms.Form):
	pass




# def contactView():
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
# 		if form.is_valid():
# 			subject = form.cleaned_data['subject']
# 			sender = form.cleaned_data['sender']
# 			message = form.cleaned_data['message']
# 			copy = form.cleaned_data['copy']

# 			recipients = ['ВАШ_EMAIL_ДЛЯ_ПОЛУЧЕНИЯ_СООБЩЕНИЯ']
# 			#Если пользователь захотел получить копию себе, добавляем его в список получателей
# 			if copy:
# 				recipients.append(sender)
# 			try:
# 				send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
# 			except BadHeaderError: #Защита от уязвимости
# 				return HttpResponse('Invalid header found')
# 			#Переходим на другую страницу, если сообщение отправлено
# 			return render(request, 'site/thanks.html')
# 	else:
# 		#Заполняем форму
# 		form = ContactForm()
# 	#Отправляем форму на страницу
# 	return render(request, 'contacts.html', {'form': form})