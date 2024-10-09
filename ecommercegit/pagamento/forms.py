from django import forms

class CheckoutForm(forms.Form):
    payment_method_nonce = forms.CharField(max_length=1000,
                                           widget=forms.widgets.HiddenInput,
                                           required=False,  # In the end it's a required field, but I wanted to provide a custom exception message
                                           )

    def clean(self):
        self.cleaned_data = super(CheckoutForm, self).clean()
        # Braintree nonce is missing
        if not self.cleaned_data.get('payment_method_nonce'):
            raise forms.ValidationError(
                'Não foi possível verificar seu pagamento. Tente novamente.')
        return self.cleaned_data
