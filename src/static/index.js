function addInputField(){
    let txtNewInputBox = document.createElement('div');

	txtNewInputBox.innerHTML = "<input class ='input-style' id = 'movieName' type='text' name='movieName' placeholder='Enter movie title'><br><br>";

	document.getElementById("newElementId").appendChild(txtNewInputBox);
}
