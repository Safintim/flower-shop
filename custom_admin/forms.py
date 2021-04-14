from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Row, Fieldset, Column
from django import forms

from main.models import Product, Category, Reason, BouquetFlower, Color


def get_link(css_class, action, text):
    return f'<a class="btn btn-{css_class} mr-2" href="{action}">{text}</a>' if action else ''


def get_submit(is_update):
    if is_update:
        return '<input type="submit" name="save" value="Сохранить" class="btn btn-primary mr-2" id="submit-id-save">'
    return ''


class CreateUpdateFormHelper(FormHelper):
    def __init__(self, delete_action=None, is_update=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'POST'
        delete_link = get_link(css_class='danger', action=delete_action, text='Удалить')
        list_input = get_submit(is_update)
        self.layout = Layout(
            *self.layout.fields,
            Submit('continue', 'Сохранить и продолжить редактирование'),
            HTML(list_input),
            HTML(delete_link)
        )


class ProductFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.base_info_layout = Fieldset(
            'Основная информация',
            Row(Column('title')),
            Row(Column('small_image'), Column('big_image'))
        )
        discount_column = Column('discount')
        self.price_present_info_layout = Fieldset(
            'Ценообразование',
            Row(Column('price'), discount_column)
        )
        self.price_bouquet_info_layout = Fieldset(
            'Ценообразование',
            Row(discount_column)
        )
        common_filters = [
            Column('is_active', 'is_hit', 'is_new'),
            Column('reasons'),
            Column('categories')
        ]
        self.filters_present_layout = Fieldset(
            'Фильтры',
            Row(*common_filters)
        )
        self.filters_bouquet_layout = Fieldset(
            'Фильтры',
            Row(*common_filters, Column('color'))
        )
        self.button_layout = Row(
            Submit('save', 'Сохранить', css_class='btn-lg'),
            css_class='justify-content-center'
        )


class PresentFormHelper(ProductFormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            self.base_info_layout,
            self.price_present_info_layout,
            self.filters_present_layout,
            self.button_layout
        )


class BouquetFormHelper(ProductFormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            self.base_info_layout,
            self.price_bouquet_info_layout,
            self.filters_bouquet_layout,
            self.button_layout
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

    color = forms.ModelMultipleChoiceField(
        label='Цвет',
        queryset=Color.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    TYPE = None

    class Meta:
        model = Product
        fields = (
            'title',
            'small_image',
            'big_image',
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

            if obj.type == Product.Type.PRESENT:
                obj.categories.add(Category.objects.filter(title='Подарки').first())

        return obj


class ProductPresentForm(ProductForm):
    TYPE = Product.Type.PRESENT

    class Meta(ProductForm.Meta):
        fields = ProductForm.Meta.fields + ('price',)

    @property
    def helper(self):
        return PresentFormHelper()


class ProductBouquetForm(ProductForm):
    Meta = ProductForm.Meta
    TYPE = Product.Type.BOUQUET

    class Meta(ProductForm.Meta):
        fields = ProductForm.Meta.fields + ('color',)

    @property
    def helper(self):
        return BouquetFormHelper()
