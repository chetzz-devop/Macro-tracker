from django.shortcuts import render, redirect
from .models import Food, Consumer
from django.views.generic import DeleteView
from django.urls import reverse_lazy


def index(request):
    foods = Food.objects.all()

    if request.method == 'POST':
        # If a logged-out user somehow submits a POST, don't let it crash
        if not request.user.is_authenticated:
            return redirect('index')

        consumed_food_id = request.POST['food']
        food = Food.objects.get(id=consumed_food_id)
        user = request.user
        consume = Consumer(user=user, food_consumed=food)
        consume.save()
        return redirect('index')

    # MANUAL CHECK: If logged in, get their items. If not, give them an empty list.
    if request.user.is_authenticated:
        food_consumed = Consumer.objects.filter(user=request.user)
    else:
        food_consumed = []

    context = {
        'foods': foods,
        'food_consumed': food_consumed
    }

    return render(request, 'myapp/index.html', context)


class DeleteFoodView(DeleteView):
    model = Consumer  # Deletes the log row, NOT the global Food item
    success_url = reverse_lazy('index')
