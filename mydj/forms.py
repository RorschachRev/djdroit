class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('is_exhibitor', 'company')

class StoreEditForm(form.ModelForm):
	class Meta:
		model = Store 
		fields= ('store_name')
