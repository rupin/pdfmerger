$( document ).ready(function() {
    $( ".datefield" ).datepicker({dateFormat:"MM d, yy", showButtonPanel: true});
    //console.log("attached");
});

$(document).ready(function() 

{
		    $( ".sortable" ).sortable();
		    $( ".sortable" ).disableSelection();



		    $("#savearrangement").bind("click", function(){

		    	fieldSequenceData=getFieldSequence()
		    	token = $('#csrfmiddlewaretoken').val()


		    	ajaxData={}
		    	ajaxData.fieldData=fieldSequenceData
		    	ajaxData.formID=$("#formID").val()	
				ajaxData.csrfmiddlewaretoken=token
		    	//console.log(fieldSequenceData)
		    	saveFieldSequence(ajaxData);
		    		
		    });

			function getFieldSequence()
			{
				arrangedFields=$("#field_rows").children("div.field_row");
		    		totalFields=arrangedFields.length
		    		fieldList=""
		    		for(i=0;i<totalFields;i++)
		    		{

		    			field=arrangedFields[i];
		    			//fieldSequence.fieldID=$(field).attr("data-id");
		    			//fieldSequence.fieldIndex=i;
		    			//fieldList[i]=$(field).attr("data-id");
		    			fieldList=fieldList+ " "+ $(field).attr("data-id");
		    			
		    		}

		    	//https://stackoverflow.com/questions/1144783/how-to-replace-all-occurrences-of-a-string
		    	fieldList=fieldList.trim().replace(/ /g, ",") //global replace o spaces

		    	return fieldList
		    		
			}

			function saveFieldSequence(data)

			{
			//console.log(data)
				var status=$.ajax({
						url: "/saveFormFieldSequence/",
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

    
