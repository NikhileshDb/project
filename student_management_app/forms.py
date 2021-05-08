from django import forms 
from django.forms import Form, ModelForm, Textarea, CheckboxInput, TextInput, DateInput, Select, FileInput, URLInput
from student_management_app.models import Courses, SessionYearModel, Notice, Category, Events, HeroCarousal, FacultyMember


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []
    
    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []
    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))



class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []

    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields= '__all__'
        widgets = {
        'title': TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Title ...'}),
        'description': Textarea(attrs={'cols': 30, 'rows': 10, 'class':'form-control', 
        'placeholder': 'Write something about the notice ....'}),
        'created_on': DateInput(attrs={'class':'form-control', 'placeholder': 'Select Date'}),      
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
        }

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
            'created_at': DateInput(attrs={'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
            'featured_image': FileInput(attrs={'class': 'form-control'}),
        }



STATUS = (
    ('Draft',"Draft"),
    ('Publish',"Publish")
)
class AddEventForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))  
    content = forms.CharField(label="Description", max_length=2000, widget=forms.Textarea(attrs={"class":"form-control"}))
    created_at = forms.DateField(label="Date", widget=forms.DateInput(attrs={"class":"form-control"}))
    featured_image = forms.FileField(label="Image", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    status = forms.ChoiceField(label="Status", choices=STATUS, widget=forms.Select(attrs={"class":"form-control"}))
    try:
        categories = Category.objects.all()
        category_list = []
        for category in categories:
            single_category = (category.id, category.title)
            category_list.append(single_category)
    except:
        category_list = []
    
    category = forms.ChoiceField(label="Category", choices=category_list, widget=forms.Select(attrs={"class":"form-control"}))



class HeroCarousalForm(ModelForm):
    class Meta:
        model = HeroCarousal
        fields = '__all__'
        widgets = {
            'alt_text':         TextInput(attrs={'class':'form-control'},),
            'carousal_image':   FileInput(attrs={'class': 'form-control'}),
            'url_link':         URLInput(attrs={'class': 'form-control'}),
            'status':           Select(attrs={'class': 'form-control'}),
            'caption':          TextInput(attrs={'class':'form-control'}),
        }

class FacultyMemberForm(ModelForm):
    class Meta:
        model = FacultyMember
        fields = '__all__'
        widgets = {
            'name' :                  TextInput(attrs={'class':'form-control'}),
            'department' :            TextInput(attrs={'class':'form-control'}),
            'designation' :           TextInput(attrs={'class':'form-control'}), 
            'qualification' :         Textarea(attrs={'class':'form-control'}),
            'experience' :            Textarea(attrs={'class':'form-control'}),
            'awards' :                Textarea(attrs={'class': 'form-control'}),
        }
