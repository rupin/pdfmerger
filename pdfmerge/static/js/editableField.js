$( document ).ready(function() {

$(".double-click-edit").bind('click', function(){
	event.stopPropagation();
	$(this).hide();
	$(this).siblings(".question_data_edit").show();
});


$(".saveEditField").bind('click', function(){

	//$(this).hide();
	event.stopPropagation();
	fieldParentHolder=$(this).parent().siblings("div.question_data_edit")
	field=fieldParentHolder.children();

	htmlfieldType=field.get(0).tagName
	fieldValue=""
	switch(htmlfieldType)
	{
		case "SELECT":
			fieldValue=$(field).children("option:selected").val();
			break

		case "INPUT":
			fieldValue=field.val()
			break

	} 

	fieldID=field.attr("data-id");	
	formID=$("#formID").val()

	token = $('#csrfmiddlewaretoken').val()
	data={}
	data.fieldID=fieldID
	data.fieldValue=fieldValue
	data.formID=formID
	data.csrfmiddlewaretoken=token

	console.log(data)
	//return

	var dataSavestatus=saveFieldEdit(data);

	console.log(dataSavestatus)
	if(dataSavestatus)
	{
		switch(htmlfieldType)
		{
			case "SELECT":
				fieldText=$(field).children("option:selected").html();
				$(this).parent().siblings("div.question_data").html(fieldText).show();
				break

			case "INPUT":
				
				$(this).parent().siblings("div.question_data").html(fieldValue).show();
				break

		} 
		
	}

	$(this).parent().hide();
	fieldParentHolder.hide();


	
	

});

$(".cancelEditField").bind('click', function(){

	//$(this).hide();
	event.stopPropagation();
	myParent=$(this).parent().hide()
	$(this).parent().siblings("div.question_data_edit").hide()
	$(this).parent().siblings("div.question_data").show()
	


	
	

});
$("#refreshbutton").bind("click", function(){

	$("iframe").attr( 'src', function ( i, val ) { return val; });
})




function saveFieldEdit(data)

{
	//console.log(data)
	var status=$.ajax({
    url: "/saveEditedField/",
    method: "POST",
    data:data,
    dataType: "json",
    success:function(data, status, xhr)
    {
    	return true;
    },

    error:function(jqXhr, textStatus, errorMessage)
    {
    	return false;
    }
    
    
    
		});

	return status
        
}




});
