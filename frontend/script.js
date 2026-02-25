async function getCareer() {
    const skillsInput = document.getElementById("skillsInput").value;

    if (!skillsInput) {
        alert("Please enter skills");
        return;
    }

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/recommend",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    skills: skillsInput.split(",")
                })
            }
        );

        const data = await response.json();

        document.getElementById("result").innerHTML =
            "Recommended Career: " + data.recommended_career;

    } catch (error) {
        document.getElementById("result").innerHTML =
            "Backend error";
    }
}
