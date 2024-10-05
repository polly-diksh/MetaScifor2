from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def home(request):
	return render(request, 'home.html')

# PLAYER FORM STUFF

def add_player(request):
	team = Team.objects.all()

	if request.method == 'POST':
		form = PlayerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return redirect('details')
	else:
		form = PlayerForm()

	context = {
		"form": form,
		"team": team,
	}

	return render(request, "add_player.html", context)

def player_details(request):
	players = Player.objects.all()

	context = {
		"players": players
	}

	return render(request, "details.html", context)

def player_detail(request):
	player = Player.object.get(pk = pk)

	context = {
		"player": player
	}

	return render(request, "player_detail.html", context)


# FORM CREATION FUNCTIONS
def create_form(request):
	if request.method == 'POST':
		# CreateForm is FormForm in the project
		create_form  = CreateForm(request.POST)
		if create_form.is_valid():
			created_form_instance = create_form.save()
			return redirect("add_questions", form_id = created_form_instance.id)
	else:
		create_form = CreateForm()

	context = {
		"create_form": create_form,
	}

	return render(request, "create_form.html", context)

def add_questions(request, form_id):
	created_form_instance = get_object_or_404(Form, id = form_id)

	if request.method == 'POST':
		question_text =request.POST.get('question_text')
		question_type = request.POST.get("question_type")
		choices = request.POST.get('options')

		question = Question.objects.create(
			form = created_form_instance,
			question_text = question_text,
			question_type = question_type
			)

		if question_type in ['multiple_choice', 'checkbox', 'dropdown']:
			choice_list = choices.split(",")
			for choice_text in choice_list:
				Multiple_choice.objects.create(question = question, choice_text = choice_text.strip())

		return redirect("add_questions", form_id = created_form_instance.id)

	questions = created_form_instance.questions.all()

	context = {
	"created_form_instance": created_form_instance,
	"questions": questions,
	}
	return render(request, "add_questions.html", context)

def list_forms(request):
	forms = Form.objects.filter(IsDelete = False)
	context = {'forms': forms}
	return render(request, 'list_forms.html', context)

def form_detail(request, form_id):
	form_instance = get_object_or_404(Form, id = form_id)
	responses = Response.objects.filter(form=form_instance).order_by('-created_at')

	if request.method == 'POST' and 'edit_response_id' in request.POST:
		response_id = request.POST.get('edit_response_id')
		return redirect('edit_response', response_id = response_id)

	context = {
		"form_instance" : form_instance,
		"responses": responses,
	}

	return render(request, 'form_detail.html', context)

def form_detail(request, form_id):
    form_instance = get_object_or_404(Form, id=form_id)
    questions = form_instance.questions.all()
    return render(request, 'form_detail.html', {'form_instance': form_instance, 'questions': questions})

def delete_form(request, form_id):
	form = get_object_or_404(Form, id = form_id)
	form.IsDelete = True
	form.save()
	# form.delete()
	return redirect("list_forms")

def recycle_data(request):
	forms = Form.objects.filter(IsDelete=True)
	context = {
		"forms": forms,
	}

	return render(request, "recycle.html", context)

def restore_data(request, form_id):
	form_instance = get_object_or_404(Form, id = form_id)
	form_instance.IsDelete = False
	form_instance.save()
	return redirect('list_forms')

def delete_data(request,form_id):
	form = get_object_or_404(Form, id = form_id)
	form.delete()
	return redirect('recycle')


