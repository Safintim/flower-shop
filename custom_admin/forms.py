from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Row, Fieldset, Column
from django import forms
from django.forms import inlineformset_factory

from main.models import Product, Category, Reason, Bouquet, BouquetFlower


class CreateUpdateFormHelper(FormHelper):
    def __init__(self, delete_action=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'POST'
        html = f'<a class="btn btn-danger" href="{delete_action}">Удалить</a>' if delete_action else ''
        self.layout = Layout(
            *self.layout.fields,
            Submit('save', 'Сохранить'),
            HTML(html)
        )


class ProductFormHelper(FormHelper):
    form_method = 'POST'
    base_info_layout = Fieldset(
        'Основная информация',
        Row(
            Column('title'),
            Column('slug'),
        ),
        Row(
            Column('small_image'),
            Column('big_image'),
        ),
    )
    price_info_layout = Fieldset(
        'Ценообразование',
        Row(
            Column('price'),
            Column('discount'),
        ),
    )
    filters_layout = Fieldset(
        'Фильтры',
        Row(
            Column(
                'is_active',
                'is_hit',
                'is_new'
            ),
            Column('reasons'),
            Column('categories', ),
        ),
    )
    button_layout = Row(Submit('save', 'Сохранить', css_class='btn-lg'), css_class='justify-content-center')
    layout = Layout(
        base_info_layout,
        price_info_layout,
        filters_layout,
        button_layout
    )


class ProductForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        label='Категории',
        initial=Category.objects.filter(title='Подарки').first(),
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    reasons = forms.ModelMultipleChoiceField(
        label='Поводы',
        queryset=Reason.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    TYPE = None

    class Meta:
        model = Product
        fields = (
            'title',
            'slug',
            'small_image',
            'big_image',
            'price',
            'discount',
            'is_active',
            'is_new',
            'is_hit',
            'categories',
            'reasons',
        )

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.type = self.TYPE
        if commit:
            obj.save()
            self.save_m2m()
        return obj


class ProductPresentForm(ProductForm):
    Meta = ProductForm.Meta
    TYPE = Product.Type.PRESENT

    @property
    def helper(self):
        return ProductFormHelper()


class ProductBouquetForm(ProductForm):
    Meta = ProductForm.Meta
    TYPE = Product.Type.BOUQUET

    @property
    def helper(self):
        return ProductFormHelper()


class BouquetFlowerForm(forms.ModelForm):
    class Meta:
        model = BouquetFlower
        exclude = ('id',)

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.disable_csrf = True
        helper.layout = Layout(
            Row(
                Column('count', css_class='col-2'),
                Column('flower', css_class='col-8'),
                Column('DELETE', css_class='col-8'),
                css_class='justify-content-center'
            ),
        )
        return helper


# TODO удалить все ниже
BouquetFlowerFormSet = inlineformset_factory(
    Bouquet,
    BouquetFlower,
    form=BouquetFlowerForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
)

BouquetFlowerMiddleFormSet = inlineformset_factory(
    Bouquet,
    BouquetFlower,
    form=BouquetFlowerForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
)
