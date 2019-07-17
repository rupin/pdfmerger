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
	field=fieldParentHolder.children("input");

	fieldID=field.attr("data-id");
	fieldValue=field.val()
	formID=$("#formID").val()

	token = $('#csrfmiddlewaretoken').val()
	data={}
	data.fieldID=fieldID
	data.fieldValue=fieldValue
	data.formID=formID
	data.csrfmiddlewaretoken=token

	var dataSavestatus=saveFieldEdit(data);

	console.log(dataSavestatus)
	if(dataSavestatus)
	{
		$(this).parent().siblings("div.question_data").html(fieldValue).show();
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
