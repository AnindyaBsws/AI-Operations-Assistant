class VerifierAgent:
    def verify(self, task: str, results: list):
        github_result = results[0]
        weather_result = results[1]

        parts = []

        # Weather success
        if "current_weather" in weather_result:
            temp = weather_result["current_weather"]["temperature"]
            wind = weather_result["current_weather"]["windspeed"]
            parts.append(
                f"The current weather in Berlin is {temp}°C with a wind speed of {wind} km/h."
            )

        # GitHub failure
        if "status" in github_result and github_result["status"] == "401":
            parts.append(
                "Fetching top AI repositories from GitHub failed due to invalid or missing GitHub API credentials."
            )

        if not parts:
            return "The task could not be completed due to errors in all external API calls."

        return " ".join(parts)
