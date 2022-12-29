let selection_answer = document.getElementById("ball-sel")
const ball_colors = ["Red", "Blue", "Brown", "Cyan", "Green", "Yellow", "Grey", "White"]


selection_answer.addEventListener('change', () => {
    let val = selection_answer.value;

    val = Number(val)

    // clear the select fields before refill it again
    for (let index = 1; index < 5; index++) {
        if(!(document.getElementById("ball-color-field-"+index).classList.contains("d-none"))){
            document.getElementById("ball-color-field-"+index).classList.add("d-none")
        }
    }

    for (let index = 1; index < (val+1); index++) {
        if(document.getElementById("ball-color-field-"+index).classList.contains("d-none")){
            document.getElementById("ball-color-field-"+index).classList.remove("d-none")
        }
    }

})

