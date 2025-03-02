from django import forms
from .models import Transaction, PaymentMethod, Category, VideoPost, Comment

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'amount', 'purpose', 'transaction_type', 'category', 'major_category', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'step': '1.0', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # 'user' キーワード引数を取得
        super(TransactionForm, self).__init__(*args, **kwargs)
        
        # ユーザーに基づいてクエリセットをフィルタリング
        if user is not None:
            self.fields['payment_method'].queryset = PaymentMethod.objects.filter(user=user)
            self.fields['payment_method'].empty_label = None  # 空のラベルを非表示にする
            self.fields['payment_method'].required = True  # フィールドを必須にする
            self.fields['category'].queryset = Category.objects.filter(user=user)
            self.fields['category'].empty_label = None  # 空のラベルを非表示にする
            self.fields['category'].required = True  # フィールドを必須にする

        # すべてのフィールドに 'form-control' クラスを追加
        for field_name, field in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['name']
        
    # bootstrap4対応で、classを指定
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  
            
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        
        fields = ['name']
    # bootstrap4対応で、classを指定
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  

# user：取引を行ったユーザー
# amount：金額
# date：取引日
# transaction_type：支出、収入、変動なし
# paymentmethod：支払方法（デフォルトは現金のみ、他はユーザーが登録できて選択式）
# purpose：用途、例（ステーキ）
# major_category：用途の大項目、例（固定費）（固定費、変動費、特別費）
# category：用途の項目、例（食費）（食費、娯楽、病院など、ユーザーが登録できて選択式）
# purpose_description：用途の詳細、例（○○で買った）


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={
        'type': 'date',
        'class': 'form-control'
    }))

class VideoPostForm(forms.ModelForm):
    class Meta:
        model = VideoPost
        fields = ['date', 'title', 'character', 'result', 'video_url', 'notes']
        error_messages = {
            'date': {
                'required': '日付を入力してください。',
            },
            'title': {
                'required': 'タイトルを入力してください。',
            },
            'character': {
                'required': '使用キャラを入力してください。',
            },
            'video_url': {
                'required': '動画URLを入力してください。',
            },
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'コメントを入力してください...', 'rows': 2})
        }