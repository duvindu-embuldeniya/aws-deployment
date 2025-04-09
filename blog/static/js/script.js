let form = document.getElementById('blog_form');
let pages = document.getElementsByClassName('page');


for(let i=0; i < pages.length; i++){
    pages[i].addEventListener('click', func);

    function func(e){
        e.preventDefault();

        let page = this.dataset.page;

        form.innerHTML += `<input type='text' name="page" value=${page} hidden>`;

        form.submit();
    }
}



let closer = document.querySelector('.msg')

setTimeout(function(){
    closer.style.display = 'none';
}, 2000)