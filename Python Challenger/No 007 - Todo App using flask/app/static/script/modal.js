$(document).ready(function () {
    console.log('Documento ativado')
    $(`#task-modal`).on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget)
        const taskID = button.data('source')
        const content = button.data('content')
        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find(`.modal-title`).text(taskID)
            $(`#task-form-display`).removeAttr('taskID')
        } else {
            modal.find(`.modal-title`).text('Edit Task ' + taskID)
            $(`#task-form-display`).attr('taskID', taskID)
        }
    
        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })
    $(`#submit-task`).click(function () {
        const tID = $(`#task-form-display`).attr('taskID');
        console.log('Item update: ' + $(`#task-modal`).find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $(`#task-modal`).find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('[Error - Update] -> Erro na atualização');
                location.reload();
            }
        });
    });
    /**/ 
    $(`.remove-task`).click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('[Error - Delete] -> Erro na exclusão');
            }
        });
    });
    /*Botões da coluna Status*/ 
    $(`.state`).click(function () {
        const state = $(this)
        const tID = state.data('source')
        var new_state = "Todo" // "var" -> para esta úica ação
        if (state.text() === "In Progress") {
            new_state = "Complete"
        }
        else if (state.text() === "Complete") {
            new_state = "Todo"
        }
        else if (state.text() === "Todo") {
            new_state = "In Progress"
        }
    
        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});