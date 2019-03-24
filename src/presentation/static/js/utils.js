// https://gist.github.com/gabrielfroes/e90a53f96ed71fb201d133395003ada4
/*
	Create SLUG from a string
	This function rewrite the string prototype and also
	replace latin and other special characters.

	Forked by Gabriel Froes - https://gist.github.com/gabrielfroes
	Original Author: Mathew Byrne - https://gist.github.com/mathewbyrne/1280286
 */
if (!String.prototype.slugify) {
    String.prototype.slugify = function () {

        return this.toString().toLowerCase()
            .replace(/[àÀáÁâÂãäÄÅåª]+/g, 'a') // Special Characters #1
            .replace(/[èÈéÉêÊëË]+/g, 'e') // Special Characters #2
            .replace(/[ìÌíÍîÎïÏ]+/g, 'i') // Special Characters #3
            .replace(/[òÒóÓôÔõÕöÖº]+/g, 'o') // Special Characters #4
            .replace(/[ùÙúÚûÛüÜ]+/g, 'u') // Special Characters #5
            .replace(/[ýÝÿŸ]+/g, 'y') // Special Characters #6
            .replace(/[ñÑ]+/g, 'n') // Special Characters #7
            .replace(/[çÇ]+/g, 'c') // Special Characters #8
            .replace(/[ß]+/g, 'ss') // Special Characters #9
            .replace(/[Ææ]+/g, 'ae') // Special Characters #10
            .replace(/[Øøœ]+/g, 'oe') // Special Characters #11
            .replace(/[%]+/g, 'pct') // Special Characters #12
            .replace(/\s+/g, '-') // Replace spaces with -
            .replace(/[^\w\-]+/g, '') // Remove all non-word chars
            .replace(/\-\-+/g, '-') // Replace multiple - with single -
            .replace(/^-+/, '') // Trim - from start of text
            .replace(/-+$/, ''); // Trim - from end of text

    };
}

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


function isElementVisible(el) {
    // https://stackoverflow.com/a/15203639
    var rect = el.getBoundingClientRect(),
        vWidth = window.innerWidth || doc.documentElement.clientWidth,
        vHeight = window.innerHeight || doc.documentElement.clientHeight,
        efp = function (x, y) {
            return document.elementFromPoint(x, y)
        };

    // Return false if it's not in the viewport
    if (rect.right < 0 || rect.bottom < 0 ||
        rect.left > vWidth || rect.top > vHeight)
        return false;

    // Return true if any of its four corners are visible
    return (
        el.contains(efp(rect.left, rect.top)) ||
        el.contains(efp(rect.right, rect.top)) ||
        el.contains(efp(rect.right, rect.bottom)) ||
        el.contains(efp(rect.left, rect.bottom))
    );
}


var getNextSibling = function (elem, selector) {
    // https://gomakethings.com/finding-the-next-and-previous-sibling-elements-that-match-a-selector-with-vanilla-js/

    // Get the next sibling element
    var sibling = elem.nextElementSibling;

    // If there's no selector, return the first sibling
    if (!selector) return sibling;

    // If the sibling matches our selector, use it
    // If not, jump to the next sibling and continue the loop
    while (sibling) {
        if (sibling.matches(selector)) return sibling;
        sibling = sibling.nextElementSibling
    }

};

var getPreviousSibling = function (elem, selector) {
    // https://gomakethings.com/finding-the-next-and-previous-sibling-elements-that-match-a-selector-with-vanilla-js/

    // Get the next sibling element
    var sibling = elem.previousElementSibling;

    // If there's no selector, return the first sibling
    if (!selector) return sibling;

    // If the sibling matches our selector, use it
    // If not, jump to the next sibling and continue the loop
    while (sibling) {
        if (sibling.matches(selector)) return sibling;
        sibling = sibling.previousElementSibling;
    }

};
