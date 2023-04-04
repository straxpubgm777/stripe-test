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
