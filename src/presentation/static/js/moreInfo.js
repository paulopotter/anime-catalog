for (let item of document.querySelectorAll('.catalog__item')) {
   item.addEventListener('click', (ev) => {
        let header = document.getElementById('header');
        let selectedItem = ev.target.parentElement.parentElement;
        let item = data[selectedItem.getAttribute('data-index')][selectedItem.getAttribute('data-position')]
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
        header.querySelector('.header__info--othersSeasons').innerText = item.othersSeasons || '';
        header.querySelector('.header__info--obs').innerText = item.obs || '';

    }, false)
}
