/*!
* Start Bootstrap - The Big Picture v5.0.6 (https://startbootstrap.com/template/the-big-picture)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-the-big-picture/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


let elements = document.getElementsByClassName("column");

let i;

function four() {
    for (i = 0; i < elements.length; i++) {
        elements[i].style.flex = "25%";
    }
}

