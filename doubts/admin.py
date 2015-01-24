from django.contrib import admin
from doubts.models import Question, Answer


class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 2

class QuestionAdmin(admin.ModelAdmin):

	# Para organizar el orden en que aparecen en el admin estos campos:
	# fields = ['pub_date','question_text','votes']

	# Para ordenarlos por grupos o fieldsets:
	fieldsets = [
		( None, { 'fields': ['question_text','votes'] } ),
		( 'Date information', { 'fields': ['pub_date'], 'classes': ['collapse'] } ),
	]

	# Para insertar un formulario de creacion de un modelo que es ForeignKey de Question:
	inlines = [AnswerInline]

	# Para mostrar campos del modelo como columnas en la pagina de lista de Questions:
	list_display = ('question_text', 'pub_date', 'votes')

	# Para filtrar por campos del modelo:
	list_filter = ['pub_date']

	# Para buscar por alguno de los campos del modelo:
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
