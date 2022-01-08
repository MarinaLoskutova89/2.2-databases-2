from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Scopes, Article


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        n = 0
        for form in self.forms:
            for key, val in form.cleaned_data.items():
                if key == 'is_main' and val is True:
                    n += 1
                    if n > 1:
                        raise ValidationError('Основным может быть только одни раздел')
        if n == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopesInline(admin.TabularInline):
    model = Scopes
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopesInline]

