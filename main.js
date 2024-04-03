function updateBook(el){
    book_id = el.value
    fetch('/read/' + book_id, {
       method: 'patch',
       headers: {'Content-Type': 'application/json'},
       body: JSON.stringify({'ready':el.checked})
    })
}

function createBook(){
    console.log('Create')
    let name = document.getElementById('name').value
    let author = document.getElementById('author').value

    fetch('/book', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'name': name || 'Отсутсвует', 'author': author || 'Отсутсвует', 'read':false})
     })
}