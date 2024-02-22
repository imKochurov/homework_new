from django.shortcuts import render, redirect, get_object_or_404
from first_app.forms import CallOrderForm, NoteForm
from django.utils import timezone
from first_app.models import Delivery, Notes, AuthUser

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from django.http import HttpResponse

# def first_view(request):
#     return HttpResponse('Hello, world!')


def home(request):
    return render(request, 'main.html')


def order_call(request):
    if request.method == 'POST':
        form = CallOrderForm(request.POST)
        if form.is_valid():
            call_order = form.save(commit=False)
            call_order.order_date = timezone.now() # додаю поточний час
            call_order.completed_status = False # додаю статус необробленого вхідного запиту
            call_order.save() # запис до бази даних
            user_name = form.cleaned_data['user_name'] # отримую в скрипт потрібне значення з форми
            request.session['user_name'] = user_name # зберігаю дані в сесії для передачі у відображення про успішне заповнення форми
            return redirect('success') # перенаправляю на відображення про успішне заповнення
        else:
            print(form.errors)
    else:
        form = CallOrderForm()
    return render(request, 'order_call.html', {'form': form})


def success(request):
    user_name = request.session.get('user_name') # отримую з сесії, з попереднього відображення, ім'я користувача
    return render(request, 'success.html', {'user_name': user_name})


def tracker(request):
    parcel_data = None
    error_message = None

    if request.method == 'POST':
        parcel_id = request.POST.get('parcel_id', None)
        if parcel_id:
            try:
                parcel_data = Delivery.objects.get(parcel_id=parcel_id)
            except Delivery.DoesNotExist:
                error_message = 'Посилка з введеним трек-номером не знайдена'

    return render(request, 'tracker.html', {'parcel_data': parcel_data, 'error_message': error_message})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user.id
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'note_create.html', {'form': form})


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Notes, pk=pk, user=request.user.id)
    return render(request, 'note_detail.html', {'note': note})

@login_required
def note_list(request):
    notes = Notes.objects.filter(user=request.user.id)
    return render(request, 'note_list.html', {'notes': notes})


@login_required
def note_edit(request, pk):
    note = get_object_or_404(Notes, pk=pk, user=request.user.id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html', {'form': form})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk, user=request.user.id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_delete.html', {'note': note})