"use strict";
const statusCDN = '[Typescript - ON]';
const message = 'Ativação completa!';
console.log(`%c ${statusCDN} %c ${message} `, 'background: #111111; color: #f0eff5; font-weight: bold;', 'background: #0274B3; color: #111111; font-weight: bold;');
const navbarBTN = document.querySelector('.navbar-button');
const closeBTN = document.querySelector('.close-btn');
var sidebarDIV = document.querySelector('.sidebar');
navbarBTN?.addEventListener('click', () => {
    if (sidebarDIV?.className === "sidebar") {
        sidebarDIV?.classList.add('active');
        document.querySelector('body').style.overflow = 'hidden';
    }
});
closeBTN?.addEventListener('click', () => {
    if (sidebarDIV?.className === "sidebar active") {
        sidebarDIV?.classList.remove('active');
        document.querySelector('body').style.overflowY = 'scroll';
    }
});
const timeUpdate = document.querySelector('.time');
timeUpdate.innerText = `${new Date("2023-02-19")}`;
