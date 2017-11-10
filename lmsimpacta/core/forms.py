from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", required=True)
    email = forms.EmailField(label="E-mail", help_text="Informe um E-mail válido")
    RA = forms.CharField(label="RA", required=True)
    Telefone = forms.CharField(label="Telefone*", required=True)
    Mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea(), required=True)

    def envia_email(self):
        print(
        "Email Para você:\n"+
        "Aluno: "+self.cleaned_data["nome"]+"\n"+
        "Email: "+self.cleaned_data["email"]+"\n"+
        "Mensagem: "+self.cleaned_data["mensagem"]
        )