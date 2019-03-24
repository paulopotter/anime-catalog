document.querySelectorAll('.catalog__item').forEach(item => {
    item.addEventListener('click', (ev) => {
        let selectedItem = ev.target.parentElement.parentElement;
        fillWithSelectedItem(selectedItem);
    }, false)
})

document.querySelector('.header__info--othersSeasons')
    .addEventListener('click', (ev) => {
        if (ev.target.innerHTML.indexOf('<li>') == -1) {
            let selectedItemName = ev.target.innerText.slugify()
            fillWithSelectedItem(document.getElementById(`id-${selectedItemName}`));
        }
    }, false)

document.getElementById('header')
    .addEventListener('click', (evt) => {
        if(evt.target.nodeName != "LI"){
            document.getElementById('header').classList.add('header__more-info--open')
        }
    }, false)

document.getElementById('catalog')
    .addEventListener('click', () => {
        document.getElementById('header').classList.remove('header__more-info--open')
    }, false)

document.onkeydown = (evt) => {
    evt = evt || window.event;
    const animeItems = document.querySelectorAll('.catalog__item:not(.hidden)');
    let showInfo = document.querySelector('.catalog__item--selected:not(.hidden)');

        switch (evt.keyCode) {
            case 13: // 13 - Enter
                document.getElementById('header').classList.add('header__more-info--open')
            break;

            case 27: // 27 - ESC
                document.getElementById('header').classList.remove('header__more-info--open')
                document.getElementById('search').classList.remove('open')
            break;

            case 37: // 37 - left
            if (!document.activeElement.classList.contains('search__input')){
                    fillWithSelectedItem(getPreviousSibling(showInfo, ':not(.hidden)'));
                }
            break;

            case 39: // 39 - right
            if (!document.activeElement.classList.contains('search__input')){
                    fillWithSelectedItem(getNextSibling(showInfo, ':not(.hidden)'))
                }
            break;

            case 38: // up
                evt.preventDefault()
                let goal = (showInfo.offsetTop - showInfo.offsetHeight - 10)
                if (goal <=0 && isElementVisible(document.querySelector('input'))) {
                        document.querySelector('input').focus()
                }
                animeItems.forEach(item => {

                    if (goal > 0 &&
                        (closest(animeItems, goal) == item.offsetTop) &&
                        (showInfo.offsetLeft == item.offsetLeft)
                    ) {
                        fillWithSelectedItem(item);
                    }
                })
            break;

            case 40: // Down
                evt.preventDefault()
                if (isElementVisible(document.querySelector('input')) && document.activeElement.classList.contains('search__input')) {
                    document.querySelector('input').blur()
                    if(showInfo){
                        fillWithSelectedItem(showInfo);
                    } else {

                        fillWithSelectedItem(animeItems[0]);
                    }
                } else {
                    let goal = (showInfo.offsetTop + showInfo.offsetHeight + 10)
                    animeItems.forEach(item => {
                        if (
                            (closest(animeItems, goal) == item.offsetTop) &&
                            (showInfo.offsetLeft == item.offsetLeft)
                        ) {
                            fillWithSelectedItem(item);
                        }
                    })
                }
            break;

            case 70: // F
                let search = document.getElementById('search')
                if (!search.classList.contains('open')) {
                    search.classList.add('open');
                    search.querySelector('input').focus(evt.preventDefault())
                }
            break
        }
};

document.querySelector('.search__button')
    .addEventListener('click', () => {
        let searchClass = document.getElementById('search').classList
        if(searchClass.contains('open') ){
            searchClass.remove('open')
        }else {
            searchClass.add('open')
        }
})

document.querySelector('.search__input')
    .addEventListener('keydown', evt => {
        let value = evt.target.value
        const animeItems = document.querySelectorAll('.catalog__item');
        if (value.length >= 2){
            if (event.keyCode >= 48 && event.keyCode <= 90 || event.keyCode == 8) {
                let found = document.querySelectorAll(`[id*='${value.slugify()}']`)
                animeItems.forEach(item => {
                    item.classList.add('hidden')
                })
                found.forEach(item => {
                    item.classList.remove('hidden')
                })

            }

        } else {
            animeItems.forEach(item => {
                item.classList.remove('hidden');
            })
            fillWithSelectedItem(animeItems[0])
        }
    })
