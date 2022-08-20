from django.shortcuts import render, redirect
from .forms import TagForm, CourseForm, LessonForm
from .models import Tag, Course, Lesson
from django.db.models import Count
# Create your views here.


def course_list(request):
    return render(request, 'course-list.html')



def create_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-course')

    courses = Course.objects.all().annotate(lesson_count=Count('lesson'))
    

    return render(request, 'create-course.html', context = {
        'form': form,
        'courses': courses
    })




def create_lesson(request, pk):
    # course = Course.objects.get(pk=pk)
    lessons = Lesson.objects.filter(course=pk)
    form = LessonForm(initial={'course': pk})
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-lesson', pk=pk)

    return render(request, 'create-lesson.html', context={
        'form': form,
        'lessons': lessons
    })





def create_tag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-tag')
        
    tags =Tag.objects.all()
    
    return render(request, 'create-tag.html', context={
        'form': form,
        'tags': tags
    })