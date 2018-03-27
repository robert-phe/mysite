from adminsortable.admin import SortableStackedInline, SortableAdmin
from django.contrib import admin
from django.forms import CharField, ModelForm

from myapp.models import Test, Page, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    show_change_link = True


class PageInline(SortableStackedInline):
    model = Page
    extra = 0
    show_change_link = True
    verbose_name = 'Page'

    def get_queryset(self, request):
        """Alter the queryset to return no existing entries"""
        # get the existing query set, then empty it.
        qs = super(PageInline, self).get_queryset(request)
        for q in qs:
            q
        return qs




    # def get_formset(self, request, obj=None, **kwargs):
#     extra_fields = {'my_field': CharField()}
#     kwargs['form'] = type('ProgressForm', (ModelForm,), extra_fields)
#     return super(PageInline, self).get_formset(request, obj, **kwargs)


@admin.register(Test)
class TestAdmin(SortableAdmin):
    fields = ('test_name', 'description')
    list_display = ('test_name', 'description', 'nr_of_pages',)
    ordering = ('test_name',)
    inlines = [PageInline]

    def nr_of_pages(self, obj):
        return Page.objects.filter(test=obj.id).count()


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    exclude = ('test',)
    list_display = ('name', 'nr_of_questions')
    ordering = ('test', 'position',)
    inlines = [QuestionInline]

    def nr_of_questions(self, obj):
        return Question.objects.filter(page=obj.id).count()

    def name(self, obj):
        for i, page in enumerate(Page.objects.filter(test_id=obj.test_id)):
            if page.id == obj.id:
                return '{} - Page {}'.format(obj.test, i + 1)

    # def has_add_permission(self, request):
    #     return False

    # def get_form(self, request, obj=None, **kwargs):
    #     if obj:  # obj is not None, so this is a change page
    #         kwargs['exclude'] = ['test', 'position', ]
    #     else:  # obj is None, so this is an add page
    #         kwargs['exclude'] = ['position', ]
    #     return super(PageAdmin, self).get_form(request, obj, **kwargs)
    #
    # def save_model(self, request, obj, form, change):
    #     #TODO: ? Add position with last index if add new page
    #     super().save_model(request, obj, form, change)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    exclude = ('page',)
    list_display = ('question', 'belongs', 'nr_of_choices',)
    ordering = ('question',)
    inlines = [ChoiceInline]

    def nr_of_choices(self, obj):
        return Choice.objects.filter(question=obj.id).count()

    def belongs(self, obj):
        page = Page.objects.filter(id=obj.page_id)[0]
        return str(page.test) + '/Page{}'.format(page.position)
