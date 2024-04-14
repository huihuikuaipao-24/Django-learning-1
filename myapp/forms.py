
#这段代码是一个使用Django的表单类的示例。它定义了一个名为CreateNewList的表单类，该类继承自forms.Form。

#CreateNewList表单类包含两个字段：

#name字段是一个CharField，用于接收用户输入的名称。它使用label参数设置字段的标签为"Name"，并使用max_length参数限制输入的最大长度为200个字符。
#check字段是一个BooleanField，用于接收用户选择的复选框。它默认显示为复选框形式。
#这个表单类可以在Django视图中使用，以便在前端显示表单并处理用户提交的数据。您可以根据需要在视图中对该表单进行实例化、验证和处理。

from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    check = forms.BooleanField()


    