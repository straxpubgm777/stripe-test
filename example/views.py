from django.shortcuts import render, redirect
import stripe

stripe.api_key = "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"

def index(request):
	return render(request, 'index.html')


def charge(request):

	if request.method == 'POST':
		print('Data:', request.POST)
		customer = stripe.Customer.create(
			email = request.POST['email'],
			name = request.POST['nickname'],
			source = request.POST['stripeToken']
		)
		charge = stripe.Charge.create(
			customer=customer,
			amount=50,
			currency='usd',
			description="donation"
		)

	return redirect('success')


def successMsg(request):
	return render(request, 'success.html')