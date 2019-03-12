let fillHeader = (elementId) => {
    let el = document.querySelector(`#${elementId}`);
    let item = data[el.getAttribute('data-index')][el.getAttribute('data-position')]
    let header = document.getElementById('header');
    let itemImg = item.path + '/thumb.png';

    let rate = '';
    for(let i = 0; i<item.rate; i++){ rate += '🤩'; }

    header.querySelector('img').src = itemImg;
    header.querySelector('.header__info--name').innerText = item.name;
    header.querySelector('.header__info--genre').innerText = item.genre;
    header.querySelector('.header__info--rate').innerText = rate;
    header.querySelector('.header__info--season').innerText = item.season;
    header.querySelector('.header__info--totalEpisodes').innerText = item.totalEpisodes || '';
    // header.querySelector('.header__info--episodesDownloaded').innerText = item.episodesDownloaded || '';
    header.querySelector('.header__info--description').innerText = item.description;
    header.querySelector('.header__info--othersSeasons').innerHTML = '';
    item.othersSeasons.forEach(element => {
        header.querySelector('.header__info--othersSeasons').innerHTML += `<span>${element}</span>`
    });
    header.querySelector('.header__info--obs').innerText = item.obs || '';
}
const moveItem = (item) => {
    item.parentElement.scroll({
        left: item.offsetLeft - 70,
        top: 0,
        behavior: 'smooth'
    });
    history.replaceState('', '', '#' + item.innerText.slugify())
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
        let selectedItemName = ev.target.innerText.slugify()
        moveItem(document.getElementById(selectedItemName));
        fillHeader(selectedItemName)
    }, false)
