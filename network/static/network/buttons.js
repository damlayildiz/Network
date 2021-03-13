function edit(id) {
    var editText = document.querySelector(`#text-${id}`);
    var editButton = document.querySelector(`#edit-${id}`);
    var text = document.querySelector(`#post-${id}`);

    editText.style.display = 'block';
    editButton.style.display = 'block';
    editText.value = text.innerHTML;

    editButton.addEventListener("click", () => {
        fetch('/edit/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                text: editText.value
            })
        });
        
        editText.style.display = 'none';
        editButton.style.display = 'none';
        text.innerHTML = editText.value;
    });

    editText.innerHTML = "";
}

function like(id) {
    var button = document.querySelector(`#like-${id}`);

    if (button.style.backgroundColor == "white") {
        button.innerHTML = parseInt(button.innerHTML) + 1;
        button.style.backgroundColor = "red";
        button.style.color = "white";

        fetch('/like/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                liked: true
            })
        });
    } else {
        button.innerHTML = parseInt(button.innerHTML) - 1;
        button.style.backgroundColor = "white";
        button.style.color = "red";

        fetch('/like/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                liked: false
            })
        });
    }
}

