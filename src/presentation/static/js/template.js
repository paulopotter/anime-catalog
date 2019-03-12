const tmp = (image, name, dIndex, dPosition) => {
    const dad = document.getElementById('catalog');

    let wrapper = document.createElement('div');
    wrapper.className = 'catalog__item';
    wrapper.setAttribute('data-index', dIndex);
    wrapper.setAttribute('data-position', dPosition);
    wrapper.id = name.slugify();


    let picture = document.createElement('picture');
    picture.className = 'catalog__item--picture';
    picture.setAttribute('srcset', './src/presentation/static/img/placeholder.gif');

    wrapper.appendChild(picture);

    let img = document.createElement('img');
    img.src = image;
    img.className = 'catalog__item--image';

    picture.appendChild(img);

    let span = document.createElement('span');
    span.className = "catalog__item--name";
    span.innerText = name;

    picture.appendChild(span);

    dad.appendChild(wrapper)
}
