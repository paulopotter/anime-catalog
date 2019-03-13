let fillHeader = (elementId) => {
    // let elId = elementId.replace(/anime-/g, '');
    let el = document.querySelector(`#${elementId}`);
    let item = data[el.getAttribute('data-index')][el.getAttribute('data-position')]
    let header = document.getElementById('header');
    let itemImg = item.path + '/thumb.png';

    let rate = '';
    for(let i = 0; i<item.rate; i++){ rate += '🤩'; }

    header.querySelector('img').src = itemImg;
    header.querySelector('img').setAttribute('onerror', 'this.src="./src/presentation/static/img/placeholder.gif"');
    header.querySelector('.header__info--name').innerText = item.name;
    header.querySelector('.header__info--genre').innerHTML = '';
    item.genre.forEach(element => {
        header.querySelector('.header__info--genre').innerHTML += `<span>${element}</span>`
    });
    header.querySelector('.header__info--rate').innerText = rate;
    header.querySelector('.header__info--season').innerText = item.season;
    header.querySelector('.header__info--totalEpisodes').innerText = item.totalEpisodes || '';
    // header.querySelector('.header__info--episodesDownloaded').innerText = item.episodesDownloaded || '';
    header.querySelector('.header__info--description').innerText = item.description;
    header.querySelector('.header__info--othersSeasons').innerHTML = '';
    item.othersSeasons.forEach(element => {
        header.querySelector('.header__info--othersSeasons').innerHTML += `<li>${element}</li>`
    });
    header.querySelector('.header__info--obs').innerText = item.obs || '';
}
const moveItem = (item) => {
    item.parentElement.scroll({
        top: item.offsetTop - 30 - document.defaultView.getComputedStyle(item.parentElement).paddingTop.replace("px", "") ,
        left: 0,
        behavior: 'smooth'
    });
    history.replaceState('', '', '#' + item.id)
}

for (let item of document.querySelectorAll('.catalog__item')) {
    item.addEventListener('click', (ev) => {
        let selectedItem = ev.target.parentElement.parentElement;
        fillHeader(selectedItem.id)
        moveItem(selectedItem);
    }, false)
}

document.querySelector('.header__info--othersSeasons')
    .addEventListener('click', (ev) => {
        if (ev.target.innerHTML.indexOf('<li>') == -1) {
            let selectedItemName = ev.target.innerText.slugify()
            moveItem(document.getElementById(`id-${selectedItemName}`));
            fillHeader(`id-${selectedItemName}`)
        }
    }, false)
