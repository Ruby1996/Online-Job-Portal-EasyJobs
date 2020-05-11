from django import forms  
from company.models import com_pro  
class CompanyForm(forms.ModelForm):  
    class Meta:  
        model = com_pro  
        fields = "__all__"  