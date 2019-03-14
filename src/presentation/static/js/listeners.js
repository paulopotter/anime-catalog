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
    const animeItems = document.querySelectorAll('.catalog__item');
    let showInfo = document.querySelector('.catalog__item--selected');

        switch (evt.keyCode) {
            case 13: // 13 - Enter
                document.getElementById('header').classList.add('header__more-info--open')
            break;

            case 27: // 27 - ESC
                document.getElementById('header').classList.remove('header__more-info--open')
            break;

            case 37: // 37 - left
                fillWithSelectedItem(showInfo.previousElementSibling);
            break;

            case 39: // 39 - right
                fillWithSelectedItem(showInfo.nextElementSibling)
            break;

            case 38: // up
                evt.preventDefault()
                animeItems.forEach(item => {
                    let goal = (showInfo.offsetTop - showInfo.offsetHeight - 10)

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
                animeItems.forEach(item => {
                    let goal = (showInfo.offsetTop + showInfo.offsetHeight + 10)
                    if (
                        (goal == item.offsetTop) &&
                        (showInfo.offsetLeft == item.offsetLeft)
                    ) {
                        fillWithSelectedItem(item);
                    }
                })
            break;
        }
};


function closest(arr, target) {
    // Based on
    // https://stackoverflow.com/a/25087661
    if (!(arr) || arr.length == 0)
        return null;
    if (arr.length == 1)
        return arr[0];

    for (let i = 1; i < arr.length; i++) {
        // As soon as a number bigger than target is found, return the previous or current
        // number depending on which has smaller difference to the target.
        if (arr[i].offsetTop > target) {
            let p = arr[i - 1].offsetTop;
            let c = arr[i].offsetTop
            return Math.abs(p - target) < Math.abs(c - target) ? p : c;
        }
    }
    // No number in array is bigger so return the last.
    return arr[arr.length - 1];
}
