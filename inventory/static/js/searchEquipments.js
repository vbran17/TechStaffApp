const searchField=document.querySelector("#searchField");

searchField.addEventListener("keyup", (e)=>{
    const searchValue=e.target.value;

    if (searchValue.trim().length > 0) {
        console.log('Search value: ', searchValue);

        fetch("")


    }
})