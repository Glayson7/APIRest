from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Order
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=int(
                order.get_total_cost() * 100
            ),  # O Stripe espera o valor em centavos
            currency="USD",
            description=f"Charge for order {order.id}",
            source=request.POST["stripeToken"],
        )

        if charge.paid:
            order.paid = True
            order.save()

            return render(
                request, "orders/order/created.html", {"order": order}
            )

    return render(request, "orders/order/payment.html", {"order": order})
