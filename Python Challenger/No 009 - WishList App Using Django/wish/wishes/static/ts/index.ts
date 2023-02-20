const statusCDN = '[Typescript (SCRIPT) - ON]';
const message = 'Ativação completa!';
console.log(`%c ${statusCDN} %c ${message} `, 'background: #111111; color: #f0eff5; font-weight: bold;', 'background: #0274B3; color: #111111; font-weight: bold;');

// ========== SIDEBAR ==========
const navbarBTN = document.querySelector('.navbar-button');
const closeBTN = document.querySelector('.close-btn');
var sidebarDIV = document.querySelector('.sidebar');
navbarBTN?.addEventListener('click', () => {
    if (sidebarDIV?.className === "sidebar") {
        sidebarDIV?.classList.add('active');
        document.querySelector('body').style.overflow = 'hidden'
    }
});

closeBTN?.addEventListener('click', () => {
    if (sidebarDIV?.className === "sidebar active") {
        sidebarDIV?.classList.remove('active');
        document.querySelector('body').style.overflowY = 'scroll'
    }
});

const timeUpdate = document.querySelector('.time')
timeUpdate.innerText = `${new Date("2023-02-19")}`

// ========== DASHBOARD ==========
const wishAndamento = document.querySelector('.wish_adn')?.textContent
const wishRealizado = document.querySelector('.wish_adn')?.textContent
const ctx = document.querySelector('#show_chart');
new Chart(ctx, {
    type: 'pie',
    data: {
        datasets: [{
                data: [parseInt(wishAndamento), parseInt(wishRealizado)]
            }],
        labels: [
            'Em Andamento',
            'Realizados'
        ],
    },
    options: {
        responsive: true
    }
});
