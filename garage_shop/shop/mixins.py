from django import views

from .models import Category, Oil, Filter, Product, Notification
#Cart, Customer, Notification
from django.views.generic.detail import SingleObjectMixin


class CategoryMixin(SingleObjectMixin):

    CATEGORY_MODEL = {
        'oil': Oil,
        'filter': Filter

    }

    def get_context_data(self, **kwargs):
        if isinstance:
            model = self.CATEGORY_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['products_category'] = model.objects.all()
            return context
        context = super().get_context_data(**kwargs)
        return context

class CategoryLeftMixin(SingleObjectMixin):

    def get_context_data(self, **kwargs):
        model = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['categories'] = model
        return context


class ProductAvailableMixin(SingleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_category'] = Product.objects.filter(available=True)
        return context


class NotificationsMixin(views.generic.detail.SingleObjectMixin):

    @staticmethod
    def notifications(user):
        if user.is_authenticated:
            return Notification.objects.all(user.customer)
        return Notification.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = self.notifications(self.request.user)
        return context


# class CartMixin(views.generic.detail.SingleObjectMixin, views.View):

    # def dispatch(self, request, *args, **kwargs):
    #     cart = None
    #     if request.user.is_authenticated:
    #         customer = Customer.objects.filter(user=request.user).first()
    #         if not customer:
    #             customer = Customer.objects.create(
    #                 user=request.user
    #             )
    #         cart = Cart.objects.filter(owner=customer, in_order=False).first()
    #         if not cart:
    #             cart = Cart.objects.create(owner=customer)
    #     self.cart = cart
    #     return super().dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['cart'] = self.cart
    #     return context
