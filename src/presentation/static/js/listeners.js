document.querySelectorAll('.catalog__item').forEach(item => {
    item.addEventListener('click', (ev) => {
        let selectedItem = ev.target.parentElement.parentElement;
        fillHeader(selectedItem.id)
        moveItemTo(selectedItem);
    }, false)
})

document.querySelector('.header__info--othersSeasons')
    .addEventListener('click', (ev) => {
        if (ev.target.innerHTML.indexOf('<li>') == -1) {
            let selectedItemName = ev.target.innerText.slugify()
            moveItemTo(document.getElementById(`id-${selectedItemName}`));
            fillHeader(`id-${selectedItemName}`)
        }
    }, false)

document.getElementById('header')
    .addEventListener('click', () => {
        document.getElementById('header').classList.add('header__more-info--open')
    }, false)

document.getElementById('catalog')
    .addEventListener('click', () => {
        document.getElementById('header').classList.remove('header__more-info--open')
    }, false)


document.onkeydown = function (evt) {
    evt = evt || window.event;
    var showInfo = document.querySelector('.catalog__item--selected');
        // var animeItems = document.querySelectorAll('.catalog__item');
        switch (evt.keyCode) {
            case 13:
            // 13 - Enter
                document.getElementById('header').classList.add('header__more-info--open')
            break;

            case 27:
            // 27 - ESC
                document.getElementById('header').classList.remove('header__more-info--open')
            break;

            case 37:
                // 37 - left
                moveItemTo(showInfo.previousElementSibling);
                fillHeader(showInfo.previousElementSibling.id)
                break;
            case 39:
                // 39 - right
                moveItemTo(showInfo.nextElementSibling);
                fillHeader(showInfo.nextElementSibling.id)
                break;

            case 38: //up
                document.querySelectorAll('.catalog__item').forEach(item => {
                    let goal = (showInfo.offsetTop - showInfo.offsetHeight - 10)
                    let counts = document.querySelectorAll('.catalog__item')

                    if (goal > 0 &&
                        (closest(counts, goal) == item.offsetTop) &&
                        (showInfo.offsetLeft == item.offsetLeft)
                    ) {
                        moveItemTo(item);
                        fillHeader(item.id)
                    }
                })
            break;
            case 40: //Down
                document.querySelectorAll('.catalog__item').forEach(item => {
                    if (
                        ((showInfo.offsetTop + showInfo.offsetHeight + 10) == item.offsetTop) &&
                        ((showInfo.offsetLeft ) == item.offsetLeft)
                    ) {
                        moveItemTo(item);
                        fillHeader(item.id)
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

    for (var i = 1; i < arr.length; i++) {
        // As soon as a number bigger than target is found, return the previous or current
        // number depending on which has smaller difference to the target.
        if (arr[i].offsetTop > target) {
            var p = arr[i - 1].offsetTop;
            var c = arr[i].offsetTop
            return Math.abs(p - target) < Math.abs(c - target) ? p : c;
        }
    }
    // No number in array is bigger so return the last.
    return arr[arr.length - 1];
}
