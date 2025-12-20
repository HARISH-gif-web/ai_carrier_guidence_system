function getCareer() {
    const skills = document.getElementById("skills").value;

    document.getElementById("result").innerHTML =
        "You entered: " + skills + "<br><b>Recommended Career: AI Engineer</b>";
}