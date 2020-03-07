from django.contrib import admin
from apps.products.models.product import Product
from apps.products.models.images import Image
from apps.products.models.option import Option
from apps.products.models.option_value import OptionValue
from apps.products.forms.images_form import ImageForm
from apps.products.forms.option_form import OptionForm
from apps.products.forms.option_value_form import OptionValueForm
import nested_admin


class ImagesInline(nested_admin.NestedTabularInline):
    """this inline class is used in Products for showing related images directly."""

    model = Image
    form = ImageForm
    fields = ('position', 'src')
    # readonly_fields = ( )
    show_add_link = True
    # inlines = []
    extra = 1



class OptionValueInline(nested_admin.NestedTabularInline):
    """this inline class is used in Products for showing related options directly."""

    model = OptionValue
    form = OptionValueForm
    fields = ('name',)
    # readonly_fields = ( )
    show_add_link = True
    # inlines = []
    extra = 0


class OptionInline(nested_admin.NestedTabularInline):
    """this inline class is used in Products for showing related options directly."""

    model = Option
    form = OptionForm
    fields = ('option_name', 'position')
    # readonly_fields = ( )
    show_add_link = True
    inlines = [OptionValueInline]
    extra = 1














# Register your models here.
@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    """Registering PRoduct in admin."""

    model = Product
    inlines = [ImagesInline, OptionInline]

