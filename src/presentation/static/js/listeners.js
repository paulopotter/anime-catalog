const HEADER = document.getElementById('header');
const SEARCH = document.getElementById('search');
const SEARCH_INPUT = SEARCH.querySelector('.search__input');


document.querySelectorAll('.catalog__item')
    .forEach(item => {
        item.addEventListener('click', (ev) => {
            const headerClass = HEADER.classList;
            if (headerClass.contains('header__more-info--open')) {
                headerClass.remove('header__more-info--open');
            } else {
                fillWithSelectedItem(ev.target.parentElement.parentElement);
                headerClass.add('header__more-info--open');
            }
        }, false)
    })

HEADER.querySelector('.header__info--othersSeasons')
    .addEventListener('click', (ev) => {
        if (ev.target.innerHTML.indexOf('<li>') == -1) {
            let selectedItemName = ev.target.innerText.slugify()
            fillWithSelectedItem(document.getElementById(`id-${selectedItemName}`));
        }
    }, false)

document.addEventListener('keydown', (evt) => {
    evt = evt || window.event;
    const animeItems = document.querySelectorAll('.catalog__item:not(.hidden)');
    const showInfo = document.querySelector('.catalog__item--selected:not(.hidden)');
    const headerClasses = HEADER.classList;
    const isHeaderOpen = headerClasses.contains('header__more-info--open');
    const isSearchInputActive = document.activeElement.classList.contains('search__input');
    const navigate = isHeaderOpen && !isSearchInputActive ? false : isHeaderOpen ? false : !isSearchInputActive;

    switch (evt.keyCode) {
        case 13: // 13 - Enter
            HEADER.classList.add('header__more-info--open');
        break;

        case 27: // 27 - ESC
            HEADER.classList.remove('header__more-info--open')
            SEARCH.classList.remove('open')
            SEARCH_INPUT.blur()
        break;

        case 37: // 37 - left
            navigate ? fillWithSelectedItem(getPreviousSibling(showInfo, ':not(.hidden)')) : null
        break;

        case 39: // 39 - right
            navigate ? fillWithSelectedItem(getNextSibling(showInfo, ':not(.hidden)')) : null
        break;

        case 38: // up
            evt.preventDefault()
            if (navigate) {
                let goal = (showInfo.offsetTop - showInfo.offsetHeight - 10)

                if (goal <=0 && isElementVisible(SEARCH)){
                    !isSearchInputActive ? document.querySelector('input').focus() : null
                } else {
                    animeItems.forEach(item => {
                        if (goal > 0 &&
                            (closest(animeItems, goal) == item.offsetTop) &&
                            (showInfo.offsetLeft == item.offsetLeft)) {

                            fillWithSelectedItem(item);
                        }
                    })
                }
            } else {
                evt.preventDefault()
            }
        break;

        case 40: // Down
            evt.preventDefault()
            if(navigate){
                let goal = (showInfo.offsetTop + showInfo.offsetHeight + 10)
                animeItems.forEach(item => {
                    if (
                        (closest(animeItems, goal) == item.offsetTop) &&
                        (showInfo.offsetLeft == item.offsetLeft)
                    ) {
                        fillWithSelectedItem(item);
                    }
                })
            } else {
                SEARCH_INPUT.blur()
                if(showInfo){
                    fillWithSelectedItem(showInfo);
                } else {
                    fillWithSelectedItem(animeItems[0]);
                }

            }
        break;

        case 70: // F
            if (!SEARCH.classList.contains('open')) {
                SEARCH.classList.add('open');
                SEARCH_INPUT.focus(evt.preventDefault())
            }
        break
    }
});

SEARCH.querySelector('.search__button')
    .addEventListener('click', () => {
        let searchClass = SEARCH.classList
        (searchClass.contains('open') ) ? searchClass.remove('open') : searchClass.add('open')
})

SEARCH_INPUT
    .addEventListener('keydown', evt => {
        let value = evt.target.value
        const animeItems = document.querySelectorAll('.catalog__item');
        if (value.length >= 2){

            if (evt.keyCode >= 48 && evt.keyCode <= 90 || evt.keyCode == 8) {
                animeItems.forEach(item => { item.classList.add('hidden')})
                document.querySelectorAll(`[id*='${value.slugify()}']`).forEach(item => {
                    item.classList.remove('hidden')
                })

            }

        } else {
            if ((!event.keyCode >= 37 && !event.keyCode <= 39 ) || event.keyCode == 8) {
                animeItems.forEach(item => { item.classList.remove('hidden'); })
                fillWithSelectedItem(animeItems[0])
            }
        }
    })
