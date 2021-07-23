from django.shortcuts import render

GroceryItem = [
    {
        'text': 'apples',
        'created': '07/24/21',
        'completed': False,
    },
    {
        'text': 'bananas',
        'created': '07/25/21',
        'completed': False,
    }
]

def index(request):
    context = {
        'GroceryItem': GroceryItem
    }
    return render(request, 'grocery_list/index.html', context)

# def addItem(request):
#     return HttpResponse('<h1>Add Items</h1>')

# def completeItem(request):
#     return HttpResponse('<h1>Complete Items</h1>')

# def deleteItem(request):
#     return HttpResponse('<h1>Delete Items</h1>')

