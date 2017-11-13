function edit_row(no)
{
 document.getElementById("edit_button"+no).style.display="none";
 document.getElementById("save_button"+no).style.display="block";
	
 var school=document.getElementById("School_row"+no);
 var country=document.getElementById("Country_row"+no);
 var course=document.getElementById("Course_row"+no);
 var scuCourse=document.getElementById("SCUCourse_row"+no);
 var determination=document.getElementById("Determination_row"+no);
 var advisor=document.getElementById("Advisor_row"+no);
 var date=document.getElementById("Date_row"+no);
	
 var sd=school.innerHTML;
 var ctd=country.innerHTML; 
 var cd=course.innerHTML;
 var scud=scuCourse.innerHTML;
 var dd=determination.innerHTML;
 var ad=advisor.innerHTML;
 var dtd=date.innerHTML;
	
 school.innerHTML="<input type='text' id='st"+no+"' value='"+sd+"'>";
 country.innerHTML="<input type='text' id='ctt"+no+"' value='"+ctd+"'>";
 course.innerHTML="<input type='text' id='ct"+no+"' value='"+cd+"'>";
 scuCourse.innerHTML="<input type='text' id='scut"+no+"' value='"+scud+"'>";
 determination.innerHTML="<input type='text' id='det"+no+"' value='"+dd+"'>";
 advisor.innerHTML="<input type='text' id='at"+no+"' value='"+ad+"'>";
 date.innerHTML="<input type='text' id='dt"+no+"' value='"+dtd+"'>";
  
}

function save_row(no)
{
 var sSchool=document.getElementById("st"+no).value;
 var sCountry=document.getElementById("ctt"+no).value;
 var sCourse=document.getElementById("ct"+no).value;
 var sSCU=document.getElementById("scut"+no).value;
 var sDetermination=document.getElementById("det"+no).value;
 var sAdvisor=document.getElementById("at"+no).value;
 var sDate=document.getElementById("dt"+no).value;  

 document.getElementById("School_row"+no).innerHTML=sSchool;
 document.getElementById("Country_row"+no).innerHTML=sCountry;
 document.getElementById("Course_row"+no).innerHTML=sCourse;
 document.getElementById("SCUCourse_row"+no).innerHTML=sSCU;
 document.getElementById("Determination_row"+no).innerHTML=sDetermination;
 document.getElementById("Advisor_row"+no).innerHTML=sAdvisor;
 document.getElementById("Date_row"+no).innerHTML=sDate;
  
 document.getElementById("edit_button"+no).style.display="block";
 document.getElementById("save_button"+no).style.display="none";
}

function delete_row(no)
{
 document.getElementById("row"+no+"").outerHTML="";
}

function add_row()
{
 var newSchool=document.getElementById("newSchool").value;
 var newCountry=document.getElementById("newCountry").value;
 var newCourse=document.getElementById("newCourse").value;
 var newSCUCourse=document.getElementById("newSCUCourse").value;
 var newDetermination=document.getElementById("newDetermination").value;
 var newAdvisor=document.getElementById("newAdvisor").value;
 var newDate=document.getElementById("newDate").value;
  
	
 var table=document.getElementById("Table");
 var len=(table.rows.length)-1;
 var row = table.insertRow(len).outerHTML="<tr id='row"+len+"'><td id='School_row"+len+"'>"+newSchool+"</td><td id='Country_row"+len+"'>"+newCountry+"</td><td id='Course_row"+len+"'>"+newCourse+"</td><td id='SCUCourse_row"+len+"'>"+newSCUCourse+"</td><td id='Determination_row"+len+"'>"+newDetermination+"</td><td id='Advisor_row"+len+"'>"+newAdvisor+"</td><td id='Date_row"+len+"'>"+newDate+"</td><td><input type='button' id='edit_button"+len+"' value='Edit' class='edit' onclick='edit_row("+len+")'> <input type='button' id='save_button"+len+"' value='Save' class='save' onclick='save_row("+len+")'> <input type='button' value='Delete' class='delete' onclick='delete_row("+len+")'></td></tr>";

 document.getElementById("newSchool").value="";
 document.getElementById("newCountry").value="";
 document.getElementById("newCourse").value="";
 document.getElementById("newSCUCOurse").value="";
 document.getElementById("newDetermination").value="";
 document.getElementById("newAdvisor").value="";
 document.getElementById("newDate").value="";
}

function search() 
{
  var input, filter, table, tr,td2, td3, i;
  input = document.getElementById("input");
  filter = input.value.toUpperCase();
  table = document.getElementById("Table");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td2 = tr[i].getElementsByTagName("td")[2];
    td3 = tr[i].getElementsByTagName("td")[3];
    if (td2 || td3 ) {
      if (td2.innerHTML.toUpperCase().indexOf(filter) > -1 || td3.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    } 
  }
}