function tmpl_content(arr, dad, dataGroup) {
    var template = document.getElementById("template_item").innerHTML,
        el = document.createElement('li');
    el.className = 'anime-item'
    el.setAttribute('data-group', dataGroup);
    el.innerHTML = template;

    for (var dataKey in arr) {
        if (el.getElementsByClassName(dataKey).length > 0) {
            if (arr[dataKey].length <= 0) {
                var elDataKey = el.getElementsByClassName(dataKey)[0];
                elDataKey.parentElement.removeChild(elDataKey);
            } else {
                if (dataKey == 'genre') {
                    var value = '';
                    for (var genreData in arr[dataKey]) {
                        value += arr[dataKey][genreData] + ', ';
                        genresNames.push(arr[dataKey][genreData]);
                    }
                    value = value.slice(0, -2);
                } else {
                    var value = arr[dataKey];
                }

                el.getElementsByClassName(dataKey)[0].innerHTML += value;
            }
        } else {
            if (dataKey == 'path') {
                el.getElementsByTagName("object")[0].data = arr.path + '/thumb.png';
            } else {
                child = document.createElement('li');
                child.className = dataKey;
                child.innerHTML = dataKey + ': ' + arr[dataKey];
                el.getElementsByClassName('plus')[0].append(child);
            }
        }
    }
    if (el.getElementsByTagName('object')[0].data == '') {
        el.getElementsByTagName('object')[0].data = '../Animes/' + toTitleCase(arr['name']) + '/thumb.png';
    }

    el.id = arr['name'];

    dad.appendChild(el);
};
