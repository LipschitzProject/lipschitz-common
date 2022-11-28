var request_data_button = document.getElementById('request-data')
request_data_button.onclick = function() {
    fetch(window.location.origin + '/download', {
        method: 'POST',  // how to add header and data?

    }).then(response => {
        console.log(response)
    }).catch(error => {
        console.log(`Error: ${error}`)
    })
}