from django.contrib import admin
from apps.products.models.product import Product
from apps.products.models.images import Image
from apps.products.models.option import Option
from apps.products.models.option_value import OptionValue
from apps.products.models.tags import Tag
from apps.products.models.variant import Variant
from apps.products.forms.images_form import ImageForm
from apps.products.forms.option_form import OptionForm
from apps.products.forms.option_value_form import OptionValueForm
from apps.products.forms.tag_form import TagForm
from apps.products.forms.variant_form import VariantForm
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


class TagInline(nested_admin.NestedTabularInline):
    """this inline class is used in Products for showing tags."""

    model = Tag
    form = TagForm
    fields = ('name',)
    # readonly_fields = ( )
    show_add_link = True
    # inlines = []
    extra = 1


class VariantInline(nested_admin.NestedStackedInline):
    """this inline class is used in Products for showing Variant."""

    model = Variant
    form = VariantForm
    fields = ('title', 'price', 'sku', 'position', 'compare_at_price',
        	  'option1', 'option2', 'option3', 'taxable', 'barcode',
        	  'weight', 'weight_unit', 'image', 'inventory_quantity',
        	  'requires_shipping')
    # readonly_fields = ( )
    show_add_link = True
    # inlines = []
    extra = 1









# Register your models here.
@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    """Registering PRoduct in admin."""

    model = Product
    inlines = [ImagesInline, OptionInline, TagInline, VariantInline]

