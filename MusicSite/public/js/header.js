let dropdownList = document.getElementsByClassName("search-category");

for (let i = 0; i < dropdownList.length; i++){
    dropdownList[i].onclick = function(){
        document.getElementsByClassName("active")[0].classList.remove("active");
        document.getElementsByClassName("search-category")[i].classList.add("active");
        placeholderText = `Search by ${document.getElementsByClassName("search-category")[i].textContent}`;
        document.getElementById("search-bar").setAttribute("placeholder", placeholderText);
    }
}
