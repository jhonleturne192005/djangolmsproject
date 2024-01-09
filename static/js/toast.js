
const toast=(message)=>{
    $(".toast-body").text(message==undefined?"Inicio Correcto":message)
    const toastLiveExample = document.getElementById('liveToast')
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    toastBootstrap.show()
}


toast(undefined);

