async function getCareer() {
    const skills = document.getElementById("skillsInput").value;

    if (!skills) {
        alert("Please enter skills");
        return;
    }

    try {
        const response = await fetch(
            "https://YOUR_RAILWAY_LINK/recommend",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    user_skills: skills
                })
            }
        );

        const data = await response.json();

        document.getElementById("result").innerHTML =
            "Recommended Career: " + data.recommended_career;

    } catch (error) {
        document.getElementById("result").innerHTML =
            "Error connecting to backend";
    }
}