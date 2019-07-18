from django import template

register = template.Library()

@register.filter(name='create_html_options_tags')
def create_html_options_tags(index,field_values_list):
	optionValueList=field_values_list.split(",")
	optioncount=0
	returnValue=""
	for optionValue in optionValueList:
		returnValue=returnValue + "<option value='{}'>{}</option>".format(optioncount,optionValue)
		optioncount=optioncount+1
	return returnValue


@register.filter(name='multi_choice_field_value')
def multi_choice_field_value(index,field_values_list):
	#print(field.field__field_display)
	optionValueList=field_values_list.split(",")

	return optionValueList[int(index)]
	


