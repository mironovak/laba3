from django.shortcuts import render
from django.http import HttpResponse #Этот класс используется для создания HTTP-ответов в Django.

def home(request):
    return render(request, 'blog/home.html')

def blog_settings(request):
    return render(request, 'blog/settings.html')





def set_preferences(request): #функция будет обрабатывать запросы на установку пользовательских настроек
    # Получаем тему и язык из GET-запроса
    #request.GET — это словарь, содержащий параметры, переданные через URL в GET-запросе.
    #Метод .get() извлекает значение по ключу. Если ключ не найден, возвращается значение по умолчанию:
    if request.method == 'POST':
        theme = request.POST.get('theme', 'light')
        language = request.POST.get('language', 'en')
    
    # Создаем ответ
        response = HttpResponse("Preferences set!")
        
    # Устанавливаем cookies для темы и языка
    #set_cookie() добавляет cookie в ответ. Он принимает три аргумента: имя куки, значение и время хранения
        response.set_cookie('theme', theme, max_age=3600*24*30)  # Хранить 30 дней
        response.set_cookie('language', language, max_age=3600*24*30)
        
        return response
    return HttpResponse("Invalid request method")
#Эта функция будет обрабатывать запросы на получение пользовательских настроек.
def get_preferences(request):
    # Получаем значения cookies для темы и языка
    #request.COOKIES — это словарь, содержащий все cookies, отправленные клиентом.
    theme = request.COOKIES.get('theme', 'default theme')
    language = request.COOKIES.get('language', 'default language')
    
    return HttpResponse(f'Current theme: {theme}, Current language: {language}')
#Используем f-строку для форматирования ответа, подставляя значения переменных theme и language.