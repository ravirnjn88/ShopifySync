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
from django.utils.safestring import mark_safe
import nested_admin


class ImagesInline(nested_admin.NestedTabularInline):
    """this inline class is used in Products for showing related images directly."""

    model = Image
    form = ImageForm
    fields = ('position', 'src', 'width', 'height', 'alt')
    readonly_fields = ('position', 'src', 'width', 'height', 'alt')
    extra = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OptionValueInline(nested_admin.NestedTabularInline):
    """this inline class is used in Products for showing related options directly."""

    model = OptionValue
    form = OptionValueForm
    fields = ('name',)
    readonly_fields = ('name',)
    extra = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OptionInline(nested_admin.NestedTabularInline):
    """this inline class is used in Products for showing related options directly."""

    model = Option
    form = OptionForm
    fields = ('option_name', 'position')
    readonly_fields = ('option_name', 'position')
    inlines = [OptionValueInline]
    extra = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TagInline(nested_admin.NestedTabularInline):
    """this inline class is used in Products for showing tags."""

    model = Tag
    form = TagForm
    fields = ('name',)
    readonly_fields = ('name',)
    extra = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class VariantInline(nested_admin.NestedStackedInline):
    """this inline class is used in Products for showing Variant."""

    model = Variant
    form = VariantForm
    fields = ('title', 'price', 'sku', 'position', 'compare_at_price',
              'option1', 'option2', 'option3', 'taxable', 'barcode',
              'weight', 'weight_unit', 'image', 'inventory_quantity',
              'requires_shipping')
    readonly_fields = ('title', 'price', 'sku', 'position', 'compare_at_price',
              'option1', 'option2', 'option3', 'taxable', 'barcode',
              'weight', 'weight_unit', 'image', 'inventory_quantity',
              'requires_shipping')
    extra = 0


    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# Register your models here.
@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    """Registering PRoduct in admin."""

    model = Product
    inlines = [ImagesInline, OptionInline, TagInline, VariantInline]
    list_display = ['shopify_product_id', 'title', 'product_type', 'product_image']
    extra = 0
    fields = ('shopify_product_id', 'title', 'body_html', 'vendor', 'product_type',
              'handle', 'published_scope', 'admin_graphql_api_id', 'published_at')
    readonly_fields = ('shopify_product_id', 'title', 'body_html', 'vendor', 'product_type',
              'handle', 'published_scope', 'admin_graphql_api_id', 'published_at')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(ProductAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

    def product_image(self, obj):                       
        return mark_safe('<img src="%s"/ width=50px height=50px >' % obj.images.all().first())
    product_image.allow_tags = True