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
			amount=10,
			currency='usd',
			description="donation"
		)

	return redirect('success')


def successMsg(request):
	return render(request, 'success.html')
