import android

app = android.Android()
app.dialogCreateAlert("Select an athlete:")
app.dialogSetSingleChoiceItems(['Mikey','Sarah','James','Julie'])
app.dialogSetPositiveButtonText('Select')
app.dialogSetNegativeButtonText('Quit')
app.dialogShow()
resp = app.dialogGetResponse().result
