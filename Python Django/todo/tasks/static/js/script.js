$(document).ready(function() {
    const statusCDN = '[JQUERY - ON]'
    const message = 'Ativação completa!'
    console.log(`%c ${statusCDN} %c ${message} `, 'background: #111111; color: #f0eff5; font-weight: bold;', 'background: #0274B3; color: #111111; font-weight: bold;');

    var deleteBTN = $('.delete-btn')
    $(deleteBTN).on('click', () => {
        var taskTitle = document.querySelector('.task-title').textContent

        if(result){
            window.location.href = '/task-list/'
            const status = '[DELETE DB]'
            const message = 'Tarefa deletada com sucesso!'
            console.log(`%c ${status} %c ${message} `, 'background: #111111; color: #f0eff5; font-weight: bold;', 'background: #0274B3; color: #111111; font-weight: bold;');
        }
    })

    var searchBTN = $('.search-btn')
    var searchForm = $('.search-form')
    $(searchBTN).on('click', () => {
        searchForm.submit()
        
    })

    var baseURL = 'http://127.0.0.1:8000/task-list/'
    var filter = $('#filter')
    $(filter).change(function(){
        var filter = $(this).val()
        window.location.href = baseURL + '?filter=' + filter
    })
})